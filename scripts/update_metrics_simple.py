#!/usr/bin/env python3
"""
简化版指标更新脚本
从环境变量或配置文件读取指标值并更新README.md
适用于无法自动获取数据的情况
"""

import re
import os
import sys
import json
from datetime import datetime
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class SimpleMetricsUpdater:
    def __init__(self, readme_path="README.md", config_path=None):
        self.readme_path = Path(readme_path)
        self.config_path = config_path
        self.metrics = {
            'INT_JOURNAL_COUNT': 0,
            'CN_JOURNAL_COUNT': 0,
            'INT_CONF_COUNT': 0,
            'BOOK_COUNT': 0,
            'TOTAL_CITATIONS': 0,
            'H_INDEX': 0,
            'LAST_UPDATE': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
        }
    
    def load_from_config(self):
        """从配置文件加载指标"""
        if self.config_path and Path(self.config_path).exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    manual = config.get('manual_metrics', {})
                    
                    self.metrics['INT_JOURNAL_COUNT'] = manual.get('int_journal_count', 0)
                    self.metrics['CN_JOURNAL_COUNT'] = manual.get('cn_journal_count', 0)
                    self.metrics['INT_CONF_COUNT'] = manual.get('int_conf_count', 0)
                    self.metrics['BOOK_COUNT'] = manual.get('book_count', 0)
                    self.metrics['TOTAL_CITATIONS'] = manual.get('total_citations', 0)
                    self.metrics['H_INDEX'] = manual.get('h_index', 0)
                    
                    print(f"✓ Loaded metrics from config file")
                    return True
            except Exception as e:
                print(f"⚠ Warning: Could not load config: {e}")
        
        return False
    
    def load_from_env(self):
        """从环境变量加载指标"""
        env_mapping = {
            'INT_JOURNAL_COUNT': 'INT_JOURNAL_COUNT',
            'CN_JOURNAL_COUNT': 'CN_JOURNAL_COUNT',
            'INT_CONF_COUNT': 'INT_CONF_COUNT',
            'BOOK_COUNT': 'BOOK_COUNT',
            'TOTAL_CITATIONS': 'TOTAL_CITATIONS',
            'H_INDEX': 'H_INDEX'
        }
        
        loaded = False
        for key, env_key in env_mapping.items():
            value = os.getenv(env_key)
            if value:
                try:
                    self.metrics[key] = int(value)
                    loaded = True
                except ValueError:
                    self.metrics[key] = value
        
        if loaded:
            print(f"✓ Loaded metrics from environment variables")
        
        return loaded
    
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
        print("Simple Publication Metrics Updater")
        print("=" * 50)
        
        # 尝试从配置文件加载
        if not self.load_from_config():
            # 如果配置文件不存在，尝试从环境变量加载
            if not self.load_from_env():
                print("⚠ No config file or environment variables found")
                print("  Using default values (0)")
        
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
    config_path = os.getenv('METRICS_CONFIG', 'scripts/config.json')
    updater = SimpleMetricsUpdater(config_path=config_path)
    success = updater.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

