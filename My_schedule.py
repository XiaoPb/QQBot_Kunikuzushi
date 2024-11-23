# schedule.py
from datetime import datetime

# 定义课程表
schedule = {
    "Monday": {
        "上午": ["前端框架应用"],
        "下午": ["软件工程与UML"],
        "晚上": []
    },
    "Tuesday": {
        "上午": ["网站设计与开发"],
        "下午": ["前端框架应用"],
        "晚上": []
    },
    "Wednesday": {
        "上午": ["交互界面设计"],
        "下午": [],
        "晚上": []
    },
    "Thursday": {
        "上午": ["AI模型训练与部署"],
        "下午": ["线性代数"],
        "晚上": []
    },
    "Friday": {
        "上午": ["数据库技术与应用"],
        "下午": [],
        "晚上": []
    },
    "Saturday": {
        "上午": [],
        "下午": [],
        "晚上": []
    },
    "Sunday": {
        "上午": [],
        "下午": [],
        "晚上": []
    }
}

def get_todays_classes():
    # 获取当前日期和星期几
    now = datetime.now()
    weekday = now.strftime("%A")
    return schedule[weekday]

def display_classes():
    todays_classes = get_todays_classes()
    Reply_schedule_content = ''
    for time_slot, classes in todays_classes.items():
        # print(f"{time_slot}: {', '.join(classes) if classes else '没有课哦！好好休息一下吧喵！（＾・ﻌ・＾✿）'}")
        Reply_schedule_content += f"{time_slot}: {', '.join(classes) if classes else '没有课哦！好好休息一下吧喵！（＾・ﻌ・＾✿）'}\n"
        return Reply_schedule_content

def next_class():
    todays_classes = get_todays_classes()
    current_hour = datetime.now().hour
    next_class = None
    next_class_time = None

    for time_slot, classes in todays_classes.items():
        if classes:
            class_time = time_slot.split("上节")[0]
            if class_time == "晚上" and current_hour < 18:
                continue
            elif class_time == "上午" and current_hour >= 12:
                continue
            elif class_time == "下午" and (current_hour < 12 or current_hour >= 18):
                continue

            if not next_class or (class_time == "上午" and int(time_slot.split("上节")[1]) > current_hour):
                next_class = ', '.join(classes)
                next_class_time = time_slot

    if next_class:
        reply_next_class = ''
        # print(f"下一堂课是：{next_class}，在{next_class_time}捏！̷(̷ ̷=̷🝦 ̷༝̷ ̷🝦 ̷=̷ ̷)̷")
        reply_next_class += f"下一堂课是：{next_class}，在{next_class_time}捏！̷(̷ ̷=̷🝦 ̷༝̷ ̷🝦 ̷=̷ ̷)̷"
        return reply_next_class
    else:
        reply_no_class = ''
        # print("今天已经没有课了，好好休息哦！Zzz(=^–^)｡o○{{ >ﾟ)++++« }}")
        reply_no_class += f"今天已经没有课了，好好休息哦！Zzz(=^–^)｡o○{{ >ﾟ)++++« }}"
        return reply_no_class