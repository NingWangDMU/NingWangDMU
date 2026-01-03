# 详细步骤指南 - 从零开始配置

本指南将带您完成从代码提交到配置运行的完整流程。

---

## 📋 第一步：提交代码到GitHub（如果还没有）

### 1.1 检查当前状态

在GitHub Desktop中：

1. **打开GitHub Desktop**
2. **检查当前仓库状态**：
   - 查看左侧是否有未提交的更改（显示为数字）
   - 如果有更改，需要先提交

### 1.2 提交更改（如果有未提交的文件）

1. **在GitHub Desktop中**：
   - 查看左侧的更改列表
   - 确认所有新文件都已勾选（包括README.md、scripts文件夹、.github文件夹等）
   - 在底部输入提交信息，例如：
     ```
     添加出版物指标自动更新系统
     ```
   - 点击 **Commit to main**（或您的主分支名称）

2. **推送到GitHub**：
   - 点击右上角的 **Push origin** 按钮
   - 等待推送完成

### 1.3 验证代码已上传

1. **在浏览器中打开您的GitHub仓库**
2. **检查以下文件是否存在**：
   - ✅ `README.md`（包含指标表格）
   - ✅ `scripts/update_metrics.py`
   - ✅ `scripts/update_metrics_simple.py`
   - ✅ `.github/workflows/update-publication-metrics.yml`
   - ✅ `requirements.txt`
   - ✅ `.gitignore`

---

## 🔧 第二步：在GitHub仓库中设置Secrets

### 2.1 进入Secrets设置页面

1. **在浏览器中打开您的GitHub仓库**
2. **点击仓库顶部的 Settings（设置）标签**
3. **在左侧菜单中找到并点击 Secrets and variables**
4. **选择 Actions**

### 2.2 创建第一个Secret：Google Scholar ID

1. **点击 New repository secret 按钮**（右上角）
2. **填写信息**：
   ```
   Name: GOOGLE_SCHOLAR_ID
   Secret: dsK8i4EAAAAJ
   ```
3. **点击 Add secret 按钮**

### 2.3 创建第二个Secret：中文期刊数量

1. **再次点击 New repository secret 按钮**
2. **填写信息**：
   ```
   Name: CN_JOURNAL_COUNT
   Secret: 51
   ```
3. **点击 Add secret 按钮**

### 2.4 验证Secrets已创建

在Secrets列表中，您应该看到：
- ✅ `GOOGLE_SCHOLAR_ID`
- ✅ `CN_JOURNAL_COUNT`

---

## 🚀 第三步：运行GitHub Actions工作流

### 3.1 进入Actions页面

1. **在GitHub仓库页面，点击顶部的 Actions 标签**
2. **如果这是第一次使用Actions，可能需要点击 I understand my workflows, go ahead and enable them**

### 3.2 运行工作流

1. **在左侧工作流列表中，找到 "Update Publication Metrics"**
2. **点击它**
3. **点击右侧的 Run workflow 下拉按钮**
4. **选择 Run workflow**
5. **确认分支是 main（或您的主分支）**
6. **点击绿色的 Run workflow 按钮**

### 3.3 查看运行状态

1. **工作流会出现在列表中，显示为黄色（运行中）或绿色（成功）**
2. **点击工作流运行记录查看详情**
3. **等待完成**（通常需要1-3分钟）

### 3.4 检查日志（如果失败）

如果工作流失败（红色）：
1. **点击失败的工作流运行**
2. **查看日志，找到错误信息**
3. **常见问题**：
   - Secrets未设置 → 返回步骤2
   - 权限问题 → 检查仓库设置
   - 脚本错误 → 查看具体错误信息

---

## ✅ 第四步：验证结果

### 4.1 检查README.md是否已更新

1. **在GitHub仓库页面，打开 README.md 文件**
2. **滚动到 "Publication Metrics" 部分**
3. **检查指标表格**：
   - 应该显示实际数值，而不是"Loading..."
   - 应该有"Last Updated"时间戳

### 4.2 检查指标数值

确认以下指标已正确显示：
- ✅ 国际期刊论文数量（从Google Scholar获取）
- ✅ 中文期刊论文数量（显示51或您设置的值）
- ✅ 国际会议论文数量（从Google Scholar获取）
- ✅ 总引用数（从Google Scholar获取）
- ✅ H-index（从Google Scholar获取）
- ✅ 最后更新时间

---

## 🔄 第五步：设置自动更新（已完成）

系统已经配置为每天自动更新：
- **自动运行时间**：每天UTC时间凌晨2点（北京时间上午10点）
- **无需手动操作**：系统会自动运行并更新指标

---

## 📝 完整操作清单

### 代码提交阶段
- [ ] 在GitHub Desktop中检查未提交的更改
- [ ] 提交所有更改（如果有）
- [ ] 推送到GitHub
- [ ] 验证所有文件已上传

### 配置阶段
- [ ] 进入GitHub仓库 Settings
- [ ] 进入 Secrets and variables > Actions
- [ ] 创建Secret：`GOOGLE_SCHOLAR_ID` = `dsK8i4EAAAAJ`
- [ ] 创建Secret：`CN_JOURNAL_COUNT` = `51`
- [ ] 验证两个Secrets都已创建

### 测试阶段
- [ ] 进入Actions页面
- [ ] 运行"Update Publication Metrics"工作流
- [ ] 等待工作流完成
- [ ] 检查工作流是否成功（绿色）

### 验证阶段
- [ ] 打开README.md
- [ ] 检查指标表格是否已更新
- [ ] 确认所有指标都显示数值（不是"Loading..."）
- [ ] 确认有最后更新时间

---

## 🆘 常见问题解决

### 问题1：GitHub Desktop显示"Nothing to commit"

**说明**：所有更改已提交，可以直接进行下一步（设置Secrets）

### 问题2：工作流显示"找不到文件"

**解决**：
1. 确认所有文件都已推送到GitHub
2. 在GitHub仓库页面检查文件是否存在
3. 如果文件不存在，返回步骤1重新提交

### 问题3：工作流失败，显示"Permission denied"

**解决**：
1. 检查仓库设置 > Actions > General
2. 确保"Workflow permissions"设置为"Read and write permissions"
3. 保存设置后重新运行工作流

### 问题4：指标仍然显示"Loading..."

**解决**：
1. 检查Secrets是否正确设置
2. 查看Actions日志，确认脚本是否成功运行
3. 确认工作流已成功完成（绿色）
4. 刷新README.md页面

### 问题5：Google Scholar数据获取失败

**说明**：这是正常的，Google Scholar有反爬虫机制

**解决**：
1. 系统会自动使用回退值（如果已设置）
2. 可以设置更多回退值（参考`YOUR_CONFIGURATION.md`）
3. 或者等待下次自动运行（可能成功）

---

## 📞 需要帮助？

如果遇到问题：
1. 查看GitHub Actions日志了解具体错误
2. 参考 `CONFIGURATION_GUIDE.md` 获取详细说明
3. 检查 `YOUR_CONFIGURATION.md` 确认配置是否正确

---

## 🎉 完成！

配置完成后，系统会：
- ✅ 每天自动更新指标
- ✅ 从Google Scholar获取最新数据
- ✅ 使用您设置的中文期刊数量
- ✅ 自动更新README.md

您无需再做任何操作，系统会自动运行！

