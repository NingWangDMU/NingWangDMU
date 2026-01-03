# Web of Science 指标快速开始指南

## ⚠️ 重要提示

**您不需要Web of Science API密钥！**

系统会自动使用您在GitHub Secrets中手动设置的指标值。

## 🚀 快速设置步骤

### 1. 准备您的指标数据

从Web of Science数据库中查询并记录以下数据：
- 国际期刊论文数量
- 国际会议论文数量
- 图书/章节数量
- SCI索引论文数量
- JCR Q1期刊论文数量
- IEEE Transactions论文数量

### 2. 设置GitHub Secrets

1. 进入您的GitHub仓库
2. 点击 **Settings** > **Secrets and variables** > **Actions**
3. 点击 **New repository secret**
4. 添加以下Secrets（每个指标一个Secret）：

| Secret名称 | 说明 | 示例值 |
|-----------|------|--------|
| `INT_JOURNAL_COUNT` | 国际期刊论文数 | `150` |
| `INT_CONF_COUNT` | 国际会议论文数 | `30` |
| `BOOK_COUNT` | 图书/章节数 | `5` |
| `SCI_PAPERS_COUNT` | SCI索引论文数 | `120` |
| `JCR_Q1_COUNT` | JCR Q1期刊论文数 | `80` |
| `IEEE_TRANS_COUNT` | IEEE Transactions论文数 | `45` |

### 3. 设置Google Scholar（可选但推荐）

如果您想自动获取总论文数、引用数和H-index：

| Secret名称 | 说明 | 如何获取 |
|-----------|------|---------|
| `GOOGLE_SCHOLAR_ID` | Google Scholar作者ID | 从您的Google Scholar个人主页URL中获取，例如：`https://scholar.google.com/citations?user=YOUR_ID` 中的 `YOUR_ID` |

### 4. 测试工作流

1. 进入仓库的 **Actions** 页面
2. 选择 **Update Publication Metrics** 工作流
3. 点击 **Run workflow** 按钮
4. 等待工作流完成
5. 检查 README.md 中的指标表格是否已更新

## ✅ 完成！

现在您的指标会自动每周一更新一次（北京时间凌晨0点）。

如果需要手动更新，只需在Actions页面再次运行工作流即可。

## 🔄 更新指标值

当您的论文数量发生变化时：

1. 在Web of Science中查询最新数据
2. 更新相应的GitHub Secrets值
3. 手动触发工作流或等待自动更新

## ❓ 常见问题

**Q: 我需要Web of Science API密钥吗？**  
A: 不需要！只需手动设置指标值即可。

**Q: 如何获取这些指标数据？**  
A: 登录Web of Science数据库，使用作者检索功能查询您的论文，然后统计各类论文数量。

**Q: 数据多久更新一次？**  
A: 系统每周一北京时间凌晨0点自动更新。您也可以随时手动触发更新。

**Q: 如果我没有设置某些指标会怎样？**  
A: 未设置的指标会显示为0或"Loading..."。建议设置所有指标以获得完整的数据展示。

