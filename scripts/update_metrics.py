#!/usr/bin/env python3
"""
自动更新README.md中的出版物指标
从Google Scholar、Web of Science和CNKI获取数据并更新README.md文件
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
            'TOTAL_PUBLICATIONS': 0,  # 从Google Scholar获取总论文数
            'INT_JOURNAL_COUNT': 0,  # 从Web of Science获取
            'INT_CONF_COUNT': 0,  # 从Web of Science获取
            'BOOK_COUNT': 0,  # 从Web of Science获取
            'SCI_PAPERS_COUNT': 0,  # 从Web of Science获取
            'JCR_Q1_COUNT': 0,  # 从Web of Science获取
            'IEEE_TRANS_COUNT': 0,  # 从Web of Science获取
            'CN_JOURNAL_COUNT': 0,  # 从CNKI获取
            'TOTAL_CITATIONS': 0,  # 从Google Scholar获取
            'H_INDEX': 0,  # 从Google Scholar获取
            'LAST_UPDATE': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
        
    def get_google_scholar_metrics(self, author_id=None):
        """
        从Google Scholar获取指标：总论文数、总引用数、H-index
        注意：Google Scholar有反爬虫机制，可能需要使用代理或API
        """
        # 如果author_id为空，直接使用环境变量回退
        if not author_id:
            print("⚠ Google Scholar author_id not provided, using environment variables")
            self._load_from_env(['TOTAL_PUBLICATIONS', 'TOTAL_CITATIONS', 'H_INDEX'])
            return
        
        try:
            print(f"🔍 Attempting to fetch Google Scholar data for author ID: {author_id}")
            # 使用scholarly库获取作者信息
            author = scholarly.search_author_id(author_id)
            author = scholarly.fill(author)
            
            # 获取基本指标
            total_citations = author.get('citedby', 0)
            h_index = author.get('hindex', 0)
            
            # 获取总论文数（所有出版物数量）
            publications = author.get('publications', [])
            total_publications = len(publications)
            
            print(f"  Found {total_publications} total publications")
            print(f"  Found {total_citations} total citations, H-index: {h_index}")
            
            # 如果成功获取到数据，使用这些值
            if total_publications > 0 or total_citations > 0 or h_index > 0:
                self.metrics['TOTAL_PUBLICATIONS'] = total_publications
                self.metrics['TOTAL_CITATIONS'] = total_citations
                self.metrics['H_INDEX'] = h_index
                
                print(f"✓ Google Scholar metrics retrieved successfully:")
                print(f"  - Total Publications: {total_publications}")
                print(f"  - Total Citations: {total_citations}")
                print(f"  - H-index: {h_index}")
            else:
                # 如果获取的数据为空，回退到环境变量
                print("⚠ Google Scholar returned empty data, falling back to environment variables")
                self._load_from_env(['TOTAL_PUBLICATIONS', 'TOTAL_CITATIONS', 'H_INDEX'])
            
        except Exception as e:
            print(f"⚠ Warning: Could not fetch Google Scholar metrics: {e}")
            print(f"  Error type: {type(e).__name__}")
            import traceback
            print(f"  Traceback: {traceback.format_exc()}")
            print("  Using fallback values from environment variables")
            # 如果无法获取，使用环境变量
            self._load_from_env(['TOTAL_PUBLICATIONS', 'TOTAL_CITATIONS', 'H_INDEX'])
    
    def get_web_of_science_metrics(self, api_key=None, author_name=None, orcid=None, researcher_id=None):
        """
        从Web of Science获取指标
        支持通过API或环境变量获取数据
        
        Web of Science API通常需要：
        - API密钥（WOS_API_KEY）
        - 作者标识：ResearcherID（推荐）、ORCID ID 或作者姓名
        """
        print("🔍 Attempting to fetch Web of Science data...")
        
        # 优先尝试使用API（如果提供了API密钥）
        if api_key:
            try:
                print("  Using Web of Science API...")
                # Web of Science API调用
                # 注意：实际API端点和格式可能因版本而异
                # 这里提供一个基础框架
                
                # 构建查询参数（优先级：ResearcherID > ORCID > 作者姓名）
                query_params = {}
                if researcher_id:
                    query_params['researcher_id'] = researcher_id
                    print(f"    Using ResearcherID: {researcher_id}")
                elif orcid:
                    query_params['orcid'] = orcid
                    print(f"    Using ORCID: {orcid}")
                elif author_name:
                    query_params['author'] = author_name
                    print(f"    Using Author Name: {author_name}")
                
                # Web of Science API端点（示例，需要根据实际API文档调整）
                # api_url = "https://api.clarivate.com/api/wos"
                # headers = {
                #     'X-ApiKey': api_key,
                #     'Content-Type': 'application/json'
                # }
                # 
                # response = requests.get(api_url, headers=headers, params=query_params, timeout=30)
                # 
                # if response.status_code == 200:
                #     data = response.json()
                #     # 解析返回的数据
                #     # 注意：实际数据结构需要根据API文档调整
                #     self.metrics['INT_JOURNAL_COUNT'] = data.get('journal_papers', 0)
                #     self.metrics['INT_CONF_COUNT'] = data.get('conference_papers', 0)
                #     self.metrics['BOOK_COUNT'] = data.get('books_chapters', 0)
                #     self.metrics['SCI_PAPERS_COUNT'] = data.get('sci_indexed', 0)
                #     self.metrics['JCR_Q1_COUNT'] = data.get('jcr_q1', 0)
                #     self.metrics['IEEE_TRANS_COUNT'] = data.get('ieee_transactions', 0)
                #     print("✓ Web of Science API data retrieved successfully")
                #     return
                # else:
                #     print(f"⚠ Web of Science API returned status {response.status_code}")
                
                # 由于Web of Science API需要付费访问，这里先使用环境变量回退
                print("  ⚠ Web of Science API access requires paid subscription")
                print("  Falling back to environment variables...")
                
            except Exception as e:
                print(f"  ⚠ Warning: Web of Science API call failed: {e}")
                print("  Falling back to environment variables...")
        
        # 从环境变量加载Web of Science指标
        print("  Loading Web of Science metrics from environment variables...")
        self._load_from_env([
            'INT_JOURNAL_COUNT',
            'INT_CONF_COUNT',
            'BOOK_COUNT',
            'SCI_PAPERS_COUNT',
            'JCR_Q1_COUNT',
            'IEEE_TRANS_COUNT'
        ])
    
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
            cn_count = os.getenv('CN_JOURNAL_COUNT')
            if cn_count:
                try:
                    self.metrics['CN_JOURNAL_COUNT'] = int(cn_count)
                except ValueError:
                    self.metrics['CN_JOURNAL_COUNT'] = cn_count
            else:
                self.metrics['CN_JOURNAL_COUNT'] = 0
            print(f"✓ CNKI metrics retrieved: {self.metrics['CN_JOURNAL_COUNT']} Chinese journal papers")
            
        except Exception as e:
            print(f"⚠ Warning: Could not fetch CNKI metrics: {e}")
            cn_count = os.getenv('CN_JOURNAL_COUNT', '0')
            try:
                self.metrics['CN_JOURNAL_COUNT'] = int(cn_count)
            except ValueError:
                self.metrics['CN_JOURNAL_COUNT'] = 0
    
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
        
        # 从环境变量获取ID和配置
        google_scholar_id = os.getenv('GOOGLE_SCHOLAR_ID')
        cnki_author_id = os.getenv('CNKI_AUTHOR_ID')
        wos_api_key = os.getenv('WOS_API_KEY')
        wos_author_name = os.getenv('WOS_AUTHOR_NAME')
        wos_orcid = os.getenv('WOS_ORCID')
        wos_researcher_id = os.getenv('WOS_RESEARCHER_ID')
        
        print(f"📋 Configuration:")
        print(f"  - GOOGLE_SCHOLAR_ID: {'Set' if google_scholar_id else 'Not set'}")
        print(f"  - CNKI_AUTHOR_ID: {'Set' if cnki_author_id else 'Not set'}")
        print(f"  - WOS_API_KEY: {'Set' if wos_api_key else 'Not set'}")
        print(f"  - WOS_RESEARCHER_ID: {'Set' if wos_researcher_id else 'Not set'}")
        print(f"  - WOS_ORCID: {'Set' if wos_orcid else 'Not set'}")
        print(f"  - WOS_AUTHOR_NAME: {'Set' if wos_author_name else 'Not set'}")
        print()
        
        # 获取Google Scholar指标（总论文数、引用数、H-index）
        if google_scholar_id:
            self.get_google_scholar_metrics(google_scholar_id)
        else:
            print("⚠ GOOGLE_SCHOLAR_ID not set, using environment variables or defaults")
            self._load_from_env(['TOTAL_PUBLICATIONS', 'TOTAL_CITATIONS', 'H_INDEX'])
        
        # 获取Web of Science指标（优先级：ResearcherID > ORCID > 作者姓名）
        self.get_web_of_science_metrics(
            api_key=wos_api_key,
            researcher_id=wos_researcher_id,
            orcid=wos_orcid,
            author_name=wos_author_name
        )
        
        # 获取CNKI指标
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
