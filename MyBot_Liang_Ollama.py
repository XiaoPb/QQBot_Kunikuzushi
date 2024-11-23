import json
from io import BytesIO

import pycurl

from MyBot_load_character_building_message import build_character_message, load_character

def input_User_Text(user_input_text, url="http://localhost:3000/api/chat/completions"):

    # 读取角色信息
    character, personality = load_character()
    system_message = build_character_message(character, personality)

    # 构建 API 请求数据
    data = {
        "model": "llama3.1:latest",
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input_text}
        ]
    }

    # 转换为 JSON 格式
    json_data = json.dumps(data)

    # 初始化 pycurl
    buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, url)
    curl.setopt(curl.HTTPHEADER, [
        # f"Authorization: Bearer {api_key}",
        f"Authorization: Bearer sk-c71ec38edb844c1c84522b3101b4dd01",
        "Content-Type: application/json"
    ])
    curl.setopt(curl.POST, 1)
    curl.setopt(curl.POSTFIELDS, json_data)
    curl.setopt(curl.WRITEFUNCTION, buffer.write)

    # 执行请求
    try:
        curl.perform()
        response = buffer.getvalue().decode("utf-8")
        buffer.close()
        curl.close()
    except pycurl.error as e:
        print(f"Curl error: {e}")
        return "无法连接到 API，请检查设置哦。可能是大模型还没有打开哦"

    # 解析响应
    try:
        response_dict = json.loads(response)
        answer_content = response_dict['choices'][0]['message']['content']
        return answer_content
        # return response_dict
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        print(f"解析响应时出错: {e}")
        return "API 返回的响应无法解析，请检查日志。"

# 单独测试ai
if __name__ == "__main__":
    api_key = "sk-c71ec38edb844c1c84522b3101b4dd01"  # 替换为实际 API 密钥
    user_input = "你多少岁了"
    response = input_User_Text(user_input, api_key)
    print("AI 回复:", response)

