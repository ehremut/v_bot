import vk_api
from vk_api.longpoll import VkEventType
import json
import random
import time

from vk_api.longpoll import VkLongPoll

vk = vk_api.VkApi(token="1bca69c30b5794c55ab9b952909d8acf92f106ca6079a3acbf3c9f6554cea23f47b276e53d609101b369a")

vk._auth_token()

vk.get_api()

easy_theme=["ЭП","ЭПСЧ","ЭПСЧ как","ЭП сожалеет","ЭП откажет"]

hard_theme=["ЭП","ЭПСЧ","ЭПСЧ как","ЭП сожалеет","ЭП откажет"]

def get_button(text,label,payload=""): #
    return{
        "action" : text,
        "payload" : json.dumps(payload),
        "label": label
    }
keyboard = {
    "one_time" : False,
    "buttons" : [
        [get_button("Легкая тема", "green")],
        [get_button("Сложная тема", "green")]
    ]

}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

longpoll = VkLongPoll(vk)

def get_theme(type):
    if type == "easy":
        return easy_theme[random.randint(1,len(easy_theme)-1)]
    if type == "hard":
        return hard_theme[random.randint(1,len(hard_theme)-1)]



# while True:
#     for event in longpoll.listen():
#         if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#             if event.text.lower() == "легкая тема":
#                 vk.method("messages.send", {"peer_id": event.peer_id, "message": get_theme("easy"), "random_id": 12341234})
#             if event.text.lower() == "тяжелая тема":
#                 vk.method("messages.send",
#                           {"peer_id": event.peer_id, "message": get_theme("hard"), "random_id": 12341234})

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "легкая тема":
                vk.method("messages.send", {"peer_id": id, "message": get_theme("easy"), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "тяжелая тема":
                vk.method("messages.send", {"peer_id": id, "message": get_theme("hard"), "random_id": random.randint(1, 2147483647)})

            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)