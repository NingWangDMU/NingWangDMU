# 🔧 解决指标显示为0的问题

## 问题描述

如果您的指标表格中以下指标显示为 **0**：
- 国际期刊论文数量 (INT_JOURNAL_COUNT)
- 国际会议论文数量 (INT_CONF_COUNT)
- 图书/章节数量 (BOOK_COUNT)

## 🔍 原因分析

### 原因1：Google Scholar自动分类失败（最常见）

Google Scholar的自动分类可能失败，因为：
1. **分类逻辑限制**：Google Scholar返回的venue字段格式不统一，可能不包含"journal"、"conference"等关键词
2. **API限制**：Google Scholar有反爬虫机制，可能无法获取完整的出版物详情
3. **数据格式变化**：Google Scholar的数据格式可能发生变化，导致分类失败

### 原因2：环境变量未设置

如果Google Scholar获取失败，脚本会回退到环境变量。如果这些环境变量未设置，指标就会保持为0。

### 原因3：出版物处理失败

在处理每个出版物时，如果出现错误（网络超时、数据格式问题等），该出版物会被跳过，导致计数为0。

---

## ✅ 解决方案

### 方案A：设置环境变量（推荐，最简单）

**这是最可靠的方法**，直接手动设置这些指标值：

1. **进入GitHub仓库设置**：
   - 访问 `https://github.com/NingWangDMU/NingWangDMU`
   - 点击 **Settings** > **Secrets and variables** > **Actions**

2. **创建以下Secrets**：

   **Secret 1: INT_JOURNAL_COUNT**
   - Name: `INT_JOURNAL_COUNT`
   - Value: 您的国际期刊论文数量（例如：`150`）

   **Secret 2: INT_CONF_COUNT**
   - Name: `INT_CONF_COUNT`
   - Value: 您的国际会议论文数量（例如：`30`）

   **Secret 3: BOOK_COUNT**
   - Name: `BOOK_COUNT`
   - Value: 您的图书/章节数量（例如：`5`）

3. **重新运行工作流**：
   - 进入 **Actions** 页面
   - 点击 **Update Publication Metrics** 工作流
   - 点击 **Run workflow**

4. **验证结果**：
   - 检查README.md，确认指标已更新为实际数值

---

### 方案B：改进自动分类（已更新）

我已经改进了分类逻辑，使其更智能：

1. **更全面的关键词匹配**：
   - 期刊：包含 "journal", "transaction", "ieee", "springer", "elsevier" 等
   - 会议：包含 "conference", "proceeding", "symposium", "workshop" 等
   - 书籍：包含 "book", "chapter", "monograph" 等

2. **多维度判断**：
   - 检查 `pub_type` 字段
   - 检查 `venue` 字段
   - 检查 `title` 字段
   - 根据venue格式推断（期刊通常名称较长，会议通常包含年份）

3. **更好的错误处理**：
   - 显示处理统计信息
   - 显示分类结果
   - 提供详细的日志输出

**注意**：即使改进了分类逻辑，Google Scholar的反爬虫机制仍可能导致获取失败。**建议同时设置环境变量作为备用**。

---

## 📋 如何获取准确的数值

### 方法1：从Google Scholar手动统计

1. **访问您的Google Scholar主页**：
   - `https://scholar.google.com/citations?user=dsK8i4EAAAAJ`

2. **手动统计**：
   - 浏览所有出版物
   - 分别统计期刊论文、会议论文、书籍/章节的数量
   - 记录这些数值

3. **设置到GitHub Secrets**：
   - 按照方案A的步骤设置这些值

### 方法2：从您的个人记录

如果您有个人记录（Excel表格、数据库等），可以直接使用这些数值。

### 方法3：使用改进后的自动分类

1. **查看GitHub Actions日志**：
   - 进入Actions页面
   - 点击最新的运行记录
   - 展开 "Run update script" 步骤
   - 查看分类结果日志

2. **如果分类结果合理**：
   - 可以依赖自动分类的结果
   - 但建议定期检查，因为Google Scholar可能变化

