# 🔧 故障排除指南

## 问题：Google Scholar 数据为空

如果您的指标表格中来自 Google Scholar 的数字显示为空、0 或 "N/A"，请按照以下步骤排查：

---

## 📋 排查步骤

### 步骤 1：检查 GitHub Secrets

1. **进入 GitHub 仓库设置**：
   - 访问您的仓库：`https://github.com/NingWangDMU/NingWangDMU`
   - 点击 **Settings** > **Secrets and variables** > **Actions**

2. **确认以下 Secrets 已设置**：
   - ✅ `GOOGLE_SCHOLAR_ID`: `dsK8i4EAAAAJ`
   - ✅ `CN_JOURNAL_COUNT`: 您的实际数值（例如：`51`）
   - ✅ `TOTAL_CITATIONS`: 您的总引用数（例如：`5000`）
   - ✅ `H_INDEX`: 您的 H-index（例如：`45`）
   - ✅ `INT_JOURNAL_COUNT`: 国际期刊论文数量（可选，但建议设置）
   - ✅ `INT_CONF_COUNT`: 国际会议论文数量（可选）
   - ✅ `BOOK_COUNT`: 书籍/章节数量（可选）

3. **如果 Secrets 未设置**：
   - 点击 **New repository secret**
   - 输入 Name 和 Value
   - 点击 **Add secret**

---

### 步骤 2：查看 GitHub Actions 日志

1. **进入 Actions 页面**：
   - 在仓库页面点击 **Actions** 标签
   - 找到最新的 **Update Publication Metrics** 运行记录

2. **查看日志**：
   - 点击运行记录
   - 展开 **Run update script** 步骤
   - 查看输出日志

3. **常见错误信息**：

   **错误 1：`Could not fetch Google Scholar metrics`**
   ```
   ⚠ Warning: Could not fetch Google Scholar metrics: ...
   ```
   **原因**：Google Scholar 反爬虫机制阻止了访问
   **解决方案**：这是正常的，脚本会自动回退到环境变量。确保您已设置 `TOTAL_CITATIONS` 和 `H_INDEX` 等 Secrets。

   **错误 2：`No config file or environment variables found`**
   ```
   ⚠ No config file or environment variables found
   ```
   **原因**：环境变量未设置
   **解决方案**：在 GitHub Secrets 中设置所有必要的指标值。

   **错误 3：`Pattern for INT_JOURNAL_COUNT not found`**
   ```
   ⚠ Warning: Pattern for INT_JOURNAL_COUNT not found in README.md
   ```
   **原因**：README.md 中的占位符格式不正确
   **解决方案**：检查 README.md 中的占位符格式是否正确。

---

### 步骤 3：验证环境变量传递

在 GitHub Actions 日志中，您应该看到类似以下输出：

```
🔍 Checking environment variables...
GOOGLE_SCHOLAR_ID: Set (hidden)
CN_JOURNAL_COUNT: Set (hidden)
TOTAL_CITATIONS: Set (hidden)
```

如果显示 "Not set"，说明对应的 Secret 未设置。

---

### 步骤 4：手动触发工作流

1. **进入 Actions 页面**
2. **选择 "Update Publication Metrics" 工作流**
3. **点击右侧 "Run workflow" 按钮**
4. **选择分支（通常是 `main`）**
5. **点击绿色 "Run workflow" 按钮**
6. **等待完成并查看结果**

---

## 🎯 推荐解决方案

### 方案 A：完全使用环境变量（最简单）

由于 Google Scholar 的反爬虫机制，**推荐直接使用环境变量**设置所有指标：

1. **在 GitHub Secrets 中设置所有指标**：
   - `TOTAL_CITATIONS`: 您的总引用数
   - `H_INDEX`: 您的 H-index
   - `INT_JOURNAL_COUNT`: 国际期刊论文数量
   - `INT_CONF_COUNT`: 国际会议论文数量
   - `BOOK_COUNT`: 书籍/章节数量
   - `CN_JOURNAL_COUNT`: 中文期刊论文数量

2. **可以保留 `GOOGLE_SCHOLAR_ID`**：
   - 脚本会尝试从 Google Scholar 获取数据
   - 如果失败，会自动回退到环境变量
   - 这样即使 Google Scholar 可用，也能正常工作

### 方案 B：仅使用环境变量（最可靠）

如果您不想依赖 Google Scholar API：

1. **删除或清空 `GOOGLE_SCHOLAR_ID` Secret**（可选）
2. **设置所有指标的环境变量**
3. **脚本会自动使用 `update_metrics_simple.py`**，直接从环境变量读取

---

## 🔍 验证指标是否正确更新

更新完成后，检查 `README.md` 文件：

1. **打开 README.md**
2. **找到 "Publication Metrics" 表格**
3. **确认指标显示实际数值**（不是 "Loading..." 或 "N/A"）
4. **确认 "Last Updated" 时间戳已更新**

---

## 📝 常见问题

### Q1: 为什么 Google Scholar 数据获取失败？

**A**: Google Scholar 有严格的反爬虫机制，在 GitHub Actions 环境中经常无法访问。这是正常现象，脚本会自动回退到环境变量。

### Q2: 我需要设置所有环境变量吗？

**A**: 不需要。至少设置以下关键指标：
- `TOTAL_CITATIONS`
- `H_INDEX`
- `CN_JOURNAL_COUNT`

其他指标（`INT_JOURNAL_COUNT`、`INT_CONF_COUNT`、`BOOK_COUNT`）是可选的。

### Q3: 如何手动更新指标？

**A**: 有两种方式：
1. **更新 GitHub Secrets**：修改 Secrets 值，然后手动触发工作流
2. **直接编辑 README.md**：在 GitHub 网页上直接编辑文件（不推荐，因为会被自动覆盖）

### Q4: 工作流运行成功，但指标仍然是 "Loading..."？

**A**: 可能的原因：
1. 脚本没有找到占位符（检查 README.md 格式）
2. 工作流没有正确提交更改（检查 "Commit changes" 步骤）
3. 需要刷新浏览器页面

---

## 🆘 仍然无法解决？

如果以上步骤都无法解决问题，请：

1. **查看完整的 GitHub Actions 日志**
2. **检查 README.md 中的占位符格式**是否正确
3. **确认仓库有写入权限**（Settings > Actions > General > Workflow permissions）

---

## 📚 相关文档

- 详细设置指南：`STEP_BY_STEP_GUIDE.md`
- 快速开始：`QUICK_START.md`
- 配置说明：`YOUR_CONFIGURATION.md`

