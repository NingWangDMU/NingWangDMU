# Web of Science 指标配置指南

本文档说明如何配置Web of Science相关指标，以及如何设置GitHub Secrets。

## 📊 指标说明

### 从Google Scholar获取的指标
- **Total Publications** (总论文数): 从Google Scholar自动获取所有论文总数
- **Total Citations** (总引用数): 从Google Scholar自动获取
- **H-index**: 从Google Scholar自动获取

### 从Web of Science获取的指标
- **International Journal Papers** (国际期刊论文数)
- **International Conference Papers** (国际会议论文数)
- **Books/Chapters** (图书/章节数)
- **SCI-indexed Papers** (SCI索引论文数)
- **JCR Q1 Papers** (JCR Q1期刊论文数)
- **IEEE Transactions** (IEEE Transactions论文数)

### 从CNKI获取的指标
- **Chinese Journal Papers** (中文期刊论文数)

## 🔧 配置方法

### ⚠️ 重要说明

**您不需要Web of Science API密钥！**

系统设计为：
- **有API密钥**：尝试自动从Web of Science API获取数据
- **无API密钥或API调用失败**：自动使用环境变量中的手动设置值

**推荐方式**：直接使用方法2（手动设置环境变量），无需API密钥。

---

### 方法1: 使用Web of Science API（可选，需要付费订阅）

**注意**：此方法需要Web of Science API访问权限，通常需要付费订阅。如果没有API访问权限，请直接使用方法2。

如果您有Web of Science API访问权限：

1. **获取API密钥**：
   - 访问 [Clarivate Developer Portal](https://developer.clarivate.com/)
   - 注册开发者账号并申请Web of Science API访问权限
   - 等待审批通过后获取API密钥
   - **详细步骤请参考**: `GET_WOS_API_KEY.md`

2. **在GitHub Secrets中设置**：
   - 进入仓库 Settings > Secrets and variables > Actions
   - 添加以下Secrets：
     - `WOS_API_KEY`: Web of Science API密钥
     - `WOS_RESEARCHER_ID`: 您的Web of Science ResearcherID（**推荐，优先级最高**）
     - `WOS_ORCID`: 您的ORCID ID（可选，如果未设置ResearcherID）
     - `WOS_AUTHOR_NAME`: 您的姓名（可选，仅在前两者都未设置时使用）

3. **作者标识优先级**：
   - 系统会按以下优先级使用作者标识：
     1. **ResearcherID**（最推荐，最准确）
     2. ORCID ID
     3. 作者姓名

4. **注意**：
   - Web of Science API通常需要付费订阅
   - 如果API调用失败，系统会自动回退到环境变量方法
   - ResearcherID是Web of Science特有的标识符，通常比ORCID或姓名更准确

### 方法2: 手动设置环境变量（推荐，无需API密钥）⭐

**这是最简单且推荐的方法，不需要任何API密钥！**

只需在GitHub Secrets中手动设置指标值：

1. **在GitHub Secrets中设置以下值**（必需）：
   - `INT_JOURNAL_COUNT`: 国际期刊论文数量
   - `INT_CONF_COUNT`: 国际会议论文数量
   - `BOOK_COUNT`: 图书/章节数量
   - `SCI_PAPERS_COUNT`: SCI索引论文数量
   - `JCR_Q1_COUNT`: JCR Q1期刊论文数量
   - `IEEE_TRANS_COUNT`: IEEE Transactions论文数量

2. **Google Scholar相关（如果无法自动获取）**：
   - `GOOGLE_SCHOLAR_ID`: 您的Google Scholar作者ID（例如：`dsK8i4EAAAAJ`）
   - `TOTAL_PUBLICATIONS`: 总论文数（如果Google Scholar无法获取）
   - `TOTAL_CITATIONS`: 总引用数（如果Google Scholar无法获取）
   - `H_INDEX`: H-index（如果Google Scholar无法获取）

3. **CNKI相关**：
   - `CN_JOURNAL_COUNT`: 中文期刊论文数量

## 📝 完整GitHub Secrets列表

### 必需配置（至少设置以下之一）

**Google Scholar自动获取（推荐）**：
- `GOOGLE_SCHOLAR_ID`: 您的Google Scholar作者ID

**或手动设置Google Scholar指标**：
- `TOTAL_PUBLICATIONS`: 总论文数
- `TOTAL_CITATIONS`: 总引用数
- `H_INDEX`: H-index

**Web of Science指标（必需手动设置，除非有API访问权限）**：
- `INT_JOURNAL_COUNT`: 国际期刊论文数
- `INT_CONF_COUNT`: 国际会议论文数
- `BOOK_COUNT`: 图书/章节数
- `SCI_PAPERS_COUNT`: SCI索引论文数
- `JCR_Q1_COUNT`: JCR Q1期刊论文数
- `IEEE_TRANS_COUNT`: IEEE Transactions论文数

**CNKI指标（可选）**：
- `CN_JOURNAL_COUNT`: 中文期刊论文数

### 可选配置（用于Web of Science API）

- `WOS_API_KEY`: Web of Science API密钥
- `WOS_RESEARCHER_ID`: Web of Science ResearcherID（**推荐，优先级最高**）
- `WOS_ORCID`: ORCID ID（如果未设置ResearcherID）
- `WOS_AUTHOR_NAME`: 作者姓名（仅在前两者都未设置时使用）

## 🔄 更新频率

工作流已配置为**每周一北京时间凌晨0点**自动运行（UTC时间周日16点）。

您也可以手动触发：
1. 进入GitHub仓库的 Actions 页面
2. 选择 "Update Publication Metrics" 工作流
3. 点击 "Run workflow"

## ⚠️ 注意事项

1. **Web of Science API访问**：
   - Web of Science API通常需要机构订阅
   - 如果没有API访问权限，请使用环境变量方法手动设置指标值

2. **数据准确性**：
   - 手动设置的指标值需要定期更新以保持准确性
   - 建议每月检查一次指标值

3. **Google Scholar限制**：
   - Google Scholar有反爬虫机制，频繁请求可能被限制
   - 如果自动获取失败，请使用环境变量回退

## 🐛 故障排除

### 问题：指标显示为0或"Loading..."

**解决方案**：
1. 检查GitHub Secrets是否已正确设置
2. 查看GitHub Actions日志，确认环境变量是否正确传递
3. 如果使用Google Scholar自动获取，检查`GOOGLE_SCHOLAR_ID`是否正确

### 问题：Web of Science API调用失败

**解决方案**：
1. 检查API密钥是否正确
2. 确认API访问权限是否有效
3. 系统会自动回退到环境变量方法，请确保已设置相应的Secrets

### 问题：更新时间不正确

**解决方案**：
- 工作流已配置为每周一北京时间凌晨0点运行
- 如需修改，请编辑`.github/workflows/update-publication-metrics.yml`中的cron表达式

## 📚 相关文档

- [GitHub Actions文档](https://docs.github.com/en/actions)
- [Web of Science API文档](https://developer.clarivate.com/apis/wos)
- [Google Scholar API文档](https://scholar.google.com/intl/en/scholar/api.html)

