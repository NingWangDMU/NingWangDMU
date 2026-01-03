# 快速配置指南 - 您的专属配置

## 🎯 配置摘要

根据您提供的信息，以下是需要设置的配置：

### 数据来源策略
- **主要数据源**: Google Scholar（自动获取）
- **中文数据源**: 百度学术（手动设置）

### Google Scholar ID（必需）
```
dsK8i4EAAAAJ
```

### 配置清单

| Secret名称 | 建议值 | 说明 | 优先级 |
|-----------|--------|------|--------|
| `GOOGLE_SCHOLAR_ID` | `dsK8i4EAAAAJ` | Google Scholar ID | ✅ 必需 |
| `CN_JOURNAL_COUNT` | `51` | 中文期刊（百度学术） | ✅ 推荐 |
| `INT_JOURNAL_COUNT` | - | 国际期刊（Google Scholar自动获取） | ⚪ 可选回退 |
| `INT_CONF_COUNT` | - | 会议论文（Google Scholar自动获取） | ⚪ 可选回退 |
| `BOOK_COUNT` | - | 书籍/章节（Google Scholar自动获取） | ⚪ 可选回退 |
| `TOTAL_CITATIONS` | - | 总引用数（Google Scholar自动获取） | ⚪ 可选回退 |
| `H_INDEX` | - | H-index（Google Scholar自动获取） | ⚪ 可选回退 |

---

## 📋 一键配置清单

### 在GitHub仓库中设置Secrets：

1. 进入：**Settings** > **Secrets and variables** > **Actions**
2. 点击：**New repository secret**
3. 逐个创建以下Secrets：

```
✅ GOOGLE_SCHOLAR_ID = dsK8i4EAAAAJ
   （Google Scholar自动获取主要数据）

✅ CN_JOURNAL_COUNT = 51
   （中文期刊论文，从百度学术获取）

⚪ 以下为可选回退值（如果担心Google Scholar获取失败）：
   INT_JOURNAL_COUNT = （留空，Google Scholar会自动获取）
   INT_CONF_COUNT = （留空，Google Scholar会自动获取）
   BOOK_COUNT = （留空，Google Scholar会自动获取）
   TOTAL_CITATIONS = （留空，Google Scholar会自动获取）
   H_INDEX = （留空，Google Scholar会自动获取）
```

---

## ✅ 配置完成后

1. 进入 **Actions** 页面
2. 运行 **Update Publication Metrics** 工作流
3. 检查 README.md 是否已更新

---

## 💡 提示

### 数据来源说明
- **Google Scholar（主要）**: 自动获取国际期刊、国际会议、总引用数、H-index等
- **百度学术（辅助）**: 仅用于中文期刊论文统计（`CN_JOURNAL_COUNT`）

### 配置建议
- **最小配置**: 只需设置 `GOOGLE_SCHOLAR_ID` 和 `CN_JOURNAL_COUNT`
- **完整配置**: 设置所有回退值，确保Google Scholar获取失败时也能正常工作
- `CN_JOURNAL_COUNT` 的值（51）是基于北大核心期刊数，您可以根据实际情况调整

### 自动更新
- Google Scholar数据每天自动更新
- 中文期刊数据需要手动更新（当有新论文时）

