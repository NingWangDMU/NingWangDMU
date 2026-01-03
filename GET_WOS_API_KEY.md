# 获取Web of Science API密钥指南

## 📋 概述

Web of Science API密钥通过 **Clarivate Developer Portal** 获取。请注意，API访问通常需要：
- 机构订阅Web of Science数据库
- 开发者账号注册和审批
- 可能需要机构管理员批准

## 🚀 获取步骤

### 步骤1: 访问Clarivate Developer Portal

1. 打开浏览器，访问：
   ```
   https://developer.clarivate.com/
   ```

2. 点击页面右上角的 **"Sign In"** 或 **"Register"** 按钮

### 步骤2: 注册/登录开发者账号

**如果您是新用户**：
1. 点击 **"Register"** 或 **"Create Account"**
2. 填写注册信息：
   - 邮箱地址（建议使用机构邮箱）
   - 密码
   - 姓名
   - 机构名称
   - 其他必要信息
3. 验证邮箱并完成注册

**如果您已有账号**：
1. 点击 **"Sign In"**
2. 使用您的邮箱和密码登录

### 步骤3: 申请Web of Science API访问权限

1. **登录后，进入API产品页面**：
   - 在开发者门户首页，找到 **"APIs"** 或 **"Products"** 菜单
   - 搜索或选择 **"Web of Science API"** 或 **"WOS API"**

2. **查看API详情**：
   - 阅读API文档和使用说明
   - 了解API的限制和配额
   - 查看定价信息（如果有）

3. **申请API密钥**：
   - 点击 **"Get API Key"** 或 **"Request Access"** 按钮
   - 填写申请表单，包括：
     - 使用目的
     - 预期使用量
     - 机构信息
     - 联系信息

### 步骤4: 等待审批

1. **提交申请后**：
   - 您会收到确认邮件
   - Clarivate团队会审核您的申请
   - 审批时间通常为几个工作日到几周不等

2. **审批通过后**：
   - 您会收到通知邮件
   - 登录开发者门户
   - 在 **"My APIs"** 或 **"API Keys"** 页面查看您的API密钥

### 步骤5: 获取API密钥

1. **登录Clarivate Developer Portal**
2. **导航到API密钥页面**：
   - 点击右上角头像/用户名
   - 选择 **"My APIs"** 或 **"API Keys"**
   - 或直接访问：`https://developer.clarivate.com/apis`
3. **找到Web of Science API**：
   - 在API列表中找到 **"Web of Science API"**
   - 点击查看详情
4. **复制API密钥**：
   - 找到 **"API Key"** 或 **"Key"** 字段
   - 点击 **"Show"** 或 **"Reveal"** 按钮（如果密钥被隐藏）
   - 复制完整的API密钥字符串

### 步骤6: 在GitHub Secrets中设置

1. **进入GitHub仓库**：
   - 打开您的GitHub仓库
   - 点击 **Settings** > **Secrets and variables** > **Actions**

2. **添加API密钥**：
   - 点击 **"New repository secret"**
   - Name: `WOS_API_KEY`
   - Value: 粘贴您刚才复制的API密钥
   - 点击 **"Add secret"**

3. **（可选）添加作者标识**：
   - `WOS_RESEARCHER_ID`: 您的Web of Science ResearcherID（推荐）
   - `WOS_ORCID`: 您的ORCID ID
   - `WOS_AUTHOR_NAME`: 您的姓名

## ⚠️ 重要注意事项

### 1. 机构订阅要求

- Web of Science API通常需要您的机构订阅Web of Science数据库
- 如果您是个人用户，可能需要：
  - 联系机构图书馆或IT部门
  - 确认机构是否有Web of Science订阅
  - 可能需要机构管理员协助申请

### 2. API限制和配额

- 大多数API都有使用限制（如每天/每月的请求次数）
- 请查看API文档了解具体的配额限制
- 超出配额可能导致API调用失败

### 3. API版本

- Web of Science可能有多个API版本（如WOS API v1, v2等）
- 请确认您使用的是哪个版本的API
- 不同版本的端点和参数可能不同

### 4. 安全注意事项

- **永远不要**将API密钥提交到代码仓库
- 只通过GitHub Secrets存储API密钥
- 如果API密钥泄露，立即在开发者门户中撤销并重新生成

## 🔍 替代方案

如果您无法获取API密钥，或者审批流程较长，您可以：

1. **使用手动设置方式**（推荐）：
   - 直接在GitHub Secrets中设置指标值
   - 无需API密钥，更简单快捷
   - 参考 `QUICK_START_WOS.md` 了解详细步骤

2. **联系机构支持**：
   - 联系您所在机构的图书馆
   - 询问是否有现成的API密钥可以使用
   - 或请求协助申请API访问权限

## 📚 相关资源

- **Clarivate Developer Portal**: https://developer.clarivate.com/
- **Web of Science API文档**: https://developer.clarivate.com/apis/wos
- **API支持**: 通过开发者门户的联系页面获取支持

## ❓ 常见问题

**Q: 申请API密钥需要多长时间？**  
A: 通常需要几个工作日到几周，具体取决于Clarivate的审批流程。

**Q: 个人用户可以申请API密钥吗？**  
A: 通常需要机构订阅。个人用户可能需要联系机构或使用手动设置方式。

**Q: API密钥有使用限制吗？**  
A: 是的，大多数API都有配额限制。请查看API文档了解具体限制。

**Q: 如果API密钥泄露怎么办？**  
A: 立即登录开发者门户，撤销旧密钥并生成新密钥。

**Q: 我可以使用多个API密钥吗？**  
A: 取决于您的订阅计划。请查看API文档或联系支持了解详情。

## 🎯 下一步

获取API密钥后：

1. 在GitHub Secrets中设置 `WOS_API_KEY`
2. （可选）设置 `WOS_RESEARCHER_ID`、`WOS_ORCID` 或 `WOS_AUTHOR_NAME`
3. 手动触发GitHub Actions工作流测试
4. 检查日志确认API调用是否成功

如果API调用失败，系统会自动回退到环境变量方式，使用您手动设置的指标值。

