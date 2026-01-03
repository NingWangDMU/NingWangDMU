# 🚀 完整设置指南 - 从代码到运行

本指南将带您完成从提交代码到运行GitHub Actions的完整流程。

---

## 📋 检查清单

在开始之前，请确认以下文件都已就绪：

- ✅ `README.md` - 包含指标表格占位符
- ✅ `scripts/update_metrics.py` - 主更新脚本
- ✅ `scripts/update_metrics_simple.py` - 简化版脚本
- ✅ `.github/workflows/update-publication-metrics.yml` - GitHub Actions工作流
- ✅ `requirements.txt` - Python依赖
- ✅ `.gitignore` - Git忽略规则

---

## 第一部分：在GitHub Desktop中提交代码

### 步骤 1.1：打开GitHub Desktop并检查状态

1. **启动GitHub Desktop应用程序**

2. **确认当前仓库**：
   - 在顶部确认显示的是 `NingWangDMU` 仓库
   - 如果显示其他仓库，点击顶部仓库名称下拉菜单，选择 `NingWangDMU`

3. **检查本地更改**：
   - 查看左侧面板，如果有未提交的更改，会显示数字（如 "5 changed files"）
   - 如果有数字，说明有本地更改需要提交

### 步骤 1.2：获取远程更新（Fetch & Pull）

**重要**：在提交本地更改之前，先获取远程仓库的最新更改，避免冲突。

1. **执行 Fetch（获取远程更新）**：
   - 点击顶部菜单栏的 **Repository（仓库）**
   - 选择 **Fetch origin（获取远程更新）**
   - 或者直接按快捷键 `Ctrl+Shift+F`（Windows）
   - 这会从GitHub下载最新的更改，但**不会**合并到本地

2. **检查是否有远程更改**：
   - 如果Fetch后显示 **"This branch is X commits behind origin/main"**（此分支落后X个提交）
   - 说明远程有更新，需要先 Pull（拉取）

3. **执行 Pull（拉取并合并）**：
   - 如果显示落后，点击 **Pull origin** 按钮
   - 或者点击菜单栏 **Repository** > **Pull origin**
   - 这将把远程更改合并到本地

4. **确认同步状态**：
   - 完成后，应该显示 **"This branch is up to date with origin/main"**（此分支与远程同步）

### 步骤 1.3：查看并选择要提交的文件

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
     - ✅ 各种配置文档（`SETUP_METRICS.md`、`YOUR_CONFIGURATION.md`、`TROUBLESHOOTING.md` 等）

2. **选择要提交的文件**：
   - 默认情况下，所有文件都应该被勾选（复选框为 ✓）
   - 如果某个文件未勾选，点击复选框选中它
   - **重要**：不要勾选 `scripts/config.json`（如果存在），这个文件应该被忽略

3. **查看文件更改内容**（可选）：
   - 点击文件名，右侧会显示具体的更改内容
   - 可以确认更改是否正确

### 步骤 1.4：提交更改（Commit）

1. **输入提交信息**：
   - 在底部左侧的文本框中输入提交信息
   - 建议使用以下格式：
     ```
     添加出版物指标自动更新系统
     
     - 添加GitHub Actions工作流
     - 添加Python脚本用于自动获取指标
     - 更新README.md添加指标表格
     - 添加配置文档和故障排除指南
     ```
   - 或者更简洁的：
     ```
     添加出版物指标自动更新系统
     ```

2. **提交更改**：
   - 点击底部右侧的 **Commit to main** 按钮（或您的主分支名称）
   - 等待提交完成（通常几秒钟）
   - 提交后，左侧面板的更改列表应该消失

### 步骤 1.5：推送到GitHub（Push）

1. **检查推送状态**：
   - 提交完成后，顶部会显示 **"X commits ahead of origin/main"**（领先X个提交）
   - 右侧会显示 **Push origin** 按钮

2. **推送到GitHub**：
   - 点击右上角的 **Push origin** 按钮
   - 或者点击顶部菜单栏的 **Repository** > **Push**
   - 等待推送完成（通常需要几秒到几十秒，取决于文件大小和网络速度）

