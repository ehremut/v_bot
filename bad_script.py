import vk_api
import random
import time
from vk_api.longpoll import VkLongPoll
import re
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

credentials_file = 'My First Project-9cc0f18cb40c.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    credentials_file, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
client = gspread.authorize(credentials)
list = []
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1pO_Y4qUbYXdG8Z3WMd9LvnUnh6r8xLsiM8F1a2G8BK8/edit#gid=0')
pack = sheet.worksheet("Простые")
data = pack.get_all_values()
# print(type(data[2]))
#print(data)



for i in range(len(data)):
    if re.match(r'ЭПСЧ', data[i][0]) != None:
        theme = {"name": data[i][0],
                 "format": "thbt",
                 "discus": "",
                 "level": "easy",
                 "lang": "ru"}
    elif re.match(r'ЭП как', data[i][0]) != None:
        theme = {"name": data[i][0],
                 "format": "tha",
                 "discus": "",
                 "level": "easy",
                 "lang": "ru"}
    else:
        theme = {"name": data[i][0],
                 "format": "th",
                 "discus": "",
                 "level": "easy",
                 "lang": "ru"}
    list.append(theme)


sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1pO_Y4qUbYXdG8Z3WMd9LvnUnh6r8xLsiM8F1a2G8BK8/edit#gid=0')
pack = sheet.worksheet("Сложные")
data = pack.get_all_values()

for i in range(len(data)):
    if re.match(r'ЭПСЧ', data[i][0]) != None:
        theme = {"name": data[i][0],
                 "format": "thbt",
                 "discus": "",
                 "level": "hard",
                 "lang": "ru"}
    elif re.match(r'ЭП как', data[i][0]) != None:
        theme = {"name": data[i][0],
                 "format": "tha",
                 "discus": "",
                 "level": "hard",
                 "lang": "ru"}
    else:
        theme = {"name": data[i][0],
                 "format": "th",
                 "discus": "",
                 "level": "hard",
                 "lang": "ru"}
    list.append(theme)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(list, f, ensure_ascii=False, indent=4)
