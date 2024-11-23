import json
import re
import logging

logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)

# 原始字符串
message = "{'author': \"{'user_openid': 'C2203C841BB94DA52F2B0B1E107BA136'}\", 'content': '你是？', 'id': 'ROBOT1.0_fNZ1moyeJas2ScqkAeR0t3SJ3nBDv-VFlFIjZ5bVnBYZOe3yT2w-5yCu26DjtWwm6YeecpntncZY4eA.MKOvGw!!', 'message_reference': \"{'message_id': None}\", 'mentions': '[]', 'attachments': '[]', 'msg_seq': 'None', 'timestamp': '2024-11-23T15:44:55+08:00', 'event_id': 'C2C_MESSAGE_CREATE:ehha3yonskofkv4dgapqzcemqq2nhu4l2zqrkjgp6zfuohchhcigml0xmisoz2'}"

try:
    # 替换单引号为双引号，同时保留嵌套结构
    fixed_message = re.sub(r"(?<!\\)'", '"', message)  # 替换未转义的单引号
    fixed_message = re.sub(r'None', 'null', fixed_message)  # 替换 None 为 null
    fixed_message = re.sub(r'\"{', '{', fixed_message)  # 修复多余的引号
    fixed_message = re.sub(r'}\"', '}', fixed_message)  # 修复多余的引号

    # 检查修复后的字符串
    print("修复后的 JSON 字符串：", fixed_message)

    # 加载 JSON
    message_dict = json.loads(fixed_message)

    # 提取 content
    message_content = message_dict.get("content", "内容不存在")
    _log.info(f"用户：{message_content}")
    print(message_content)

except json.JSONDecodeError as e:
    logging.error(f"JSON 解析错误：{e}")
except Exception as e:
    logging.error(f"提取消息时发生错误：{e}")