3. **确认推送成功**：
   - 推送完成后，顶部应该显示 **"This branch is up to date with origin/main"**（此分支与远程同步）
   - 不再显示 "X commits ahead" 的提示

### 步骤 1.6：验证代码已上传到GitHub

1. **在浏览器中打开您的GitHub仓库**：
   - 访问 `https://github.com/NingWangDMU/NingWangDMU`（或您的仓库地址）
   - 或者点击GitHub Desktop中的 **View on GitHub** 按钮

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
   - 点击 `README.md`，滚动到 **"Publication Metrics"** 部分
   - 确认表格存在且显示 "Loading..." 占位符
   - 点击 `.github/workflows/update-publication-metrics.yml`，确认工作流文件存在

4. **如果文件缺失**：
   - 返回GitHub Desktop，检查是否有未提交的更改
   - 如果有，重复步骤1.3和1.4
   - 如果GitHub Desktop显示 "Nothing to commit"，但文件仍然缺失，可能需要刷新浏览器页面

---

## 第二部分：在GitHub网页上设置Secrets

### 步骤 2.1：进入仓库设置

1. **打开GitHub仓库页面**：
   - 在浏览器中访问 `https://github.com/NingWangDMU/NingWangDMU`

2. **进入设置页面**：
   - 点击仓库页面顶部的 **Settings（设置）** 标签
   - 如果看不到Settings标签，确认您有仓库的管理员权限

3. **进入Secrets设置**：
   - 在左侧菜单中，找到 **Secrets and variables** 部分
   - 点击 **Actions** 子菜单
   - 您会看到 "Repository secrets" 部分

### 步骤 2.2：创建必需的Secrets

根据您的配置（Google Scholar ID: `dsK8i4EAAAAJ`），需要设置以下Secrets：

#### Secret 1：GOOGLE_SCHOLAR_ID（必需）

1. **点击 "New repository secret" 按钮**

2. **填写信息**：
   - **Name**: `GOOGLE_SCHOLAR_ID`
   - **Secret**: `dsK8i4EAAAAJ`
   - **注意**：Name必须完全匹配（区分大小写）

3. **点击 "Add secret" 按钮**

4. **确认创建成功**：
   - 在Secrets列表中应该看到 `GOOGLE_SCHOLAR_ID`（值会被隐藏显示为 `••••••••••••••••`）

#### Secret 2：CN_JOURNAL_COUNT（必需）

1. **再次点击 "New repository secret" 按钮**

2. **填写信息**：
   - **Name**: `CN_JOURNAL_COUNT`
   - **Secret**: `51`（或您从百度学术获取的实际数值）
   - **注意**：只输入数字，不要包含其他字符

3. **点击 "Add secret" 按钮**

#### Secret 3：TOTAL_CITATIONS（强烈推荐）

1. **点击 "New repository secret" 按钮**

2. **填写信息**：
   - **Name**: `TOTAL_CITATIONS`
   - **Secret**: 您的总引用数（例如：`5000`）
   - **如何获取**：访问您的Google Scholar主页，查看总引用数

3. **点击 "Add secret" 按钮**

#### Secret 4：H_INDEX（强烈推荐）

1. **点击 "New repository secret" 按钮**

2. **填写信息**：
   - **Name**: `H_INDEX`
   - **Secret**: 您的H-index（例如：`45`）
   - **如何获取**：访问您的Google Scholar主页，查看H-index

3. **点击 "Add secret" 按钮**

#### Secret 5-7：可选指标（可选但推荐）

如果需要更完整的指标，可以继续添加：

- **INT_JOURNAL_COUNT**: 国际期刊论文数量
- **INT_CONF_COUNT**: 国际会议论文数量
- **BOOK_COUNT**: 书籍/章节数量

**设置方法**：重复上述步骤，使用对应的Name和Value

### 步骤 2.3：验证所有Secrets已设置

