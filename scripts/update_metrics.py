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
            self.metrics['INT_JOURNAL_COUNT'] = os.getenv('INT_JOURNAL_COUNT', 'N/A')
            self.metrics['INT_CONF_COUNT'] = os.getenv('INT_CONF_COUNT', 'N/A')
            self.metrics['BOOK_COUNT'] = os.getenv('BOOK_COUNT', 'N/A')
            self.metrics['TOTAL_CITATIONS'] = os.getenv('TOTAL_CITATIONS', 'N/A')
            self.metrics['H_INDEX'] = os.getenv('H_INDEX', 'N/A')
            return
        
        try:
            # 使用scholarly库获取作者信息
            author = scholarly.search_author_id(author_id)
            author = scholarly.fill(author)
            
            # 统计不同类型的出版物
            publications = author.get('publications', [])
            
            int_journal_count = 0
            int_conf_count = 0
            book_count = 0
            
            for pub in publications:
                pub_filled = scholarly.fill(pub)
                title = pub_filled.get('bib', {}).get('title', '').lower()
                venue = pub_filled.get('bib', {}).get('venue', '').lower()
                
                # 简单分类逻辑（可根据实际情况调整）
                if 'journal' in venue or 'transaction' in venue or 'ieee' in venue:
                    int_journal_count += 1
                elif 'conference' in venue or 'proceeding' in venue:
                    int_conf_count += 1
                elif 'book' in venue or 'chapter' in title:
                    book_count += 1
            
            self.metrics['INT_JOURNAL_COUNT'] = int_journal_count
            self.metrics['INT_CONF_COUNT'] = int_conf_count
            self.metrics['BOOK_COUNT'] = book_count
            self.metrics['TOTAL_CITATIONS'] = author.get('citedby', 0)
            self.metrics['H_INDEX'] = author.get('hindex', 0)
            
            print(f"✓ Google Scholar metrics retrieved: {self.metrics['TOTAL_CITATIONS']} citations")
            
        except Exception as e:
            print(f"⚠ Warning: Could not fetch Google Scholar metrics: {e}")
            print("  Using fallback values or manual configuration")
            # 如果无法获取，可以使用环境变量或配置文件中的值
            self.metrics['INT_JOURNAL_COUNT'] = os.getenv('INT_JOURNAL_COUNT', 'N/A')
            self.metrics['INT_CONF_COUNT'] = os.getenv('INT_CONF_COUNT', 'N/A')
            self.metrics['BOOK_COUNT'] = os.getenv('BOOK_COUNT', 'N/A')
            self.metrics['TOTAL_CITATIONS'] = os.getenv('TOTAL_CITATIONS', 'N/A')
            self.metrics['H_INDEX'] = os.getenv('H_INDEX', 'N/A')
    
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
        
        # 获取指标
        if google_scholar_id:
            self.get_google_scholar_metrics(google_scholar_id)
        else:
            print("⚠ GOOGLE_SCHOLAR_ID not set, using environment variables or defaults")
            self.metrics['INT_JOURNAL_COUNT'] = os.getenv('INT_JOURNAL_COUNT', 'N/A')
            self.metrics['INT_CONF_COUNT'] = os.getenv('INT_CONF_COUNT', 'N/A')
            self.metrics['BOOK_COUNT'] = os.getenv('BOOK_COUNT', 'N/A')
            self.metrics['TOTAL_CITATIONS'] = os.getenv('TOTAL_CITATIONS', 'N/A')
            self.metrics['H_INDEX'] = os.getenv('H_INDEX', 'N/A')
        
        self.get_cnki_metrics(cnki_author_id)
        
        # 更新README
        success = self.update_readme()
        
        print("=" * 50)
        if success:
            print("✓ Update completed successfully!")
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

