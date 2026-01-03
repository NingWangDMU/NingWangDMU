# 🔧 解决分类失败问题 - 详细操作指南

## 📋 问题确认

如果您的指标表格中以下指标显示为 **0**：
- ✅ 国际期刊论文数量 (INT_JOURNAL_COUNT)
- ✅ 国际会议论文数量 (INT_CONF_COUNT)
- ✅ 图书/章节数量 (BOOK_COUNT)

而 **Total Citations** 和 **H-index** 有正常数值，说明Google Scholar数据获取成功，但分类逻辑失败。

---

## 🎯 解决方案（两种方法）

### 方案A：设置环境变量（推荐，最可靠）⭐

**这是最可靠的方法**，直接手动设置这些指标值，不依赖自动分类。

#### 步骤1：获取您的实际数值

**方法1：从Google Scholar手动统计**

1. **访问您的Google Scholar主页**：
   ```
   https://scholar.google.com/citations?user=dsK8i4EAAAAJ
   ```

2. **手动统计**：
   - 浏览所有出版物列表
   - 分别统计：
     - **国际期刊论文**：发表在期刊上的论文
     - **国际会议论文**：发表在会议上的论文
     - **图书/章节**：书籍、书籍章节、专著等
   - 记录这些数值

**方法2：从您的个人记录**

如果您有Excel表格、数据库或其他记录，可以直接使用这些数值。

#### 步骤2：在GitHub上设置Secrets

1. **进入GitHub仓库设置**：
   - 在浏览器中访问：`https://github.com/NingWangDMU/NingWangDMU`
   - 点击顶部 **Settings** 标签

2. **进入Secrets设置**：
   - 在左侧菜单中，点击 **Secrets and variables** > **Actions**
   - 您会看到 "Repository secrets" 部分

3. **创建Secret 1: INT_JOURNAL_COUNT**
   - 点击 **New repository secret** 按钮
   - **Name**: `INT_JOURNAL_COUNT`
   - **Secret**: 输入您的国际期刊论文数量（例如：`150`）
   - 点击 **Add secret**

4. **创建Secret 2: INT_CONF_COUNT**
   - 再次点击 **New repository secret** 按钮
   - **Name**: `INT_CONF_COUNT`
   - **Secret**: 输入您的国际会议论文数量（例如：`30`）
   - 点击 **Add secret**

5. **创建Secret 3: BOOK_COUNT**
   - 再次点击 **New repository secret** 按钮
   - **Name**: `BOOK_COUNT`
   - **Secret**: 输入您的图书/章节数量（例如：`5`）
   - 点击 **Add secret**

6. **验证Secrets已创建**：
   - 在 "Repository secrets" 列表中，您应该看到：
     - ✅ `INT_JOURNAL_COUNT` (值被隐藏显示为 `••••••`)
     - ✅ `INT_CONF_COUNT` (值被隐藏显示为 `••••••`)
     - ✅ `BOOK_COUNT` (值被隐藏显示为 `••••••`)

#### 步骤3：重新运行工作流

1. **进入Actions页面**：
   - 在GitHub仓库页面，点击顶部 **Actions** 标签

2. **运行工作流**：
   - 在左侧找到 **"Update Publication Metrics"** 工作流
   - 点击它
   - 点击右侧 **"Run workflow"** 下拉按钮
   - 确认分支是 `main`
   - 点击绿色 **"Run workflow"** 按钮

3. **等待完成**：
   - 工作流通常需要1-3分钟
   - 等待显示为绿色（成功）

#### 步骤4：验证结果

1. **检查README.md**：
   - 在GitHub仓库页面，打开 `README.md` 文件
   - 滚动到 **"Publication Metrics"** 部分
   - 确认以下指标显示实际数值（不是0）：
     - ✅ International Journal Papers: 显示您设置的值
     - ✅ International Conference Papers: 显示您设置的值
     - ✅ Books/Chapters: 显示您设置的值

2. **如果仍然显示0**：
   - 检查工作流是否成功运行（绿色）
   - 查看Actions日志，确认环境变量是否正确加载
   - 参考下面的"故障排除"部分

---

### 方案B：使用改进后的自动分类（已更新代码）

我已经改进了分类逻辑，使其更智能。但**仍然建议设置环境变量作为备用**。

#### 改进内容

1. **更全面的关键词匹配**：
   - 期刊：包含 "journal", "transaction", "ieee", "springer", "elsevier", "ocean engineering" 等
   - 会议：包含 "conference", "proceeding", "symposium", "workshop" 等
   - 书籍：包含 "book", "chapter", "monograph" 等

2. **多策略分类**：
   - 策略1：检查 `pub_type` 字段
   - 策略2：检查 `venue` 字段（使用扩展的关键词列表）
   - 策略3：启发式判断（根据venue长度、格式、是否包含年份等）
   - 策略4：检查标题

3. **智能回退**：
   - 如果分类结果全部为0，自动回退到环境变量
   - 显示详细的调试信息（venue示例）
   - 提供清晰的错误提示

4. **详细日志**：
   - 显示处理统计信息
   - 显示分类结果
   - 显示venue示例（用于调试）

#### 使用改进后的分类

1. **提交更新的代码**（如果还未提交）：
   - 按照下面的"提交代码"部分操作