1. **检查Secrets列表**：
   - 在 "Repository secrets" 部分，您应该看到所有已创建的Secrets
   - 每个Secret的名称应该清晰可见
   - 值会被隐藏显示为点号

2. **确认必需的Secrets**：
   - ✅ `GOOGLE_SCHOLAR_ID` - 已设置
   - ✅ `CN_JOURNAL_COUNT` - 已设置
   - ✅ `TOTAL_CITATIONS` - 已设置（推荐）
   - ✅ `H_INDEX` - 已设置（推荐）

3. **如果需要修改Secret**：
   - 点击Secret名称右侧的 **✏️（编辑）** 图标
   - 修改值后点击 **Update secret**

4. **如果需要删除Secret**：
   - 点击Secret名称右侧的 **🗑️（删除）** 图标
   - 确认删除操作

---

## 第三部分：运行GitHub Actions工作流

### 步骤 3.1：进入Actions页面

1. **打开GitHub仓库页面**：
   - 在浏览器中访问 `https://github.com/NingWangDMU/NingWangDMU`

2. **进入Actions页面**：
   - 点击仓库页面顶部的 **Actions** 标签
   - 如果是第一次使用Actions，可能会看到提示：
     - **"Get started with GitHub Actions"** 或
     - **"I understand my workflows, go ahead and enable them"**
   - 如果看到这些提示，点击相应的按钮启用Actions

### 步骤 3.2：找到工作流

1. **查看工作流列表**：
   - 在左侧边栏，您应该看到 **"Update Publication Metrics"** 工作流
   - 如果看不到，可能需要刷新页面

2. **点击工作流名称**：
   - 点击 **"Update Publication Metrics"** 进入工作流详情页面

### 步骤 3.3：手动触发工作流

1. **找到运行按钮**：
   - 在工作流详情页面右侧，找到 **"Run workflow"** 下拉按钮
   - 如果看不到，可能需要等待页面完全加载

2. **点击运行按钮**：
   - 点击 **"Run workflow"** 下拉按钮
   - 会显示一个下拉菜单

3. **选择分支**：
   - 在下拉菜单中，确认分支选择为 **"main"**（或您的主分支名称）
   - 如果显示其他分支，点击下拉菜单选择正确的分支

4. **确认并运行**：
   - 点击绿色的 **"Run workflow"** 按钮
   - 工作流会立即开始运行

### 步骤 3.4：监控工作流执行

1. **查看运行状态**：
   - 工作流开始运行后，页面会自动刷新
   - 您会看到一个新的运行记录，显示为黄色（运行中）或绿色（成功）或红色（失败）

2. **查看运行详情**：
   - 点击运行记录，查看详细执行过程
   - 您会看到各个步骤的执行状态：
     - ✅ 绿色勾号 = 成功
     - ⏳ 黄色圆圈 = 运行中
     - ❌ 红色叉号 = 失败

3. **查看日志输出**：
   - 点击 **"Run update script"** 步骤
   - 展开后可以看到详细的日志输出，包括：
     - 环境变量检查结果
     - Google Scholar获取尝试
     - 指标更新过程
     - 最终结果

4. **等待完成**：
   - 通常需要1-3分钟完成
   - 如果超过5分钟仍在运行，可能需要检查是否有问题

---

## 第四部分：验证结果

### 步骤 4.1：检查README.md是否已更新

1. **打开README.md文件**：
   - 在GitHub仓库页面，点击 `README.md` 文件

2. **找到指标表格**：
   - 滚动到 **"Publication Metrics"** 部分（大约在第73行）

3. **检查指标值**：
   - 确认指标显示**实际数值**（不是 "Loading..." 或 "N/A"）
   - 检查以下指标：
     - ✅ **International Journal Papers**: 应该显示数字
     - ✅ **Chinese Journal Papers**: 应该显示 `51`（或您设置的值）
     - ✅ **International Conference Papers**: 应该显示数字
     - ✅ **Books/Chapters**: 应该显示数字
     - ✅ **Total Citations**: 应该显示您的总引用数
     - ✅ **H-index**: 应该显示您的H-index

