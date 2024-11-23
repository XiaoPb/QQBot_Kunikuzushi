import json
import re
import logging

def fix_json_string(message):

    # 确保 message 是字符串
    if not isinstance(message, str):
        message = str(message)  # 转换为字符串

    # 原始字符串
    # print("原始数据：", message)
    try:
        # 替换单引号为双引号，同时保留嵌套结构
        fixed_message = re.sub(r"(?<!\\)'", '"', message)  # 替换未转义的单引号
        fixed_message = re.sub(r'None', 'null', fixed_message)  # 替换 None 为 null
        fixed_message = re.sub(r'\"{', '{', fixed_message)  # 修复多余的引号
        fixed_message = re.sub(r'}\"', '}', fixed_message)  # 修复多余的引号

        # 检查修复后的字符串
        # print("修复后的 JSON 字符串：", fixed_message)

        # 加载 JSON
        message_dict = json.loads(fixed_message)

        # 提取 content
        message_content = message_dict.get("content", "内容不存在")

    except json.JSONDecodeError as e:
        logging.error(f"JSON 解析错误：{e}")
    except Exception as e:
        logging.error(f"提取消息时发生错误：{e}")

    return message_content
