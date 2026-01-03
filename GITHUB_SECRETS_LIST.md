# GitHub Secrets 完整列表

本文档列出所有需要设置的GitHub Secrets，按必需和可选分类。

## ✅ 必需设置的 Secrets

### 1. Google Scholar 相关（二选一）

**方式A：自动获取（推荐）**
- `GOOGLE_SCHOLAR_ID`: 您的Google Scholar作者ID
  - 如何获取：从您的Google Scholar个人主页URL中提取
  - 示例：`https://scholar.google.com/citations?user=dsK8i4EAAAAJ` 中的 `dsK8i4EAAAAJ`

**方式B：手动设置（如果无法自动获取）**
- `TOTAL_PUBLICATIONS`: 总论文数
- `TOTAL_CITATIONS`: 总引用数
- `H_INDEX`: H-index

> **建议**：优先使用方式A（设置 `GOOGLE_SCHOLAR_ID`），系统会自动获取数据。

---

### 2. Web of Science 相关（必需手动设置）

以下6个指标**必须手动设置**（除非您有Web of Science API访问权限）：

- `INT_JOURNAL_COUNT`: 国际期刊论文数量
- `INT_CONF_COUNT`: 国际会议论文数量
- `BOOK_COUNT`: 图书/章节数量
- `SCI_PAPERS_COUNT`: SCI索引论文数量
- `JCR_Q1_COUNT`: JCR Q1期刊论文数量
- `IEEE_TRANS_COUNT`: IEEE Transactions论文数量

> **注意**：这些值需要您从Web of Science数据库中手动查询并统计。

---

## 🔧 可选设置的 Secrets

### 1. CNKI 相关（可选）

- `CN_JOURNAL_COUNT`: 中文期刊论文数量
- `CNKI_AUTHOR_ID`: CNKI作者ID（如果将来实现自动获取功能）

---

### 2. Web of Science API 相关（可选，需要付费订阅）

**仅当您有Web of Science API访问权限时设置**：

- `WOS_API_KEY`: Web of Science API密钥
  - 如何获取：参考 `GET_WOS_API_KEY.md`
  
- `WOS_RESEARCHER_ID`: Web of Science ResearcherID（**推荐，优先级最高**）
  - 如何获取：登录Web of Science，在您的个人资料页面查看

- `WOS_ORCID`: ORCID ID（如果未设置ResearcherID）
  - 如何获取：访问 https://orcid.org/ 注册或登录

- `WOS_AUTHOR_NAME`: 作者姓名（仅在前两者都未设置时使用）

> **注意**：如果没有API访问权限，只需手动设置上述6个Web of Science指标值即可，无需设置这些API相关Secrets。

---

## 📋 快速设置清单

### 最小配置（推荐）

**Google Scholar（自动获取）**：
- [ ] `GOOGLE_SCHOLAR_ID`

**Web of Science（手动设置）**：
- [ ] `INT_JOURNAL_COUNT`
- [ ] `INT_CONF_COUNT`
- [ ] `BOOK_COUNT`
- [ ] `SCI_PAPERS_COUNT`
- [ ] `JCR_Q1_COUNT`
- [ ] `IEEE_TRANS_COUNT`

**总计：7个Secrets**

---

### 完整配置（包含所有可选项）

**Google Scholar**：
- [ ] `GOOGLE_SCHOLAR_ID`

**Web of Science（手动设置）**：
- [ ] `INT_JOURNAL_COUNT`
- [ ] `INT_CONF_COUNT`
- [ ] `BOOK_COUNT`
- [ ] `SCI_PAPERS_COUNT`
- [ ] `JCR_Q1_COUNT`
- [ ] `IEEE_TRANS_COUNT`

**CNKI**：
- [ ] `CN_JOURNAL_COUNT`

**Web of Science API（如果有API访问权限）**：
- [ ] `WOS_API_KEY`
- [ ] `WOS_RESEARCHER_ID`
- [ ] `WOS_ORCID`（可选）
- [ ] `WOS_AUTHOR_NAME`（可选）

**总计：最多13个Secrets**

---

## 🔍 如何设置 GitHub Secrets

1. **进入GitHub仓库**
   - 打开您的GitHub仓库页面

