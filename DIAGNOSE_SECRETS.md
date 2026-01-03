# 🔍 诊断Secrets问题 - 详细指南

## 📋 问题确认

您已经设置了所有必需的Secrets：
- ✅ `INT_JOURNAL_COUNT`
- ✅ `INT_CONF_COUNT`
- ✅ `BOOK_COUNT`
- ✅ `GOOGLE_SCHOLAR_ID`
- ✅ `CN_JOURNAL_COUNT`
- ✅ `TOTAL_CITATIONS`
- ✅ `H_INDEX`

但指标仍然显示为0。这说明问题不在于Secrets未设置，而可能是：

1. **Secrets的值可能设置为0或空字符串**
2. **工作流可能没有正确传递环境变量**
3. **脚本逻辑可能有问题**

---

## 🔍 诊断步骤

### 步骤1：检查Secrets的值

1. **进入GitHub仓库设置**：
   - 访问 `https://github.com/NingWangDMU/NingWangDMU`
   - 点击 **Settings** > **Secrets and variables** > **Actions**

2. **检查每个Secret的值**：
   - 点击每个Secret名称右侧的 **✏️（编辑）** 图标
   - **重要**：检查Value字段中的值
   - 确认以下Secrets的值**不是0或空字符串**：
     - `INT_JOURNAL_COUNT`: 应该是您的实际期刊论文数量（例如：`150`）
     - `INT_CONF_COUNT`: 应该是您的实际会议论文数量（例如：`30`）
     - `BOOK_COUNT`: 应该是您的实际图书/章节数量（例如：`5`）

3. **如果值为0或空**：
   - 修改为正确的数值
   - 点击 **Update secret** 保存

---

### 步骤2：查看GitHub Actions日志

1. **进入Actions页面**：
   - 在GitHub仓库页面，点击 **Actions** 标签

2. **查看最新运行记录**：
   - 点击最新的 **"Update Publication Metrics"** 运行记录
   - 展开 **"Run update script"** 步骤

3. **查找关键信息**：

   **查找环境变量检查**：
   ```
   🔍 Checking environment variables...
   GOOGLE_SCHOLAR_ID: Set (hidden)
   CN_JOURNAL_COUNT: Set (hidden)
   TOTAL_CITATIONS: Set (hidden)
   ```

   **查找环境变量加载**：
   ```
   🔍 Checking environment variables for counts...
     ✓ Using INT_JOURNAL_COUNT from environment: 150
     ✓ Using INT_CONF_COUNT from environment: 30
     ✓ Using BOOK_COUNT from environment: 5
   ```

   **如果看到**：
   ```
     ⚠ INT_JOURNAL_COUNT not found in environment, using classification result
   ```
   → 说明环境变量没有被正确传递

   **如果看到**：
   ```
     ⚠ INT_JOURNAL_COUNT in environment is 0, using classification result
   ```
   → 说明环境变量的值是0，需要修改

---

### 步骤3：验证工作流配置

1. **检查工作流文件**：
   - 在GitHub仓库中，打开 `.github/workflows/update-publication-metrics.yml`
   - 确认 `env` 部分包含所有Secrets：
     ```yaml
     env:
       GOOGLE_SCHOLAR_ID: ${{ secrets.GOOGLE_SCHOLAR_ID }}
       INT_JOURNAL_COUNT: ${{ secrets.INT_JOURNAL_COUNT }}
       INT_CONF_COUNT: ${{ secrets.INT_CONF_COUNT }}
       BOOK_COUNT: ${{ secrets.BOOK_COUNT }}
       ...
     ```

2. **如果缺少某个Secret**：
   - 编辑工作流文件，添加缺失的Secret
   - 提交更改

---

## ✅ 解决方案

### 方案1：确保Secrets的值正确（最重要）

1. **检查并修改Secrets的值**：
   - 进入 Settings > Secrets and variables > Actions
   - 点击每个Secret的编辑图标
   - 确认值不是0或空字符串
   - 如果为0，修改为正确的数值

2. **示例正确的值**：
   - `INT_JOURNAL_COUNT`: `150`（不是`0`或空）
   - `INT_CONF_COUNT`: `30`（不是`0`或空）
   - `BOOK_COUNT`: `5`（不是`0`或空）

### 方案2：重新运行工作流

1. **进入Actions页面**
2. **运行工作流**：
   - 点击 "Update Publication Metrics" 工作流
   - 点击 "Run workflow"
   - 等待完成

3. **查看日志**：
   - 确认看到 "✓ Using INT_JOURNAL_COUNT from environment: [您的数值]"
   - 如果看到 "not found" 或 "is 0"，说明Secrets的值有问题

### 方案3：提交更新的代码

我已经改进了脚本，使其：
- **优先使用环境变量**（如果存在且大于0）
- **提供详细的诊断信息**
- **明确显示使用了哪个值**

1. **提交更新的代码**：
   - 在GitHub Desktop中提交 `scripts/update_metrics.py`
   - 推送到GitHub

2. **重新运行工作流**：
   - 运行工作流，查看新的日志输出

---

## 🔧 快速修复步骤

### 如果Secrets的值是0：

1. **修改Secrets的值**（5分钟）：
   - 进入 Settings > Secrets and variables > Actions
   - 点击 `INT_JOURNAL_COUNT` 的编辑图标
   - 将Value改为您的实际数值（例如：`150`）
   - 点击 Update secret
   - 重复此步骤，修改 `INT_CONF_COUNT` 和 `BOOK_COUNT`

2. **重新运行工作流**（1分钟）：
   - Actions > Update Publication Metrics > Run workflow

3. **验证结果**：
   - 检查README.md，确认指标已更新

---

## 📊 检查清单

完成诊断后，确认：

- [ ] 所有Secrets的值都不是0或空字符串
- [ ] `INT_JOURNAL_COUNT` 的值是您的实际期刊论文数量
- [ ] `INT_CONF_COUNT` 的值是您的实际会议论文数量
- [ ] `BOOK_COUNT` 的值是您的实际图书/章节数量
- [ ] 工作流已重新运行
- [ ] 日志中显示 "✓ Using ... from environment"
- [ ] README.md中的指标显示实际数值（不是0）

---

## 🆘 仍然无法解决？

如果按照以上步骤操作后，问题仍然存在：

1. **查看完整日志**：
   - 在GitHub Actions中查看详细的日志输出
   - 特别关注环境变量检查部分

2. **检查工作流权限**：
   - Settings > Actions > General > Workflow permissions
   - 确保设置为 "Read and write permissions"

3. **尝试强制使用环境变量**：
   - 添加一个新的Secret：
     - Name: `USE_ENV_FOR_COUNTS`
     - Value: `true`
   - 这会强制脚本使用环境变量，忽略分类结果

4. **联系支持**：
   - 提供GitHub Actions的完整日志
   - 说明您已经检查了Secrets的值

---

## 💡 最佳实践

1. **定期检查Secrets的值**：
   - 确保值不是0或空字符串
   - 当您发表新论文时，记得更新数值

2. **使用有意义的数值**：
   - 不要设置为0（除非确实没有）
   - 确保数值准确可靠

3. **监控日志输出**：
   - 定期查看GitHub Actions日志
   - 确认环境变量被正确使用

