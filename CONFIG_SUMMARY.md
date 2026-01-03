# 配置摘要 - 数据来源说明

## 📊 数据来源策略

### ✅ 主要数据源：Google Scholar（自动获取）

以下指标**自动从Google Scholar获取**，每天自动更新：

| 指标 | 数据源 | 更新方式 |
|------|--------|----------|
| 国际期刊论文数量 | Google Scholar | 自动 |
| 国际会议论文数量 | Google Scholar | 自动 |
| 总引用数 | Google Scholar | 自动 |
| H-index | Google Scholar | 自动 |
| 书籍/章节（国际） | Google Scholar | 自动 |

### 📝 辅助数据源：百度学术（手动设置）

以下指标**从百度学术获取**，需要手动设置：

| 指标 | 数据源 | 更新方式 |
|------|--------|----------|
| 中文期刊论文数量 | 百度学术 | 手动 |

---

## 🔧 必需配置

### 1. Google Scholar ID（必需）
```
Name: GOOGLE_SCHOLAR_ID
Value: dsK8i4EAAAAJ
```

### 2. 中文期刊论文数量（推荐）
```
Name: CN_JOURNAL_COUNT
Value: 51
说明: 从百度学术获取（北大核心期刊51篇，可根据实际情况调整）
```

---

## ⚪ 可选配置（回退值）

如果担心Google Scholar获取失败，可以设置以下回退值：

```
INT_JOURNAL_COUNT = （留空，Google Scholar会自动获取）
INT_CONF_COUNT = （留空，Google Scholar会自动获取）
BOOK_COUNT = （留空，Google Scholar会自动获取）
TOTAL_CITATIONS = （留空，Google Scholar会自动获取）
H_INDEX = （留空，Google Scholar会自动获取）
```

---

## 📋 最小配置清单

**只需设置2个Secrets即可**：

- [x] `GOOGLE_SCHOLAR_ID` = `dsK8i4EAAAAJ`
- [ ] `CN_JOURNAL_COUNT` = `51`

其他指标会自动从Google Scholar获取！

---

## 🔄 数据更新说明

- **Google Scholar数据**: 每天UTC时间凌晨2点（北京时间上午10点）自动更新
- **中文期刊数据**: 需要手动更新（当有新中文论文时，更新GitHub Secrets中的值）

---

## 💡 配置建议

### 方案A：最小配置（推荐）
- 只设置 `GOOGLE_SCHOLAR_ID` 和 `CN_JOURNAL_COUNT`
- 优点：简单，主要数据自动更新
- 缺点：如果Google Scholar获取失败，会显示"N/A"

### 方案B：完整配置（最稳定）
- 设置所有Secrets（包括回退值）
- 优点：即使Google Scholar获取失败，也能显示数据
- 缺点：需要维护更多值

**建议**: 先使用方案A，如果Google Scholar访问稳定，就不需要设置回退值。

