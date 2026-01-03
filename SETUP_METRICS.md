# 出版物指标自动更新设置指南

本指南将帮助您设置自动更新README.md中的出版物指标。

## 快速开始

### 方法1：使用环境变量（推荐，最简单）

1. **在GitHub仓库中设置Secrets**：
   - 进入仓库 Settings > Secrets and variables > Actions
   - 添加以下Secrets：
     - `INT_JOURNAL_COUNT`: 国际期刊论文数量
     - `CN_JOURNAL_COUNT`: 中文期刊论文数量
     - `INT_CONF_COUNT`: 国际会议论文数量
     - `BOOK_COUNT`: 书籍/章节数量
     - `TOTAL_CITATIONS`: 总引用数
     - `H_INDEX`: H-index

2. **修改GitHub Actions工作流**：
   编辑 `.github/workflows/update-publication-metrics.yml`，将脚本改为使用简化版本：
   ```yaml
   - name: Run update script
     env:
       INT_JOURNAL_COUNT: ${{ secrets.INT_JOURNAL_COUNT }}
       CN_JOURNAL_COUNT: ${{ secrets.CN_JOURNAL_COUNT }}
       INT_CONF_COUNT: ${{ secrets.INT_CONF_COUNT }}
       BOOK_COUNT: ${{ secrets.BOOK_COUNT }}
       TOTAL_CITATIONS: ${{ secrets.TOTAL_CITATIONS }}
       H_INDEX: ${{ secrets.H_INDEX }}
     run: |
       python scripts/update_metrics_simple.py
   ```

3. **手动触发更新**：
   - 在GitHub Actions页面点击"Update Publication Metrics"
   - 选择"Run workflow"

### 方法2：使用Google Scholar自动获取（需要配置）

1. **获取Google Scholar ID**：
   - 访问您的Google Scholar个人主页
   - 从URL中提取ID，例如：`https://scholar.google.com/citations?user=YOUR_ID`
   - `YOUR_ID`就是您需要的ID

2. **在GitHub Secrets中添加**：
   - `GOOGLE_SCHOLAR_ID`: 您的Google Scholar作者ID

3. **注意**：Google Scholar有反爬虫机制，可能需要：
   - 使用代理服务器
   - 降低更新频率
   - 或回退到方法1（手动设置）

### 方法3：使用配置文件

1. **创建配置文件**：
   ```bash
   cp scripts/config.example.json scripts/config.json
   ```

2. **编辑 `scripts/config.json`**：
   ```json
   {
     "manual_metrics": {
       "int_journal_count": 150,
       "cn_journal_count": 20,
       "int_conf_count": 30,
       "book_count": 5,
       "total_citations": 5000,
       "h_index": 45
     }
   }
   ```

3. **注意**：不要将包含真实数据的`config.json`提交到Git仓库（已在.gitignore中）

## 更新频率

默认情况下，GitHub Actions每天UTC时间凌晨2点（北京时间上午10点）自动运行一次。

您可以在 `.github/workflows/update-publication-metrics.yml` 中修改cron表达式来调整更新频率：

```yaml
schedule:
  - cron: '0 2 * * *'  # 每天UTC 2:00
  # - cron: '0 */6 * * *'  # 每6小时
  # - cron: '0 0 * * 0'    # 每周日
```

## 手动更新

如果需要立即更新指标，可以：

1. **通过GitHub Actions**：
   - 进入仓库的Actions页面
   - 选择"Update Publication Metrics"工作流
   - 点击"Run workflow"

2. **本地运行**：
   ```bash
   # 设置环境变量
   export INT_JOURNAL_COUNT=150
   export CN_JOURNAL_COUNT=20
   export TOTAL_CITATIONS=5000
   export H_INDEX=45
   
   # 运行脚本
   python scripts/update_metrics_simple.py
   
   # 提交更改
   git add README.md
   git commit -m "Update publication metrics"
   git push
   ```

## 故障排除

### 问题：指标显示"Loading..."或"N/A"

**原因**：脚本尚未运行或运行失败

**解决方案**：
1. 检查GitHub Actions是否正常运行
2. 查看Actions日志了解错误信息
3. 确保已正确设置Secrets或配置文件

### 问题：Google Scholar数据无法获取

**原因**：Google Scholar的反爬虫机制

**解决方案**：
1. 使用环境变量手动设置指标（方法1）
2. 或使用配置文件（方法3）
3. 考虑使用Google Scholar API（如果可用）

### 问题：CNKI数据无法获取

**原因**：CNKI需要API密钥或特殊访问权限

**解决方案**：
1. 手动设置`CN_JOURNAL_COUNT`环境变量
2. 或使用配置文件设置中文期刊论文数量

## 自定义

### 添加新的指标

1. **在README.md中添加新行**：
   ```markdown
   | **New Metric** | <!-- NEW_METRIC -->0<!-- /NEW_METRIC --> | Source | <!-- LAST_UPDATE -->-<!-- /LAST_UPDATE --> |
   ```

2. **在脚本中添加更新逻辑**：
   编辑`scripts/update_metrics_simple.py`，在`metrics`字典中添加新键

3. **在GitHub Secrets中添加对应的值**

### 修改表格样式

直接编辑README.md中的表格部分，脚本会自动更新注释标记中的值。

## 支持

如有问题，请：
1. 查看`scripts/README.md`获取详细文档
2. 检查GitHub Actions日志
3. 提交Issue到仓库