2. **导航到Secrets设置**
   - 点击 **Settings**（设置）
   - 在左侧菜单中找到 **Secrets and variables** > **Actions**

3. **添加Secret**
   - 点击 **"New repository secret"** 按钮
   - 在 **Name** 字段输入Secret名称（例如：`GOOGLE_SCHOLAR_ID`）
   - 在 **Value** 字段输入Secret值（例如：`dsK8i4EAAAAJ`）
   - 点击 **"Add secret"** 按钮

4. **重复步骤3**，添加所有需要的Secrets

---

## 📊 Secrets 详细说明表

| Secret名称 | 类型 | 必需 | 说明 | 示例值 |
|-----------|------|------|------|--------|
| `GOOGLE_SCHOLAR_ID` | Google Scholar | 推荐 | Google Scholar作者ID | `dsK8i4EAAAAJ` |
| `TOTAL_PUBLICATIONS` | Google Scholar | 备选 | 总论文数（如果无法自动获取） | `200` |
| `TOTAL_CITATIONS` | Google Scholar | 备选 | 总引用数（如果无法自动获取） | `5000` |
| `H_INDEX` | Google Scholar | 备选 | H-index（如果无法自动获取） | `45` |
| `INT_JOURNAL_COUNT` | Web of Science | ✅ 必需 | 国际期刊论文数 | `150` |
| `INT_CONF_COUNT` | Web of Science | ✅ 必需 | 国际会议论文数 | `30` |
| `BOOK_COUNT` | Web of Science | ✅ 必需 | 图书/章节数 | `5` |
| `SCI_PAPERS_COUNT` | Web of Science | ✅ 必需 | SCI索引论文数 | `120` |
| `JCR_Q1_COUNT` | Web of Science | ✅ 必需 | JCR Q1期刊论文数 | `80` |
| `IEEE_TRANS_COUNT` | Web of Science | ✅ 必需 | IEEE Transactions论文数 | `45` |
| `CN_JOURNAL_COUNT` | CNKI | 可选 | 中文期刊论文数 | `20` |
| `WOS_API_KEY` | Web of Science API | 可选 | Web of Science API密钥 | `your-api-key` |
| `WOS_RESEARCHER_ID` | Web of Science API | 可选 | ResearcherID | `A-1234-5678` |
| `WOS_ORCID` | Web of Science API | 可选 | ORCID ID | `0000-0000-0000-0000` |
| `WOS_AUTHOR_NAME` | Web of Science API | 可选 | 作者姓名 | `Ning Wang` |

---

## ⚠️ 重要提示

1. **不需要Web of Science API密钥**：
   - 您可以直接手动设置6个Web of Science指标值
   - API密钥仅在有API访问权限且希望自动获取数据时使用

2. **Google Scholar ID优先**：
   - 如果设置了 `GOOGLE_SCHOLAR_ID`，系统会自动获取总论文数、引用数和H-index
   - 无需手动设置 `TOTAL_PUBLICATIONS`、`TOTAL_CITATIONS`、`H_INDEX`

3. **数据来源**：
   - 从Web of Science数据库手动查询并统计各项指标
   - 定期更新这些值以保持准确性

4. **安全提示**：
   - Secrets值在GitHub中会被隐藏，无法再次查看
   - 建议在本地保存一份备份
   - 如果忘记值，需要重新设置

---

## 🚀 下一步

设置完Secrets后：

1. **测试工作流**：
   - 进入仓库的 **Actions** 页面
   - 选择 **"Update Publication Metrics"** 工作流
   - 点击 **"Run workflow"** 按钮

2. **检查结果**：
   - 查看工作流日志，确认所有Secrets都被正确读取
   - 检查 README.md 中的指标表格是否已更新

3. **验证数据**：
   - 确认所有指标都显示正确的数值
   - 如果显示为0或"Loading..."，检查对应的Secret是否已正确设置

---

## 📚 相关文档

- **快速开始指南**：`QUICK_START_WOS.md`
- **Web of Science配置指南**：`WOS_SETUP_GUIDE.md`
- **获取API密钥指南**：`GET_WOS_API_KEY.md`
- **更改摘要**：`CHANGES_SUMMARY.md`

