# 您的出版物指标配置信息

根据您提供的信息，以下是您的配置详情：

## 📊 数据来源策略

### 主要数据源：Google Scholar（自动获取）
以下指标将从Google Scholar自动获取：
- ✅ **国际期刊论文数量** (`INT_JOURNAL_COUNT`)
- ✅ **国际会议论文数量** (`INT_CONF_COUNT`)
- ✅ **总引用数** (`TOTAL_CITATIONS`)
- ✅ **H-index** (`H_INDEX`)
- ✅ **书籍/章节** (`BOOK_COUNT`) - 国际专著

### 辅助数据源：百度学术（手动设置回退值）
以下指标使用百度学术数据作为回退值：
- 📝 **中文期刊论文数量** (`CN_JOURNAL_COUNT`) - 仅用于中文期刊统计
- 📝 **中文专著** - 如果需要单独统计

---

## 📊 从百度学术获取的中文数据

根据 [百度学术页面](https://xueshu.baidu.com/scholarID/CN-B9G8SHIK) 的数据，用于中文论文统计：

| 指标 | 数值 | 说明 |
|------|------|------|
| **中文期刊论文** | 51 | 北大核心期刊（可根据实际情况调整） |
| **中文专著** | 3 | 图书/专著（如果需要单独统计） |

### 详细分类（百度学术）：
- **北大核心期刊**: 51篇
- **CSCD期刊**: 19篇
- **中国科技核心**: 54篇
- **图书/专著**: 3篇

> **注意**: 这些分类可能有重叠，建议根据实际情况设置 `CN_JOURNAL_COUNT` 的值。

---

## 🔧 GitHub Secrets 配置步骤

### 步骤1：访问GitHub仓库设置

1. 进入您的GitHub仓库
2. 点击 **Settings**（设置）
3. 在左侧菜单选择 **Secrets and variables** > **Actions**
4. 点击 **New repository secret**（新建仓库密钥）

### 步骤2：设置Google Scholar ID（主要数据源）

创建以下Secret：

```
Name: GOOGLE_SCHOLAR_ID
Value: dsK8i4EAAAAJ
```

### 步骤3：设置中文数据回退值（推荐）

**重要**: 以下值仅作为回退值使用。系统会优先从Google Scholar自动获取数据。

#### 必需设置（中文数据）：
```
Name: CN_JOURNAL_COUNT
Value: 51
说明: 中文期刊论文数量（从百度学术：北大核心期刊51篇，可根据实际情况调整）
```

#### 可选设置（作为回退值，以防Google Scholar获取失败）：
```
Name: INT_JOURNAL_COUNT
Value: （留空或设置，Google Scholar会自动获取）

Name: INT_CONF_COUNT
Value: （留空或设置，Google Scholar会自动获取）

Name: BOOK_COUNT
Value: （留空或设置，Google Scholar会自动获取）

Name: TOTAL_CITATIONS
Value: （留空或设置，Google Scholar会自动获取）

Name: H_INDEX
Value: （留空或设置，Google Scholar会自动获取）
```

> **建议**: 如果Google Scholar访问稳定，可以只设置 `CN_JOURNAL_COUNT`。如果担心Google Scholar获取失败，可以设置所有回退值。

---

## 📝 配置清单

请确认以下Secrets已创建：

### 必需配置
- [x] `GOOGLE_SCHOLAR_ID` = `dsK8i4EAAAAJ` （Google Scholar自动获取主要数据）

### 推荐配置（中文数据）
- [ ] `CN_JOURNAL_COUNT` = `51`（中文期刊论文，从百度学术获取）

### 可选配置（回退值，以防Google Scholar获取失败）
- [ ] `INT_JOURNAL_COUNT` = （Google Scholar会自动获取，可留空）
- [ ] `INT_CONF_COUNT` = （Google Scholar会自动获取，可留空）
- [ ] `BOOK_COUNT` = （Google Scholar会自动获取，可留空）
- [ ] `TOTAL_CITATIONS` = （Google Scholar会自动获取，可留空）
- [ ] `H_INDEX` = （Google Scholar会自动获取，可留空）

---

## 🚀 测试配置

配置完成后：

1. 进入仓库的 **Actions** 页面
2. 选择 **Update Publication Metrics** 工作流
3. 点击 **Run workflow**（运行工作流）
4. 等待工作流完成
5. 检查 README.md 中的指标表格是否已更新

---

## ⚠️ 注意事项

### 数据来源优先级

1. **主要数据（Google Scholar自动获取）**：
   - 系统会优先从Google Scholar自动获取以下数据：
     - 国际期刊论文数量
     - 国际会议论文数量
     - 总引用数
     - H-index
     - 国际书籍/章节
   - 这些数据每天自动更新

2. **中文数据（百度学术，手动设置）**：
   - `CN_JOURNAL_COUNT` 需要手动设置（从百度学术获取）
   - 这是唯一需要手动维护的中文指标

3. **回退机制**：
   - 如果Google Scholar获取失败，会使用您设置的回退值
   - 建议设置回退值以确保系统稳定运行

### 关于中文期刊论文数量

从百度学术数据看：
- 北大核心期刊：51篇
- CSCD期刊：19篇
- 中国科技核心：54篇

这些可能有重叠。建议您根据实际情况设置 `CN_JOURNAL_COUNT` 的值。如果无法确定，可以先设置为 `51`（北大核心期刊数），后续可以根据需要调整。

### 关于国际期刊论文数量

- 从Google Scholar获取时会自动分类和统计
- 如果Google Scholar获取失败，会使用您设置的回退值（如果有）
- 建议让Google Scholar自动获取，保持数据最新

---

## 🔄 后续更新

- 系统会每天自动从Google Scholar获取最新数据
- 如果自动获取失败，会使用您设置的回退值
- 您可以随时更新GitHub Secrets中的值

---

## 📞 需要帮助？

如果配置过程中遇到问题，请：
1. 查看GitHub Actions日志
2. 检查Secrets是否正确设置
3. 参考 `CONFIGURATION_GUIDE.md` 获取详细说明

