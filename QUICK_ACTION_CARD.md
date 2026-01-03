# ⚡ 快速操作卡片

## 📝 当前状态检查

### ✅ 代码文件状态
- [x] `README.md` - 指标表格占位符正确
- [x] `scripts/update_metrics.py` - 主脚本正常
- [x] `scripts/update_metrics_simple.py` - 简化脚本正常
- [x] `.github/workflows/update-publication-metrics.yml` - 工作流配置正确
- [x] `requirements.txt` - 依赖列表完整
- [x] `.gitignore` - 忽略规则正确

### ⚠️ 需要执行的操作

---

## 🚀 三步快速操作

### 第一步：GitHub Desktop - 提交代码

```
1. 打开GitHub Desktop
2. 点击 Repository > Fetch origin (或按 Ctrl+Shift+F)
3. 如果有远程更新，点击 Pull origin
4. 检查左侧更改列表，确认所有文件已勾选
5. 输入提交信息："添加出版物指标自动更新系统"
6. 点击 Commit to main
7. 点击 Push origin
8. 等待推送完成
```

**验证**：在浏览器打开GitHub仓库，确认所有文件已上传

---

### 第二步：GitHub网页 - 设置Secrets

```
1. 打开 https://github.com/NingWangDMU/NingWangDMU
2. 点击 Settings > Secrets and variables > Actions
3. 点击 New repository secret，创建以下Secrets：

   Secret 1:
   Name: GOOGLE_SCHOLAR_ID
   Value: dsK8i4EAAAAJ

   Secret 2:
   Name: CN_JOURNAL_COUNT
   Value: 51

   Secret 3 (推荐):
   Name: TOTAL_CITATIONS
   Value: [您的总引用数]

   Secret 4 (推荐):
   Name: H_INDEX
   Value: [您的H-index]
```

**验证**：在Secrets列表中看到所有已创建的Secret

---

### 第三步：GitHub Actions - 运行工作流

```
1. 在GitHub仓库页面，点击 Actions 标签
2. 左侧找到 "Update Publication Metrics" 工作流
3. 点击右侧 "Run workflow" 下拉按钮
4. 确认分支是 main
5. 点击绿色 "Run workflow" 按钮
6. 等待1-3分钟完成
```

**验证**：
- 工作流显示绿色（成功）
- README.md中的指标显示实际数值（不是"Loading..."）

---

## 📋 必需Secrets清单

### 最低配置（必需）
- ✅ `GOOGLE_SCHOLAR_ID`: `dsK8i4EAAAAJ`
- ✅ `CN_JOURNAL_COUNT`: `51`（或您的实际数值）

### 推荐配置（强烈推荐）
- ✅ `TOTAL_CITATIONS`: 您的总引用数
- ✅ `H_INDEX`: 您的H-index

### 完整配置（可选）
- `INT_JOURNAL_COUNT`: 国际期刊论文数量
- `INT_CONF_COUNT`: 国际会议论文数量
- `BOOK_COUNT`: 书籍/章节数量

---

## 🔍 验证清单

完成后，确认以下项目：

- [ ] 所有代码文件已推送到GitHub
- [ ] 至少2个Secrets已设置（`GOOGLE_SCHOLAR_ID` 和 `CN_JOURNAL_COUNT`）
- [ ] GitHub Actions工作流已成功运行（绿色）
- [ ] README.md中的指标显示实际数值
- [ ] "Last Updated"时间戳已更新

---

## 🆘 快速故障排除

### 问题：工作流失败
→ 查看Actions日志，检查Secrets是否正确设置

### 问题：指标仍显示"Loading..."
→ 确认工作流已成功完成，刷新README.md页面

### 问题：无法看到Settings标签
→ 确认您有仓库管理员权限

---

## 📚 详细文档

- **完整指南**：`COMPLETE_SETUP_GUIDE.md`
- **快速开始**：`QUICK_START.md`
- **故障排除**：`TROUBLESHOOTING.md`

---

**预计完成时间**：10-15分钟