2. **运行工作流**：
   - 进入Actions页面
   - 运行 "Update Publication Metrics" 工作流

3. **查看日志**：
   - 展开 "Run update script" 步骤
   - 查看分类结果和venue示例
   - 如果分类仍然失败，会看到警告信息

4. **如果分类失败**：
   - 使用方案A设置环境变量

---

## 📝 提交更新的代码

如果您想使用改进后的分类逻辑，需要先提交更新的代码：

### 在GitHub Desktop中：

1. **打开GitHub Desktop**

2. **检查更改**：
   - 左侧面板应该显示 `scripts/update_metrics.py` 已修改

3. **输入提交信息**：
   ```
   改进Google Scholar分类逻辑，修复分类失败问题
   
   - 添加多策略分类算法
   - 改进关键词匹配
   - 添加智能回退机制
   - 添加详细调试信息
   ```

4. **提交并推送**：
   - 点击 **Commit to main**
   - 点击 **Push origin**

5. **验证**：
   - 在GitHub网页上确认文件已更新

---

## 🔍 诊断和调试

### 查看GitHub Actions日志

1. **进入Actions页面**：
   - 点击仓库顶部的 **Actions** 标签

2. **查看最新运行记录**：
   - 点击最新的 **"Update Publication Metrics"** 运行记录
   - 展开 **"Run update script"** 步骤

3. **查找关键信息**：

   **如果看到**：
   ```
   Processed X publications, skipped Y, unclassified Z
   Classification results: Journals=0, Conferences=0, Books=0
   ⚠ Warning: All classifications are 0, but X publications were processed
   ```
   → 分类失败，已自动回退到环境变量

   **如果看到**：
   ```
   Sample venues (first 10):
     [1] venue='ieee transactions on...' pub_type='article'
   ```
   → 显示venue示例，可以用于调试分类逻辑

   **如果看到**：
   ```
   ⚠ INT_JOURNAL_COUNT not found in environment, using: 0
   ```
   → 环境变量未设置，需要按照方案A设置

### 检查环境变量

1. **进入Settings**：
   - Settings > Secrets and variables > Actions

2. **确认Secrets存在**：
   - `INT_JOURNAL_COUNT`
   - `INT_CONF_COUNT`
   - `BOOK_COUNT`

3. **如果不存在**：
   - 按照方案A的步骤创建它们

---

## ⚙️ 高级选项：强制使用环境变量

如果您想**完全禁用自动分类**，只使用环境变量：

1. **在GitHub Secrets中添加**：
   - Name: `USE_ENV_FOR_COUNTS`
   - Value: `true`

2. **这样设置后**：
   - 即使Google Scholar分类成功，也会优先使用环境变量的值
   - 总引用数和H-index仍然从Google Scholar获取

---

## 📊 推荐的完整Secrets配置

为了确保所有指标都能正确显示，建议设置以下Secrets：

### 必需Secrets（最低配置）
- ✅ `GOOGLE_SCHOLAR_ID`: `dsK8i4EAAAAJ`
- ✅ `CN_JOURNAL_COUNT`: `51`（或您的实际数值）

### 强烈推荐Secrets（解决分类失败问题）
- ✅ `INT_JOURNAL_COUNT`: 国际期刊论文数量
- ✅ `INT_CONF_COUNT`: 国际会议论文数量
- ✅ `BOOK_COUNT`: 图书/章节数量

### 可选但推荐Secrets
- ✅ `TOTAL_CITATIONS`: 总引用数（如果Google Scholar获取失败时的备用）
- ✅ `H_INDEX`: H-index（如果Google Scholar获取失败时的备用）

---

## ✅ 完成检查清单

修复完成后，确认：

- [ ] `INT_JOURNAL_COUNT` Secret已设置
- [ ] `INT_CONF_COUNT` Secret已设置
- [ ] `BOOK_COUNT` Secret已设置
- [ ] 工作流已成功运行（绿色）
- [ ] README.md中的指标显示实际数值（不是0）
- [ ] "Last Updated"时间戳已更新

如果所有项目都已勾选，问题已解决！🎉

---

## 🆘 仍然无法解决？

如果按照以上步骤操作后，问题仍然存在：

1. **查看完整日志**：
   - 在GitHub Actions中查看详细的错误信息
   - 特别关注venue示例和分类结果

2. **检查工作流权限**：
   - Settings > Actions > General > Workflow permissions
   - 确保设置为 "Read and write permissions"

3. **参考其他文档**：
   - `FIX_ZERO_METRICS.md` - 问题分析和解决方案
   - `TROUBLESHOOTING.md` - 详细故障排除指南
   - `COMPLETE_SETUP_GUIDE.md` - 完整设置指南

---

## 💡 最佳实践建议

1. **始终设置环境变量**：
   - 即使自动分类工作正常，也建议设置环境变量作为备用
   - Google Scholar的反爬虫机制可能导致获取失败

2. **定期更新数值**：
   - 当您发表新论文时，记得更新GitHub Secrets中的数值
   - 或者让系统自动更新（如果分类成功）

3. **监控分类结果**：
   - 定期查看GitHub Actions日志
   - 如果发现分类结果不合理，使用环境变量手动设置

---

**预计完成时间**：10-15分钟（如果已有准确的数值）

