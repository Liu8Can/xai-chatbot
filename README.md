# XAI Chatbot（XAI 聊天机器人）

🤖 一个基于 [XAI API](https://x.ai) 构建的简单聊天机器人脚本。该聊天机器人可以进行交互式对话，并将聊天会话记录到本地文件中。每个会话都带有时间戳，并清晰区分用户和机器人（助手）之间的消息。

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-green)

## 特性

- **🗣️ 交互式聊天**：与聊天机器人进行实时对话。
- **📜 会话日志记录**：所有对话会保存到日志文件中，带有时间戳，并清晰区分用户和机器人消息。
- **📚 历史记录管理**：会保留最新的 30 条消息（可配置），为后续对话提供上下文。
- **🖥️ 可选代理支持**：可以根据需要启用或禁用代理。
- **🔑 环境变量管理**：通过 `.env` 文件安全加载 API 密钥。

## 前置条件

在运行此聊天机器人之前，请确保你具备以下条件：

- **Python 3.6+**
- **所需的 Python 库**：通过 `requirements.txt` 安装所需的库。
- **XAI API 密钥**：需要从 XAI 服务获取 API 密钥，并在 `.env` 文件中进行配置。你可以在 [x.ai](https://x.ai) 申请 API 密钥。

## 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/Liu8Can/xai-chatbot.git
   cd xai-chatbot
   ```

2. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

3. 在项目根目录创建 `.env` 文件，并添加你的 XAI API 密钥：

   ```env
   XAI_API_KEY=your_api_key_here
   ```

4. 如果需要，可以在脚本或 `.env` 文件中调整代理设置。

## 使用

要启动聊天机器人，直接运行以下命令：

```bash
python xai_chatbot.py
```

机器人会提示你输入消息，输入 `"退出"`、`"再见"`、`"拜拜"` 或其他类似命令来结束会话。每次对话都会被记录并保存在 `chat_log.txt` 文件中。

## 日志格式

聊天记录保存在 `chat_log.txt` 文件中，格式如下：

```
==================================================
New Chat Session: 2024-11-16 10:30:00
==================================================
2024-11-16 10:30:10
User: 你好，GroK！

2024-11-16 10:30:12
Grok: 你好！有什么我可以帮忙的吗？
```

每条消息前会带有时间戳和发言者标识（“User” 或 “Grok”），每一轮对话之间会有分隔线。

## 日志管理

项目最多保留最新的 **30 条消息**，以确保每次对话都具有上下文。如果需要，你可以根据需要调整这个数量。

## 贡献

如果你想为这个聊天机器人做贡献，欢迎 Fork 仓库并提交 Pull Request。请确保为任何新特性或修复添加测试。

## 许可证

本项目使用 MIT 许可证 - 请参阅 [LICENSE](LICENSE) 文件了解详情。