3. **如果分类结果不合理**：
   - 使用方案A手动设置正确的值

---

## 🔍 诊断步骤

### 步骤1：查看GitHub Actions日志

1. 进入 **Actions** 页面
2. 点击最新的 **Update Publication Metrics** 运行记录
3. 展开 **Run update script** 步骤
4. 查找以下信息：

   **如果看到**：
   ```
   ⚠ Warning: Could not fetch Google Scholar metrics: ...
   ```
   → Google Scholar获取失败，已回退到环境变量

   **如果看到**：
   ```
   ⚠ INT_JOURNAL_COUNT not found in environment, using: 0
   ```
   → 环境变量未设置，需要按照方案A设置

   **如果看到**：
   ```
   Processed X publications, skipped Y
   Classification results: Journals=0, Conferences=0, Books=0
   ```
   → 分类失败，可能是venue字段格式问题，建议使用方案A

### 步骤2：检查环境变量

1. 进入 **Settings** > **Secrets and variables** > **Actions**
2. 确认以下Secrets是否存在：
   - `INT_JOURNAL_COUNT`
   - `INT_CONF_COUNT`
   - `BOOK_COUNT`
3. 如果不存在，按照方案A创建它们

### 步骤3：验证更新

1. 检查README.md中的指标表格
2. 确认数值是否正确
3. 如果仍然是0，检查工作流是否成功运行

---

## 📊 推荐的Secrets配置

为了确保所有指标都能正确显示，建议设置以下Secrets：

### 必需Secrets（最低配置）
- ✅ `GOOGLE_SCHOLAR_ID`: `dsK8i4EAAAAJ`
- ✅ `CN_JOURNAL_COUNT`: `51`

### 强烈推荐Secrets
- ✅ `TOTAL_CITATIONS`: 您的总引用数
- ✅ `H_INDEX`: 您的H-index
- ✅ `INT_JOURNAL_COUNT`: 国际期刊论文数量
- ✅ `INT_CONF_COUNT`: 国际会议论文数量
- ✅ `BOOK_COUNT`: 图书/章节数量

---

## 🎯 快速修复步骤

如果您想立即修复这个问题：

1. **获取您的实际数值**：
   - 从Google Scholar或其他来源获取准确的数值

2. **设置GitHub Secrets**（5分钟）：
   - `INT_JOURNAL_COUNT`: [您的数值]
   - `INT_CONF_COUNT`: [您的数值]
   - `BOOK_COUNT`: [您的数值]

3. **运行工作流**（1分钟）：
   - Actions > Update Publication Metrics > Run workflow

4. **验证结果**：
   - 检查README.md，确认指标已更新

---

## 📝 注意事项

1. **Google Scholar限制**：
   - Google Scholar有严格的反爬虫机制
   - 自动获取可能经常失败
   - **建议始终设置环境变量作为备用**

2. **分类准确性**：
   - 自动分类可能不够准确
   - 手动设置的值更可靠
   - 建议定期检查和更新

3. **数据来源**：
   - 可以从Google Scholar、个人记录、其他数据库获取
   - 确保数值准确可靠

---

## 🆘 仍然无法解决？

如果按照以上步骤操作后，问题仍然存在：

1. **查看完整日志**：
   - 在GitHub Actions中查看详细的错误信息

2. **检查工作流权限**：
   - Settings > Actions > General > Workflow permissions
   - 确保设置为 "Read and write permissions"

3. **参考其他文档**：
   - `TROUBLESHOOTING.md` - 详细故障排除指南
   - `COMPLETE_SETUP_GUIDE.md` - 完整设置指南

---

## ✅ 完成检查清单

修复完成后，确认：

- [ ] `INT_JOURNAL_COUNT` Secret已设置
- [ ] `INT_CONF_COUNT` Secret已设置
- [ ] `BOOK_COUNT` Secret已设置
- [ ] 工作流已成功运行
- [ ] README.md中的指标显示实际数值（不是0）

如果所有项目都已勾选，问题已解决！🎉

