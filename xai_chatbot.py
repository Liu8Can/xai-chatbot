import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取API密钥（通过环境变量读取）
api_key = os.getenv("XAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please make sure it's set in the .env file.")

# 设置代理（可选启用）
use_proxy = True
proxies = {
    'http': 'http://127.0.0.1:10101',
    'https': 'http://127.0.0.1:10101'
} if use_proxy else None

# XAI API的URL
url = "https://api.x.ai/v1/chat/completions"

# 请求头部，包含Authorization头
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# 初始化对话历史
messages = [
    {
        "role": "system",
        "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
    }
]

# 动态日志文件路径
log_file = os.path.join(os.path.dirname(__file__), "chat_log.txt")

# 最大消息记录数
MAX_HISTORY = 30


# 保存消息到日志文件
def save_to_log(message, is_new_round=False):
    with open(log_file, "a", encoding="utf-8") as f:
        if is_new_round:
            # 写入分隔线和新轮次时间戳
            f.write("\n" + "=" * 50 + "\n")
            f.write(f"New Chat Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n")
        
        # 获取当前时间戳
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 记录消息及时间戳，并换行
        f.write(f"{timestamp} \n")
        f.write(f"{message}\n\n")  # 增加分隔线
        
# 聊天主逻辑
def chat():
    global messages  # 声明messages为全局变量
    print("你好！我是Grok，一个受《银河系漫游指南》启发的聊天机器人。")
    print(f"当前会话已加载 {len(messages)} 条历史记录。日志将保存到: {log_file}\n")
    save_to_log("", is_new_round=True)  # 添加分隔符，表示新一轮对话

    while True:
        user_input = input("你: ").strip()
        if not user_input:
            print("输入不能为空，请重新输入。")
            continue
        if user_input.lower() in ["退出", "再见", "拜拜", "quit", "exit"]:
            print("再见！期待下次聊天。")
            break

        # 更新消息记录，用户输入
        messages.append({"role": "user", "content": user_input})
        save_to_log(f"User: {user_input}")

        # 控制历史消息数量
        if len(messages) > MAX_HISTORY:
            messages = messages[-MAX_HISTORY:]

        # 请求体数据
        data = {
            "messages": messages,
            "model": "grok-beta",
            "stream": False,
            "temperature": 0
        }

        try:
            # 发送POST请求
            response = requests.post(url, json=data, headers=headers, proxies=proxies)
            response.raise_for_status()  # 检查HTTP请求是否成功

            # 解析响应
            bot_response = response.json()['choices'][0]['message']['content']
            print("\n" + "=" * 50)
            print(f"Grok: {bot_response}")
            print("=" * 50 + "\n")

            # 更新消息记录，机器人回应
            messages.append({"role": "assistant", "content": bot_response})
            save_to_log(f"Grok: {bot_response}")

        except requests.exceptions.RequestException as e:
            print("网络错误:", e)
            save_to_log(f"Error: {e}")
        except KeyError:
            print("响应格式错误，无法获取内容。")
            save_to_log("Error: Invalid response format.")

# 启动对话
if __name__ == "__main__":
    chat()
