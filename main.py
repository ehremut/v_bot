import vk_api
import random
import time
from vk_api.longpoll import VkLongPoll
import gspread
from oauth2client.service_account import ServiceAccountCredentials

credentials_file = 'My First Project-9cc0f18cb40c.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    credentials_file, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
client = gspread.authorize(credentials)


vk = vk_api.VkApi(token="1bca69c30b5794c55ab9b952909d8acf92f106ca6079a3acbf3c9f6554cea23f47b276e53d609101b369a")
vk._auth_token()
vk.get_api()
longpoll = VkLongPoll(vk)

def get_theme(type):
    sheet = client.open_by_url(
        'https://docs.google.com/spreadsheets/d/1XMy-3kcitEFHIYeA0BMgUN_-z-B5YS2-xGjuqVHkYys/edit#gid=0')
    if type == "easy":
        pack = sheet.worksheet("Простые")
        data = pack.get_all_values()
        return data[random.randint(1, len(data) - 1)]
    if type == "hard":
        pack = sheet.get_worksheet("Сложные")
        data = pack.get_all_values()
        return data[random.randint(1, len(data) - 1)]

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
                vk.method("messages.send", {"peer_id": id, "random_id": random.randint(1, 2147483647)}) # "message": "я не знаю что значит " + str(body),
    except Exception as E:
        time.sleep(1)