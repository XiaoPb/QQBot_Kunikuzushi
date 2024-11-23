<div align="center">
  <a href="你的项目语言链接">
    <img src="https://img.shields.io/badge/language-python-green.svg?style=plastic" alt="项目语言">
  </a>
  <img src="https://img.shields.io/badge/python-312-blue" alt="Python版本">


  <p>✨ 一个普通的项目 ✨</p>


  <a href="你的文档链接">文档</a>
  ·
  <a href="你的下载链接">下载</a>
  
</div>

# QQ机器人连接Ollama本地大模型适配器
请配合OpenWebUi使用

[Ollama GitHub](https://github.com/ollama/ollama)
[OpenWebUi](https://github.com/open-webui/open-webui)
[qqbotoy](https://github.com/tencent-connect/botpy)

## 准备工作
请确保你已经安装了`ollama`和`openwebui`。

## 配置机器人信息
在`config.yaml`文件中，添加你的机器人的`appid`和`secret`：
```yaml
appid: "xxxx"
secret: "xxxx"
```
## 修改模型配置


找到MyBot_Kunikuzushi_Ollama.py文件，修改以下部分：

找到这行代码，修改里面的url为你的openwebui的链接，一般来说不用改
``` python
def input_User_Text(user_input_text, url="http://localhost:3000/api/chat/completions"):
```

``` python
# 构建 API 请求数据
data = {
    "model": "llama3.1:latest",  # 修改为你的模型名称
    "messages": [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input_text}
    ]
}
```
将model的值从llama3.1:latest改为你自己的模型名称。

## 更新API密钥
继续往下找到以下代码，将Authorization后面的
值xxxxxxxxxxxxx改成你的openwebui提供的API
密钥，注意保留Bearer关键词：
``` python
curl.setopt(curl.HTTPHEADER, [
    # f"Authorization: Bearer {api_key}",
    f"Authorization: Bearer xxxxxxxxxxxxx",
    "Content-Type: application/json"
])
```
## 修改AI角色
你可以在ai_character.yaml文件中修改AI要扮演的角色。

## 项目状态
这个项目目前还在更新中，还有很多功能没有实现。请保持关注，以便获取最新更新和功能。
