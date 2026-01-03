# 出版物指标自动更新脚本

这个目录包含用于自动更新README.md中出版物指标的脚本。

## 功能

- 从Google Scholar自动获取国际期刊论文数量、引用数和H-index
- 从CNKI获取中文期刊论文数量（需要API密钥）
- 自动更新README.md中的指标表格
- 支持GitHub Actions自动运行

## 设置

### 1. 安装依赖

```bash
pip install scholarly requests beautifulsoup4 lxml
```

### 2. 配置环境变量

在GitHub仓库的Settings > Secrets and variables > Actions中添加以下密钥：

- `GOOGLE_SCHOLAR_ID`: 您的Google Scholar作者ID
- `CNKI_AUTHOR_ID`: 您的CNKI作者ID（可选）
- `CNKI_API_KEY`: CNKI API密钥（可选）

### 3. 手动设置指标（如果无法自动获取）

如果无法自动获取数据，可以在GitHub Secrets中设置：

- `INT_JOURNAL_COUNT`: 国际期刊论文数量
- `CN_JOURNAL_COUNT`: 中文期刊论文数量
- `INT_CONF_COUNT`: 国际会议论文数量
- `BOOK_COUNT`: 书籍/章节数量
- `TOTAL_CITATIONS`: 总引用数
- `H_INDEX`: H-index

### 4. 本地测试

```bash
# 设置环境变量
export GOOGLE_SCHOLAR_ID="your_scholar_id"
export CNKI_AUTHOR_ID="your_cnki_id"

# 运行脚本
python scripts/update_metrics.py
```

## 注意事项

1. **Google Scholar限制**: Google Scholar有反爬虫机制，频繁请求可能被限制。建议：
   - 使用代理服务器
   - 降低更新频率
   - 考虑使用Google Scholar API（如果可用）

2. **CNKI访问**: CNKI可能需要：
   - 官方API密钥
   - 或使用爬虫（需遵守网站使用条款和robots.txt）

3. **更新频率**: GitHub Actions工作流默认每天运行一次，可以在`.github/workflows/update-publication-metrics.yml`中修改。

4. **手动更新**: 如果自动更新失败，可以：
   - 手动运行GitHub Action（在Actions页面点击"Run workflow"）
   - 或直接编辑README.md中的指标值

## 故障排除

### 问题：无法获取Google Scholar数据

**解决方案**:
1. 检查`GOOGLE_SCHOLAR_ID`是否正确
2. 尝试使用代理
3. 使用环境变量手动设置指标

### 问题：CNKI数据无法获取

**解决方案**:
1. 申请CNKI API密钥
2. 或使用环境变量`CN_JOURNAL_COUNT`手动设置
3. 考虑使用其他中文数据库API

### 问题：GitHub Action失败

**解决方案**:
1. 检查GitHub Secrets是否正确设置
2. 查看Actions日志了解具体错误
3. 确保仓库有写入权限

## 扩展

如果需要添加其他数据源（如ORCID、ResearchGate等），可以：

1. 在`update_metrics.py`中添加新的获取方法
2. 在README.md中添加对应的指标行
3. 在GitHub Actions中添加相应的环境变量

