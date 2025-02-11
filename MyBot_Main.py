import os
import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message, GroupMessage, C2CMessage
from MyBot_fix_Extend import fix_json_string
from MyBot_Kunikuzushi_Ollama import input_User_Text

test_config = read(os.path.join(os.path.dirname(__file__), "./app/config.yaml"))
_log = logging.get_logger()

async def replay_message(ai_message, use_raw_message, message_type='group'):
    if message_type == 'group':
        messageResult = await use_raw_message._api.post_group_message(
            group_openid=use_raw_message.group_openid,
            msg_type=0,
            msg_id=use_raw_message.id,
            content=f"{ai_message}")
    elif message_type == 'author':
        messageResult2 = await use_raw_message._api.post_c2c_message(
            openid=use_raw_message.author.user_openid,
            msg_type=0,
            msg_id=use_raw_message.id,
            content=f"{ai_message}")
    else:
        raise ValueError("Invalid message type")

    use_message = fix_json_string(use_raw_message)
    _log.info(f"用户：{use_message}")
    _log.info(f"Kunikuzushi：{ai_message}")

async def replay_content(use_input_message, message_type='group'):
    get_ollama_text = input_User_Text(use_input_message.content, url=test_config["open_webui_url"], model_name=test_config["model_name"], api_key=test_config["api_key"])
    await replay_message(get_ollama_text, use_input_message, message_type)

class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot_Kunikuzushi 「{self.robot.name}」 on_ready喵!!!!")

    async def on_c2c_message_create(self, message: C2CMessage):
        await replay_content(message, 'author')

    async def on_group_at_message_create(self, message: GroupMessage):
        await replay_content(message, 'group')


if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True, interaction=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], secret=test_config["secret"])