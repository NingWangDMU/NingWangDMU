# 🚀 快速开始指南

根据您的配置（Google Scholar ID: `dsK8i4EAAAAJ`），按照以下步骤快速完成设置。

---

## 📝 操作清单（按顺序执行）

### ✅ 第一步：在GitHub Desktop中同步代码

1. **打开GitHub Desktop**
2. **确认仓库**：顶部显示 `NingWangDMU`
3. **Fetch（获取远程更新）**：
   - 点击菜单栏 **Repository** > **Fetch origin**
   - 或按快捷键 `Ctrl+Shift+F`
4. **如果有远程更新**：
   - 点击 **Pull origin** 按钮合并远程更改
5. **检查本地更改**：
   - 左侧显示有未提交的更改（显示数字）
6. **提交更改**：
   - 确认所有文件都已勾选
   - 输入提交信息：`添加出版物指标自动更新系统`
   - 点击 **Commit to main**
7. **推送到GitHub**：
   - 点击右上角 **Push origin** 按钮
   - 等待完成

**验证**：在浏览器打开GitHub仓库，确认所有文件都已上传。

---

### ✅ 第二步：设置GitHub Secrets

1. **进入GitHub仓库设置**：
   - 在浏览器打开您的GitHub仓库
   - 点击顶部 **Settings** 标签
   - 左侧菜单选择 **Secrets and variables** > **Actions**

2. **创建第一个Secret**：
   - 点击 **New repository secret**
   - Name: `GOOGLE_SCHOLAR_ID`
   - Secret: `dsK8i4EAAAAJ`
   - 点击 **Add secret**

3. **创建第二个Secret**：
   - 再次点击 **New repository secret**
   - Name: `CN_JOURNAL_COUNT`
   - Secret: `51`（或您从百度学术获取的实际数值）
   - 点击 **Add secret**

**验证**：在Secrets列表中看到两个Secret。

---

### ✅ 第三步：运行GitHub Actions工作流

1. **进入Actions页面**：
   - 在GitHub仓库页面，点击顶部 **Actions** 标签
   - 如果是第一次，点击 **I understand my workflows, go ahead and enable them**

2. **运行工作流**：
   - 左侧找到 **Update Publication Metrics**
   - 点击它
   - 点击右侧 **Run workflow** 下拉按钮
   - 选择 **Run workflow**
   - 确认分支是 `main`
   - 点击绿色 **Run workflow** 按钮

3. **等待完成**：
   - 工作流显示为黄色（运行中）或绿色（成功）
   - 通常需要1-3分钟

---

### ✅ 第四步：验证结果

1. **检查README.md**：
   - 在GitHub仓库页面打开 `README.md`
   - 滚动到 **Publication Metrics** 部分
   - 确认指标显示实际数值（不是"Loading..."）
   - 确认有"Last Updated"时间戳

2. **检查指标**：
   - ✅ 国际期刊论文数量（从Google Scholar）
   - ✅ 中文期刊论文数量（显示51或您设置的值）
   - ✅ 国际会议论文数量（从Google Scholar）
   - ✅ 总引用数（从Google Scholar）
   - ✅ H-index（从Google Scholar）

---

## 🎉 完成！

配置完成后，系统会：
- ✅ 每天自动更新指标（UTC 2:00，北京时间10:00）
- ✅ 从Google Scholar自动获取最新数据
- ✅ 使用您设置的中文期刊数量
- ✅ 自动更新README.md

**您无需再做任何操作，系统会自动运行！**

---

## 🆘 遇到问题？

### 问题1：GitHub Desktop显示"Nothing to commit"
**说明**：所有更改已提交，可以直接进行下一步（设置Secrets）

### 问题2：工作流失败
**解决**：
1. 点击失败的工作流，查看日志
2. 检查Secrets是否正确设置
3. 检查仓库设置 > Actions > General > Workflow permissions 是否为 "Read and write permissions"

### 问题3：指标仍然显示"Loading..."
**解决**：
1. 确认工作流已成功完成（绿色）
2. 刷新README.md页面
3. 检查Actions日志，确认脚本是否成功运行

---

## 📚 需要更多帮助？

- 详细步骤：查看 `STEP_BY_STEP_GUIDE.md`
- 配置说明：查看 `YOUR_CONFIGURATION.md`
- 配置总结：查看 `CONFIG_SUMMARY.md`

