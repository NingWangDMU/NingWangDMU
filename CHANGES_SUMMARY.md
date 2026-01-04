# 更新摘要

## ✅ 已完成的更改

### 1. 更新时间调整
- **修改前**: 每天UTC时间凌晨2点运行（北京时间上午10点）
- **修改后**: 每周一北京时间凌晨0点运行（UTC时间周日16点）
- **文件**: `.github/workflows/update-publication-metrics.yml`

### 2. Google Scholar数据获取调整
- **修改前**: 从Google Scholar分类统计国际期刊、会议、书籍数量
- **修改后**: 从Google Scholar获取**总论文数（Total Publications）**，不再进行分类统计
- **文件**: `scripts/update_metrics.py`

### 3. 新增Web of Science数据源
- 添加了Web of Science数据获取功能
- 支持通过API自动获取（如果配置了API密钥）
- 支持通过环境变量手动设置（作为回退方案）
- **新增指标**：
  - International Journal Papers（国际期刊论文）
  - International Conference Papers（国际会议论文）
  - Books/Chapters（图书/章节）
  - SCI-indexed Papers（SCI索引论文）
  - JCR Q1 Papers（JCR Q1期刊论文）
  - IEEE Transactions（IEEE Transactions论文）

### 4. README.md表格更新
- 添加了"Total Publications"行（数据源：Google Scholar）
- 将International Journal Papers、International Conference Papers、Books/Chapters的数据源改为Web of Science
- 新增三行指标：
  - SCI-indexed Papers
  - JCR Q1 Papers
  - IEEE Transactions

### 5. 工作流文件更新
- 添加了Web of Science相关的环境变量配置
- 更新了环境变量检查日志

## 📋 需要设置的GitHub Secrets

### 必需设置（至少选择一种方式）

**方式1：Google Scholar自动获取（推荐）**
- `GOOGLE_SCHOLAR_ID`: 您的Google Scholar作者ID

**方式2：手动设置Google Scholar指标**
- `TOTAL_PUBLICATIONS`: 总论文数
- `TOTAL_CITATIONS`: 总引用数
- `H_INDEX`: H-index

### Web of Science指标（必需手动设置）

**注意**：您不需要Web of Science API密钥！只需在GitHub Secrets中手动设置以下指标值即可。

- `INT_JOURNAL_COUNT`: 国际期刊论文数
- `INT_CONF_COUNT`: 国际会议论文数
- `BOOK_COUNT`: 图书/章节数
- `SCI_PAPERS_COUNT`: SCI索引论文数
- `JCR_Q1_COUNT`: JCR Q1期刊论文数
- `IEEE_TRANS_COUNT`: IEEE Transactions论文数

**可选**（仅当您有Web of Science API访问权限时）：
- `WOS_API_KEY`: Web of Science API密钥（用于自动获取数据）
- `WOS_RESEARCHER_ID`: Web of Science ResearcherID
- `WOS_ORCID`: ORCID ID
- `WOS_AUTHOR_NAME`: 作者姓名

### 可选设置

- `CN_JOURNAL_COUNT`: 中文期刊论文数

**Web of Science API相关（仅当您有API访问权限时，通常需要付费订阅）**：
- `WOS_API_KEY`: Web of Science API密钥（用于自动获取数据）
- `WOS_RESEARCHER_ID`: Web of Science ResearcherID（**推荐**，用于API查询，优先级最高）
- `WOS_ORCID`: ORCID ID（用于API查询，如果未设置ResearcherID）
- `WOS_AUTHOR_NAME`: 作者姓名（用于API查询，仅在前两者都未设置时使用）

**注意**：如果没有API访问权限，只需手动设置上述Web of Science指标值即可，无需API密钥。

## 🚀 下一步操作

1. **设置GitHub Secrets**：
   - 进入仓库 Settings > Secrets and variables > Actions
   - 添加上述必需的Secrets

2. **测试工作流**：
   - 进入 Actions 页面
   - 手动触发 "Update Publication Metrics" 工作流
   - 检查日志确认数据是否正确获取

3. **验证结果**：
   - 检查 README.md 中的指标表格是否已更新
   - 确认所有指标都显示正确的数值

## 📚 详细文档

- 完整的配置指南请参考：`WOS_SETUP_GUIDE.md`
- 工作流配置：`.github/workflows/update-publication-metrics.yml`
- 更新脚本：`scripts/update_metrics.py`

