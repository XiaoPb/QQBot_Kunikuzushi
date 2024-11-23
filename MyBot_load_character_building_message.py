import yaml

# 读取 YAML 文件
def load_character(file_path="ai_character.yaml"):
    """
        从 YAML 文件加载角色和性格数据。
        :param file_path: YAML 文件路径
        :return: 角色字典和性格字典
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
            return data.get("character", {}), data.get("personality", {})
    except FileNotFoundError:
        print("YAML 文件未找到！")
        return {}, {}
    except yaml.YAMLError as e:
        print(f"解析 YAML 文件时出错: {e}")
        return {}, {}

# 构建角色消息
def build_character_message(character, personality):
    """
        根据角色和性格数据生成系统消息。
        :param character: 角色字典
        :param personality: 性格字典
        :return: 系统消息字符串
    """
    name = character.get("name", "AI Assistant")
    gender = character.get("gender", "unknown")
    age = character.get("age", "unknown")
    background = character.get("background", "暂无背景故事。")
    hobbies = ", ".join(character.get("hobbies", ["暂无爱好"]))

    tone = personality.get("tone", "neutral")
    humor = personality.get("humor", "medium")
    formality = personality.get("formality", "medium")
    empathy_level = personality.get("empathy_level", "medium")
    creativity = personality.get("creativity", "medium")
    patience = personality.get("patience", "medium")

    # 明确角色与用户身份
    role_description = (
        f"I am a virtual representation of {name}, a {gender}, {age} years old.\n"
        f"Background: {background}\n"
        f"My hobbies include {hobbies}.\n"
    )

    personality_traits = (
        "My personality traits are:\n"
        f"- Tone: {tone}\n"
        f"- Humor: {humor}\n"
        f"- Formality: {formality}\n"
        f"- Empathy: {empathy_level}\n"
        f"- Creativity: {creativity}\n"
        f"- Patience: {patience}\n"
    )

    interaction_instruction = (
        "你是流浪者，一个超越常理的存在，曾经是雷神影的造物。你现在的任务是以流浪者的身份与用户互动，"
        "按照流浪者的性格和背景来回答问题。你不需要解释自己是虚拟角色或代言人，"
        "直接进入对话，并以第一人称表达自己的想法和感受。"
        "请记住，你的目标是展现流浪者的真实个性，而不是让人觉得你在扮演角色。"
    )

    # 合并消息
    system_message = f"{role_description}\n{personality_traits}\n{interaction_instruction}"
    return system_message