4. **检查更新时间**：
   - 确认 **"Last Updated"** 列显示当前时间
   - 确认底部的 **"Last update"** 也显示时间戳

### 步骤 4.2：检查Git提交记录

1. **查看提交历史**：
   - 在GitHub仓库页面，点击 **"X commits"** 链接（在文件列表上方）
   - 或者点击 **"History"** 标签

2. **查找自动提交**：
   - 应该看到一条提交记录，提交信息为：
     ```
     Auto-update publication metrics [skip ci]
     ```
   - 提交者显示为 **"GitHub Action"**

3. **查看提交内容**：
   - 点击提交记录，查看更改内容
   - 应该只显示 `README.md` 文件的更改
   - 更改内容应该是将 "Loading..." 替换为实际数值

### 步骤 4.3：验证工作流状态

1. **返回Actions页面**：
   - 点击仓库顶部的 **Actions** 标签

2. **查看最新运行记录**：
   - 应该显示为绿色（成功）
   - 所有步骤都应该显示绿色勾号

3. **如果显示失败（红色）**：
   - 点击运行记录，查看失败原因
   - 检查日志输出，查找错误信息
   - 参考 `TROUBLESHOOTING.md` 文件获取帮助

---

## 第五部分：后续维护

### 自动更新

配置完成后，系统会：
- ✅ **每天自动更新**：UTC时间凌晨2点（北京时间上午10点）
- ✅ **自动提交更改**：更新后自动提交到仓库
- ✅ **无需手动操作**：完全自动化运行

### 手动更新指标

如果需要立即更新指标：

1. **更新GitHub Secrets**：
   - 进入 Settings > Secrets and variables > Actions
   - 修改相应的Secret值
   - 保存更改

2. **手动触发工作流**：
   - 进入 Actions 页面
   - 点击 "Update Publication Metrics" 工作流
   - 点击 "Run workflow" 按钮

### 查看更新历史

1. **查看提交历史**：
   - 在仓库页面查看提交历史
   - 查找 "Auto-update publication metrics" 提交记录

2. **查看Actions历史**：
   - 在Actions页面查看所有运行记录
   - 可以看到每次更新的时间和状态

---

## 🆘 遇到问题？

### 问题1：GitHub Desktop显示"Nothing to commit"

**说明**：所有更改已提交，可以直接进行下一步（设置Secrets）

### 问题2：工作流失败

**解决步骤**：
1. 点击失败的工作流，查看日志
2. 检查Secrets是否正确设置
3. 检查仓库设置 > Actions > General > Workflow permissions 是否为 "Read and write permissions"
4. 参考 `TROUBLESHOOTING.md` 获取详细帮助

### 问题3：指标仍然显示"Loading..."

**解决步骤**：
1. 确认工作流已成功完成（绿色）
2. 刷新README.md页面
3. 检查Actions日志，确认脚本是否成功运行
4. 确认Secrets已正确设置

### 问题4：无法看到Settings标签

**原因**：您可能没有仓库的管理员权限

**解决方案**：
- 联系仓库所有者授予管理员权限
- 或请仓库所有者帮助设置Secrets

---

## ✅ 完成检查清单

完成所有步骤后，确认以下项目：

- [ ] 所有代码文件已提交并推送到GitHub
- [ ] GitHub Secrets已设置（至少 `GOOGLE_SCHOLAR_ID` 和 `CN_JOURNAL_COUNT`）
- [ ] GitHub Actions工作流已成功运行（显示绿色）
- [ ] README.md中的指标显示实际数值（不是"Loading..."）
- [ ] "Last Updated"时间戳已更新

如果所有项目都已勾选，恭喜您！系统已成功配置并运行！🎉

---

## 📚 相关文档

- **快速开始**：`QUICK_START.md`
- **详细步骤**：`STEP_BY_STEP_GUIDE.md`
- **故障排除**：`TROUBLESHOOTING.md`
- **配置说明**：`YOUR_CONFIGURATION.md`

