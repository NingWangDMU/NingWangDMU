# 详细步骤指南 - 从零开始配置

本指南将带您完成从代码提交到配置运行的完整流程。

## ⚡ 快速回答：是否需要先 Fetch 和 Push？

**简短回答**：
- ✅ **是的，建议先 Fetch**：在提交本地更改之前，先获取远程仓库的最新更改，避免冲突
- ✅ **必须 Push**：提交本地更改后，必须推送到GitHub，否则GitHub上不会有这些文件

**详细说明**：
1. **Fetch（获取）**：从GitHub下载最新更改，但不合并。建议在每次提交前先执行，确保本地和远程同步
2. **Pull（拉取）**：如果Fetch后发现远程有更新，需要Pull来合并这些更新
3. **Commit（提交）**：将本地更改保存到本地Git仓库
4. **Push（推送）**：将本地提交推送到GitHub，使更改在GitHub上可见

**操作顺序**：
```
Fetch → (如果有远程更新) Pull → Commit → Push
```

---

## 📋 第一步：在GitHub Desktop中同步代码

### 1.1 打开GitHub Desktop并检查状态

1. **打开GitHub Desktop应用程序**
2. **确认当前仓库**：
   - 在顶部确认显示的是 `NingWangDMU` 仓库
   - 如果显示其他仓库，点击顶部仓库名称，选择 `NingWangDMU`

3. **检查本地更改状态**：
   - 查看左侧面板，如果有未提交的更改，会显示数字（如 "5 changed files"）
   - 如果有数字，说明有本地更改需要提交

### 1.2 先进行 Fetch（获取远程更新）

**重要**：在提交本地更改之前，建议先获取远程仓库的最新更改，避免冲突。

1. **点击顶部菜单栏的 Repository（仓库）**
2. **选择 Fetch origin（获取远程更新）**
   - 或者直接按快捷键 `Ctrl+Shift+F`（Windows）
   - 这会从GitHub下载最新的更改，但不会合并到本地

3. **检查是否有远程更改**：
   - 如果Fetch后显示 "This branch is X commits behind origin/main"（此分支落后X个提交）
   - 说明远程有更新，需要先 Pull（拉取）
   - 点击 **Pull origin** 按钮，将远程更改合并到本地

### 1.3 提交本地更改（如果有未提交的文件）

如果左侧显示有未提交的更改：

1. **查看更改列表**：
   - 在左侧面板查看所有更改的文件
   - 确认以下文件都在列表中：
     - ✅ `README.md`
     - ✅ `scripts/update_metrics.py`
     - ✅ `scripts/update_metrics_simple.py`
     - ✅ `scripts/config.example.json`
     - ✅ `scripts/README.md`
     - ✅ `.github/workflows/update-publication-metrics.yml`
     - ✅ `requirements.txt`
     - ✅ `.gitignore`（如果存在）
     - ✅ 各种配置文档（`SETUP_METRICS.md`、`YOUR_CONFIGURATION.md` 等）

2. **选择要提交的文件**：
   - 默认情况下，所有文件都应该被勾选
   - 如果某个文件未勾选，点击复选框选中它
   - **注意**：不要勾选 `scripts/config.json`（如果存在），这个文件应该被忽略

3. **输入提交信息**：
   - 在底部左侧的文本框中输入提交信息，例如：
     ```
     添加出版物指标自动更新系统
     ```
   - 或者更详细的：
     ```
     添加出版物指标自动更新系统
     - 添加GitHub Actions工作流
     - 添加Python脚本用于自动获取指标
     - 更新README.md添加指标表格
     ```

4. **提交更改**：
   - 点击底部右侧的 **Commit to main** 按钮（或您的主分支名称）
   - 等待提交完成（通常几秒钟）

### 1.4 推送到GitHub（Push）

提交完成后，需要将更改推送到GitHub：

1. **检查推送状态**：
   - 提交后，顶部会显示 "X commits ahead of origin/main"（领先X个提交）
   - 右侧会显示 **Push origin** 按钮

2. **推送到GitHub**：
   - 点击右上角的 **Push origin** 按钮
   - 或者点击顶部菜单栏的 **Repository** > **Push**
   - 等待推送完成（通常需要几秒到几十秒，取决于文件大小）

3. **确认推送成功**：
   - 推送完成后，顶部应该显示 "This branch is up to date with origin/main"（此分支与远程同步）
   - 不再显示 "X commits ahead" 的提示

### 1.5 验证代码已上传到GitHub

推送完成后，验证所有文件都已成功上传：

1. **在浏览器中打开您的GitHub仓库**：
   - 访问 `https://github.com/NingWangDMU/NingWangDMU`（或您的仓库地址）

2. **检查以下文件是否存在**：
   - ✅ `README.md`（包含指标表格）
   - ✅ `scripts/update_metrics.py`
   - ✅ `scripts/update_metrics_simple.py`
   - ✅ `scripts/config.example.json`
   - ✅ `scripts/README.md`
   - ✅ `.github/workflows/update-publication-metrics.yml`
   - ✅ `requirements.txt`
   - ✅ `.gitignore`（如果存在）

3. **验证文件内容**：
   - 点击 `README.md`，滚动到 "Publication Metrics" 部分
   - 确认表格存在且显示 "Loading..." 占位符
   - 点击 `.github/workflows/update-publication-metrics.yml`，确认工作流文件存在

4. **如果文件缺失**：
   - 返回GitHub Desktop，检查是否有未提交的更改
   - 如果有，重复步骤1.3和1.4
   - 如果GitHub Desktop显示 "Nothing to commit"，但文件仍然缺失，可能需要刷新浏览器页面

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
- [ ] 打开GitHub Desktop并确认仓库
- [ ] 执行 Fetch origin（获取远程更新）
- [ ] 如果有远程更新，执行 Pull origin（拉取并合并）
- [ ] 检查本地未提交的更改
- [ ] 选择所有需要提交的文件
- [ ] 输入提交信息并提交（Commit）
- [ ] 推送到GitHub（Push origin）
- [ ] 验证所有文件已成功上传到GitHub

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

