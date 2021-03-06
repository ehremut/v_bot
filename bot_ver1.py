import vk_api
import random
import time
from vk_api.longpoll import VkLongPoll
import gspread
from oauth2client.service_account import ServiceAccountCredentials

credentials_file = '' # generate from google api
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    credentials_file, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
client = gspread.authorize(credentials)


vk = vk_api.VkApi(token=" ") # get from Vk public
vk._auth_token()
vk.get_api()
longpoll = VkLongPoll(vk)

def get_theme(type):
    sheet = client.open_by_url(
        'https://docs.google.com/spreadsheets/d/1pO_Y4qUbYXdG8Z3WMd9LvnUnh6r8xLsiM8F1a2G8BK8/edit#gid=0')
    if type == "easy":
        pack = sheet.worksheet("Простые")
        data = pack.get_all_values()
        return data[random.randint(1, len(data) - 1)]
    if type == "hard":
        pack = sheet.worksheet("Сложные")
        data = pack.get_all_values()
        return data[random.randint(1, len(data) - 1)]

easy_list = ['простая тема', 'легкая тема', 'лёгкая тема', 'дай простую тему',
             'дай легкую тему', 'дай лёгкую тему', 'скажи простую тему', 'скажи легкую тему', 'скажи лёгкую тему']

hard_list = ['сложная тема', 'тяжелая тема', 'тяжёлая тема', 'трудная тема', 'дай сложную тему', 'дай тяжелую тему', 
'дай тяжёлую тему', 'дай трудную тему', 'скажи сложную тему', 'скажи тяжелую тему', 'скажи тяжёлую тему', 'скажи трудную тему']

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() in easy_list:
                vk.method("messages.send", {"peer_id": id, "message": get_theme("easy"), "random_id": random.randint(1, 2147483647)})
            elif body.lower() in hard_list:
                vk.method("messages.send", {"peer_id": id, "message": get_theme("hard"), "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
