# XAI Chatbot

🤖 A simple chatbot script built on the XAI API. This chatbot allows interactive conversations and logs chat sessions to a local file. Each session is timestamped and clearly distinguishes messages between the user and the chatbot (assistant).

## Features

- **🗣️ Interactive Chat**: Engage in real-time conversations with the chatbot.
- **📜 Conversation Log**: All conversations are saved to a log file with timestamps, clearly separating user and chatbot messages.
- **📚 History Management**: Keeps the latest 30 messages (configurable) to provide context for future conversations.
- **🖥️ Optional Proxy Support**: Allows enabling or disabling proxies as needed.
- **🔑 Environment Variable Management**: Securely loads the API key through a `.env` file.

## Prerequisites

Before running this chatbot, ensure that you meet the following requirements:

- **Python 3.6+**
- **Required Python Libraries**: Install the required libraries using `requirements.txt`.
- **XAI API Key**: You need to obtain an API key from the XAI service and configure it in the `.env` file. You can get the API key at x.ai.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Liu8Can/xai-chatbot.git
   cd xai-chatbot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. 创建 `.env` file in the project root directory and add your XAI API key:

   ```env
   XAI_API_KEY=your_api_key_here
   ```

4. Optionally, you can adjust the proxy settings in the script or the `.env` file.

## Usage

To start the chatbot, run the following command:

```bash
python xai_chatbot.py
```

The chatbot will prompt you for input. Type `"exit"`, `"bye"`, `"quit"`, or other similar commands to end the session. Each conversation will be logged and saved in the `chat_log.txt` file.

## Log Format

The chat logs are stored in the `chat_log.txt` file in the following format:

```
==================================================
New Chat Session: 2024-11-16 10:30:00
==================================================
2024-11-16 10:30:10
User: Hello, GroK!

2024-11-16 10:30:12
Grok: Hello! How can I help you today?
```

Each message is prefixed with a timestamp and the speaker's identifier ("User" or "Grok"), with a separator between each round of conversation.

## Log Management

The project keeps a maximum of **30 messages** to ensure context for each conversation. You can adjust this number as needed.

## Contributing

If you'd like to contribute to this chatbot, feel free to fork the repository and submit a Pull Request. Please make sure to add tests for any new features or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
