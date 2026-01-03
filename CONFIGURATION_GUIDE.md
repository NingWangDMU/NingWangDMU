# 出版物指标配置指南

本指南将帮助您完成出版物指标自动更新系统的配置。

## 📋 配置方式选择

您有两种配置方式：

### 方式A：手动设置指标（推荐，最简单）⭐
- ✅ **优点**：简单快速，无需任何ID，立即可用
- ✅ **适用**：您知道自己的指标数值，希望手动维护
- ⏱️ **设置时间**：5分钟

### 方式B：自动从Google Scholar获取（需要ID）
- ✅ **优点**：自动更新，数据准确
- ⚠️ **缺点**：需要Google Scholar ID，可能受反爬虫限制
- ⏱️ **设置时间**：10分钟

---

## 🚀 快速配置（方式A：手动设置）

### 步骤1：获取您的指标数据

请准备以下数据（可以从您的Google Scholar、CNKI或其他来源获取）：

| 指标 | 说明 | 示例值 |
|------|------|--------|
| `INT_JOURNAL_COUNT` | 国际期刊论文数量 | 150 |
| `CN_JOURNAL_COUNT` | 中文期刊论文数量 | 20 |
| `INT_CONF_COUNT` | 国际会议论文数量 | 30 |
| `BOOK_COUNT` | 书籍/章节数量 | 5 |
| `TOTAL_CITATIONS` | 总引用数 | 5000 |
| `H_INDEX` | H-index | 45 |

### 步骤2：在GitHub仓库中设置Secrets

1. 访问您的GitHub仓库
2. 点击 **Settings**（设置）
3. 在左侧菜单选择 **Secrets and variables** > **Actions**
4. 点击 **New repository secret**（新建仓库密钥）
5. 为每个指标创建Secret：

   ```
   Name: INT_JOURNAL_COUNT
   Value: 150（您的实际数值）
   ```

   重复此步骤，创建以下所有Secrets：
   - `INT_JOURNAL_COUNT`
   - `CN_JOURNAL_COUNT`
   - `INT_CONF_COUNT`
   - `BOOK_COUNT`
   - `TOTAL_CITATIONS`
   - `H_INDEX`

### 步骤3：测试配置

1. 进入仓库的 **Actions** 页面
2. 选择 **Update Publication Metrics** 工作流
3. 点击 **Run workflow**（运行工作流）
4. 等待工作流完成
5. 检查 README.md 中的指标表格是否已更新

✅ **完成！** 系统现在会每天自动更新您的指标。

---

## 🔍 自动配置（方式B：Google Scholar自动获取）

### 步骤1：获取Google Scholar ID

1. 访问您的Google Scholar个人主页
   - 网址格式：`https://scholar.google.com/citations?user=YOUR_ID`
2. 从URL中提取ID
   - 例如：如果URL是 `https://scholar.google.com/citations?user=abc123xyz`
   - 那么您的ID就是：`abc123xyz`

### 步骤2：在GitHub仓库中设置Secret

1. 访问您的GitHub仓库
2. 点击 **Settings** > **Secrets and variables** > **Actions**
3. 点击 **New repository secret**
4. 创建Secret：
   ```
   Name: GOOGLE_SCHOLAR_ID
   Value: abc123xyz（您的实际ID）
   ```

### 步骤3：设置回退值（可选但推荐）

即使设置了Google Scholar ID，也建议设置手动指标作为回退：

按照"方式A"的步骤2，设置所有指标的环境变量。这样，如果Google Scholar获取失败，系统会自动使用这些值。

### 步骤4：测试配置

1. 进入 **Actions** 页面
2. 运行 **Update Publication Metrics** 工作流
3. 检查日志，确认是否成功从Google Scholar获取数据

---

## 📝 配置检查清单

使用此清单确保配置完整：

### 必需配置（至少选择一种方式）

- [ ] **方式A**：已设置所有6个指标Secrets
  - [ ] `INT_JOURNAL_COUNT`
  - [ ] `CN_JOURNAL_COUNT`
  - [ ] `INT_CONF_COUNT`
  - [ ] `BOOK_COUNT`
  - [ ] `TOTAL_CITATIONS`
  - [ ] `H_INDEX`

- [ ] **方式B**：已设置Google Scholar ID
  - [ ] `GOOGLE_SCHOLAR_ID`

### 可选配置

- [ ] CNKI配置（如果需要自动获取中文期刊论文）
  - [ ] `CNKI_AUTHOR_ID`
  - [ ] `CNKI_API_KEY`

### 验证步骤

- [ ] 已运行GitHub Actions工作流
- [ ] 工作流成功完成（无错误）
- [ ] README.md中的指标表格已更新
- [ ] 指标数值正确

---

## 🆘 需要帮助？

### 如果您需要我帮您配置：

请提供以下信息（您可以选择提供哪些）：

1. **Google Scholar ID**（如果使用自动获取）
   - 您的Google Scholar个人主页URL
   - 或直接提供ID

2. **指标数值**（如果使用手动设置）
   - 国际期刊论文数量
   - 中文期刊论文数量
   - 国际会议论文数量
   - 书籍/章节数量
   - 总引用数
   - H-index

3. **CNKI信息**（可选，如果需要）
   - CNKI作者ID
   - CNKI API密钥

### 我可以帮您：

- ✅ 创建配置文件
- ✅ 生成配置命令
- ✅ 验证配置是否正确
- ✅ 测试配置

---

## 📊 当前配置状态

要检查当前配置状态，可以：

1. 查看GitHub Actions日志
2. 检查README.md中的指标是否显示"Loading..."（表示未配置）
3. 运行本地测试脚本

---

## 🔄 更新指标

### 手动更新指标值

只需更新GitHub Secrets中的值，然后运行工作流即可。

### 自动更新

如果使用Google Scholar自动获取，系统会每天自动更新。您也可以随时手动触发工作流。

---

## 💡 推荐配置方案

**最佳实践**：结合使用两种方式

1. 设置Google Scholar ID用于自动获取
2. 同时设置所有指标的手动值作为回退
3. 这样即使自动获取失败，也能显示正确的指标

---

## 📞 下一步

- 如果您想使用**方式A（手动设置）**，请提供您的指标数值
- 如果您想使用**方式B（自动获取）**，请提供您的Google Scholar ID
- 如果您不确定，我建议先使用**方式A**，因为它最简单可靠

