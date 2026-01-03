#!/usr/bin/env python3
"""
自动更新README.md中的出版物指标
从Google Scholar和CNKI获取数据并更新README.md文件
"""

import re
import os
import sys
from datetime import datetime
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from scholarly import scholarly
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"Error importing required packages: {e}")
    print("Please install: pip install scholarly requests beautifulsoup4 lxml")
    sys.exit(1)


class PublicationMetricsUpdater:
    def __init__(self, readme_path="README.md"):
        self.readme_path = Path(readme_path)
        self.metrics = {
            'INT_JOURNAL_COUNT': 0,
            'CN_JOURNAL_COUNT': 0,
            'INT_CONF_COUNT': 0,
            'BOOK_COUNT': 0,
            'TOTAL_CITATIONS': 0,
            'H_INDEX': 0,
            'LAST_UPDATE': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        
    def get_google_scholar_metrics(self, author_id=None):
        """
        从Google Scholar获取指标
        注意：Google Scholar有反爬虫机制，可能需要使用代理或API
        """
        # 如果author_id为空，直接使用环境变量回退
        if not author_id:
            print("⚠ Google Scholar author_id not provided, using environment variables")
            self._load_from_env(['INT_JOURNAL_COUNT', 'INT_CONF_COUNT', 'BOOK_COUNT', 'TOTAL_CITATIONS', 'H_INDEX'])
            return
        
        try:
            print(f"🔍 Attempting to fetch Google Scholar data for author ID: {author_id}")
            # 使用scholarly库获取作者信息
            author = scholarly.search_author_id(author_id)
            author = scholarly.fill(author)
            
            # 获取基本指标
            total_citations = author.get('citedby', 0)
            h_index = author.get('hindex', 0)
            
            print(f"  Found {total_citations} total citations, H-index: {h_index}")
            
            # 统计不同类型的出版物
            publications = author.get('publications', [])
            print(f"  Processing {len(publications)} publications...")
            
            int_journal_count = 0
            int_conf_count = 0
            book_count = 0
            
            # 限制处理数量以避免超时（Google Scholar可能返回大量出版物）
            max_pubs = 200
            processed_count = 0
            skipped_count = 0
            unclassified_count = 0
            sample_venues = []  # 用于调试，显示一些venue示例
            
            # 扩展的关键词列表
            journal_keywords = [
                'journal', 'transaction', 'ieee', 'ieee transactions', 'ieee trans',
                'springer', 'elsevier', 'acm transactions', 'siam', 'nature', 'science',
                'cell', 'plos', 'biosystems', 'ocean engineering', 'automatica', 'control',
                'robotics', 'transactions on', 'journal of', 'international journal',
                'applied', 'engineering', 'systems', 'computing', 'informatics'
            ]
            
            conf_keywords = [
                'conference', 'proceeding', 'symposium', 'workshop', 'icml', 'neurips',
                'iccv', 'cvpr', 'aaai', 'ijcai', 'ieee conference', 'acm conference',
                'ifac', 'ieee', 'acm', 'ieee/acm', 'international conference',
                'annual conference', 'workshop on', 'symposium on'
            ]
            
            book_keywords = [
                'book', 'chapter', 'monograph', 'handbook', 'encyclopedia',
                'series', 'volume', 'edition'
            ]
            
            for i, pub in enumerate(publications[:max_pubs]):
                try:
                    pub_filled = scholarly.fill(pub)
                    bib = pub_filled.get('bib', {})
                    title = bib.get('title', '').lower()
                    venue = bib.get('venue', '').lower() if bib.get('venue') else ''
                    pub_type = bib.get('pub_type', '').lower() if bib.get('pub_type') else ''
                    
                    # 收集venue示例用于调试（前10个）
                    if i < 10 and venue:
                        sample_venues.append(f"  [{i+1}] venue='{venue[:60]}...' pub_type='{pub_type}'")
                    
                    classified = False
                    
                    # 策略1: 检查pub_type字段（如果存在）
                    if pub_type:
                        if any(kw in pub_type for kw in ['article', 'journal', 'paper']):
                            int_journal_count += 1
                            classified = True
                        elif any(kw in pub_type for kw in ['conference', 'proceeding', 'workshop', 'symposium']):
                            int_conf_count += 1
                            classified = True
                        elif any(kw in pub_type for kw in ['book', 'chapter', 'monograph']):
                            book_count += 1
                            classified = True
                    
                    # 策略2: 检查venue字段（如果未分类且venue存在）
                    if not classified and venue:
                        # 期刊匹配（更严格的匹配）
                        if any(kw in venue for kw in journal_keywords):
                            # 排除会议关键词，避免误判
                            if not any(kw in venue for kw in ['conference', 'proceeding', 'workshop', 'symposium']):
                                int_journal_count += 1
                                classified = True
                        
                        # 会议匹配
                        if not classified and any(kw in venue for kw in conf_keywords):
                            int_conf_count += 1
                            classified = True
                        
                        # 书籍匹配
                        if not classified and any(kw in venue for kw in book_keywords):
                            book_count += 1
                            classified = True
                    
                    # 策略3: 启发式判断（如果仍未分类）
                    if not classified and venue:
                        # 检查venue长度和格式
                        venue_clean = venue.strip()
                        
                        # 期刊通常：名称较长，不包含年份，可能包含"Transactions"、"Journal"等
                        if len(venue_clean) > 15:
                            # 检查是否包含年份（通常是4位数字在末尾或中间）
                            has_year = bool(re.search(r'\b(19|20)\d{2}\b', venue_clean))
                            
                            if not has_year and ('trans' in venue_clean or 'journal' in venue_clean or 'engineering' in venue_clean):
                                int_journal_count += 1
                                classified = True
                            elif has_year and ('conference' in venue_clean or 'proceeding' in venue_clean):
                                int_conf_count += 1
                                classified = True
                            elif has_year:
                                # 包含年份但不确定，倾向于会议
                                int_conf_count += 1
                                classified = True
                    
                    # 策略4: 检查标题（最后的手段）
                    if not classified and title:
                        if any(kw in title for kw in book_keywords):
                            book_count += 1
                            classified = True
                    
                    if not classified:
                        unclassified_count += 1
                        # 默认归类：如果有venue但无法分类，倾向于期刊（因为期刊更常见）
                        if venue:
                            int_journal_count += 1
                        else:
                            # 没有venue信息，无法判断，跳过
                            skipped_count += 1
                            continue
                    
                    processed_count += 1
                    
                except Exception as e:
                    # 如果单个出版物处理失败，继续处理下一个
                    skipped_count += 1
                    if skipped_count <= 5:  # 只显示前5个错误，避免日志过长
                        print(f"  ⚠ Warning: Could not process publication {i+1}: {e}")
                    continue
            
            # 显示调试信息
            print(f"  Processed {processed_count} publications, skipped {skipped_count}, unclassified {unclassified_count}")
            print(f"  Classification results: Journals={int_journal_count}, Conferences={int_conf_count}, Books={book_count}")
            
            # 显示venue示例（用于调试）
            if sample_venues:
                print(f"  Sample venues (first 10):")
                for sample in sample_venues[:5]:  # 只显示前5个
                    print(sample)
            
            # 如果分类结果全部为0，可能是分类失败，建议使用环境变量
            if int_journal_count == 0 and int_conf_count == 0 and book_count == 0 and processed_count > 0:
                print(f"  ⚠ Warning: All classifications are 0, but {processed_count} publications were processed")
                print(f"     This suggests classification may have failed. Falling back to environment variables.")
                self._load_from_env(['INT_JOURNAL_COUNT', 'INT_CONF_COUNT', 'BOOK_COUNT'])
                return
            
            # 如果成功获取到数据，使用这些值
            if total_citations > 0 or h_index > 0:
                # 总引用数和H-index总是从Google Scholar获取（如果成功）
                self.metrics['TOTAL_CITATIONS'] = total_citations
                self.metrics['H_INDEX'] = h_index
                
                # 对于计数类指标，优先使用Google Scholar分类结果（如果非0）
                # 如果分类结果为0，才使用环境变量作为备用
                print("  🔍 Determining final values for counts (prioritizing Google Scholar results)...")
                
                # 映射关系
                count_mapping = {
                    'INT_JOURNAL_COUNT': int_journal_count,
                    'INT_CONF_COUNT': int_conf_count,
                    'BOOK_COUNT': book_count
                }
                
                for key, classification_value in count_mapping.items():
                    # 优先使用Google Scholar分类结果（如果非0）
                    if classification_value > 0:
                        self.metrics[key] = classification_value
                        print(f"    ✓ Using {key} from Google Scholar classification: {classification_value}")
                    else:
                        # 分类结果为0，检查环境变量作为备用
                        env_val = os.getenv(key)
                        if env_val and env_val.strip():
                            try:
                                env_int = int(env_val.strip())
                                if env_int > 0:
                                    self.metrics[key] = env_int
                                    print(f"    ✓ Using {key} from environment (fallback): {env_int}")
                                else:
                                    # 环境变量也为0，保持0
                                    self.metrics[key] = 0
                                    print(f"    ⚠ {key} is 0 in both classification and environment, keeping 0")
                            except ValueError:
                                # 环境变量不是有效数字，保持分类结果（0）
                                self.metrics[key] = 0
                                print(f"    ⚠ {key} in environment is not a valid number: '{env_val}', keeping classification result (0)")
                        else:
                            # 环境变量不存在或为空，保持分类结果（0）
                            self.metrics[key] = 0
                            print(f"    ⚠ {key} not found in environment, keeping classification result (0)")
                
                print(f"✓ Google Scholar metrics retrieved successfully:")
                print(f"  - International Journals: {self.metrics['INT_JOURNAL_COUNT']} (from {'Google Scholar' if int_journal_count > 0 else 'environment/fallback'})")
                print(f"  - International Conferences: {self.metrics['INT_CONF_COUNT']} (from {'Google Scholar' if int_conf_count > 0 else 'environment/fallback'})")
                print(f"  - Books/Chapters: {self.metrics['BOOK_COUNT']} (from {'Google Scholar' if book_count > 0 else 'environment/fallback'})")
                print(f"  - Total Citations: {total_citations} (from Google Scholar)")
                print(f"  - H-index: {h_index} (from Google Scholar)")
            else:
                # 如果获取的数据为空，回退到环境变量
                print("⚠ Google Scholar returned empty data, falling back to environment variables")
                self._load_from_env(['INT_JOURNAL_COUNT', 'INT_CONF_COUNT', 'BOOK_COUNT', 'TOTAL_CITATIONS', 'H_INDEX'])
            
        except Exception as e:
            print(f"⚠ Warning: Could not fetch Google Scholar metrics: {e}")
            print(f"  Error type: {type(e).__name__}")
            import traceback
            print(f"  Traceback: {traceback.format_exc()}")
            print("  Using fallback values from environment variables")
            # 如果无法获取，使用环境变量
            self._load_from_env(['INT_JOURNAL_COUNT', 'INT_CONF_COUNT', 'BOOK_COUNT', 'TOTAL_CITATIONS', 'H_INDEX'])
    
    def _load_from_env(self, keys):
        """从环境变量加载指定的指标"""
        loaded_any = False
        print(f"  🔍 Loading from environment variables: {', '.join(keys)}")
        
        for key in keys:
            value = os.getenv(key)
            # 详细诊断信息
            if value is None:
                print(f"    ❌ {key}: Not set (None)")
            elif value == '':
                print(f"    ❌ {key}: Empty string (Secret may be empty)")
            elif value.strip() == '':
                print(f"    ❌ {key}: Only whitespace (Secret may be empty)")
            else:
                print(f"    ✓ {key}: Found (value length: {len(value)})")
            
            if value and value.strip():  # 检查是否存在且不为空（包括去除空白后）
                try:
                    # 尝试转换为整数
                    int_value = int(value.strip())
                    self.metrics[key] = int_value
                    loaded_any = True
                    print(f"    ✓ Loaded {key} from environment: {int_value}")
                except ValueError:
                    # 如果无法转换为整数，使用原始值
                    self.metrics[key] = value.strip()
                    loaded_any = True
                    print(f"    ✓ Loaded {key} from environment (as string): {self.metrics[key]}")
            else:
                # 如果环境变量不存在或为空，保持当前值
                current_value = self.metrics.get(key, 0)
                print(f"    ⚠ {key} not found or empty in environment, keeping current value: {current_value}")
        
        if not loaded_any:
            print(f"  ⚠ Warning: No valid environment variables found for {', '.join(keys)}")
            print(f"     Please check GitHub Secrets:")
            for key in keys:
                print(f"       - {key}")
            print(f"     Make sure the values are not empty and are valid numbers")
    
    def get_cnki_metrics(self, author_id=None):
        """
        从CNKI获取中文期刊论文数量
        注意：CNKI需要登录和API访问，这里提供基础框架
        """
        try:
            # CNKI API调用示例（需要实际的API密钥）
            cnki_api_key = os.getenv('CNKI_API_KEY')
            if cnki_api_key and author_id:
                # 这里应该调用CNKI API
                # 示例URL格式（实际API可能不同）
                # url = f"https://api.cnki.net/v1/author/{author_id}/papers"
                # response = requests.get(url, headers={'Authorization': f'Bearer {cnki_api_key}'})
                # data = response.json()
                # self.metrics['CN_JOURNAL_COUNT'] = data.get('count', 0)
                pass
            
            # 如果无法获取，使用环境变量
            self.metrics['CN_JOURNAL_COUNT'] = os.getenv('CN_JOURNAL_COUNT', 'N/A')
            print(f"✓ CNKI metrics retrieved: {self.metrics['CN_JOURNAL_COUNT']} Chinese journal papers")
            
        except Exception as e:
            print(f"⚠ Warning: Could not fetch CNKI metrics: {e}")
            self.metrics['CN_JOURNAL_COUNT'] = os.getenv('CN_JOURNAL_COUNT', 'N/A')
    
    def update_readme(self):
        """更新README.md文件中的指标"""
        if not self.readme_path.exists():
            print(f"Error: {self.readme_path} not found")
            return False
        
        content = self.readme_path.read_text(encoding='utf-8')
        
        # 更新每个指标
        for key, value in self.metrics.items():
            # 查找并替换注释标记中的值
            pattern = f'<!-- {key} -->.*?<!-- /{key} -->'
            replacement = f'<!-- {key} -->{value}<!-- /{key} -->'
            
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                print(f"✓ Updated {key}: {value}")
            else:
                print(f"⚠ Warning: Pattern for {key} not found in README.md")
        
        # 写回文件
        self.readme_path.write_text(content, encoding='utf-8')
        print(f"\n✓ Successfully updated {self.readme_path}")
        return True
    
    def run(self):
        """运行完整的更新流程"""
        print("=" * 50)
        print("Publication Metrics Updater")
        print("=" * 50)
        
        # 从环境变量获取ID
        google_scholar_id = os.getenv('GOOGLE_SCHOLAR_ID')
        cnki_author_id = os.getenv('CNKI_AUTHOR_ID')
        
        print(f"📋 Configuration:")
        print(f"  - GOOGLE_SCHOLAR_ID: {'Set' if google_scholar_id else 'Not set'}")
        print(f"  - CNKI_AUTHOR_ID: {'Set' if cnki_author_id else 'Not set'}")
        print()
        
        # 获取指标
        if google_scholar_id:
            self.get_google_scholar_metrics(google_scholar_id)
        else:
            print("⚠ GOOGLE_SCHOLAR_ID not set, using environment variables or defaults")
            self._load_from_env(['INT_JOURNAL_COUNT', 'INT_CONF_COUNT', 'BOOK_COUNT', 'TOTAL_CITATIONS', 'H_INDEX'])
        
        self.get_cnki_metrics(cnki_author_id)
        
        # 更新README
        success = self.update_readme()
        
        print("=" * 50)
        if success:
            print("✓ Update completed successfully!")
            print(f"  Final metrics:")
            for key, value in self.metrics.items():
                if key != 'LAST_UPDATE':
                    print(f"    - {key}: {value}")
        else:
            print("✗ Update failed!")
        print("=" * 50)
        
        return success


def main():
    """主函数"""
    updater = PublicationMetricsUpdater()
    success = updater.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

