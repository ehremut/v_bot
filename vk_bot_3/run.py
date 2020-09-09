from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
from keyboard import Keyboard
from vk_bot import VkBot
import random
from pymongo import MongoClient
import json

vk = vk_api.VkApi(
    token="1bca69c30b5794c55ab9b952909d8acf92f106ca6079a3acbf3c9f6554cea23f47b276e53d609101b369a")  # токен паблика/группы
vk._auth_token()
vk.get_api()
longpoll = VkLongPoll(vk)

client = MongoClient("mongodb://user1:password@10.128.0.2:27017")
db = client.dbThemes
col = db.users

users_bot = {}

with open('users.json', 'r') as j:
    try:
        users_json = json.load(j)
        for user in users_json:
            user_data = users_json[user]
            users_bot[int(user)] = {'send': {'lang': user_data['send']['lang'],
                                              'level': user_data['send']['level'],
                                              'format': user_data['send']['format'],
                                              'discus': user_data['send']['discus']},
                                     'steps': {'1': user_data['steps']['1'],
                                               '2': user_data['steps']['2'],
                                               '3': user_data['steps']['3'],
                                               '4': user_data['steps']['4'],
                                               '5': user_data['steps']['5']}}
        j.close()
        print(users_bot)
    except Exception:
        print("empty file")


def send_message(vk, id_type, id, message=None, keyboard=None):
    vk.method('messages.send', {id_type: id, 'message': message, 'random_id': random.randint(-2147483647, 2147483647),
                                'keyboard': keyboard})


def get_name(id):
    user = vk.method("users.get", {"user_ids": id})
    fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
    return fullname


def run():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('\n' + get_name(event.user_id) + ' (id: ' + str(event.user_id) + ')')
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print("---------------------------------\n")
            response = event.text.lower()
            keyboard = Keyboard()
            if event.from_user and event.to_me:
                if found_user(event.user_id) == False:
                    print(event.user_id)
                    print(type(event.user_id))
                    send = {'lang': '',
                            'level': '',
                            'format': '',
                            'discus': ''}
                    steps = {'1': False,
                             '2': False,
                             '3': False,
                             '4': False,
                             '5': False}
                    bot = VkBot(event.user_id, send, steps)
                    add_into_user_bot(event.user_id, send, steps, bot)
                else:
                    if 'vkbot' not in users_bot[event.user_id].keys():
                        user = users_bot[event.user_id]
                        bot = VkBot(event.user_id, user['send'], user['steps'])
                        add_into_user_bot(event.user_id, user['send'], user['steps'], bot)
                bot_Object = users_bot[event.user_id]['vkbot']
                keyboard = keyboard.create_keyboard(response, bot_Object.get_step())
                bb = bot_Object.message(response, keyboard)
                add_into_user_bot(event.user_id, bot_Object.send, bot_Object.STEPS, bot_Object)
                print(bb)
                print(users_bot)
                print(bot_Object.send)
                print(bot_Object.STEPS)
                add_data_in_json(event.user_id)
                if bb == None:
                    continue
                elif len(bb) == 4:
                    send_message(vk, bb[0], bb[1], message=bb[2], keyboard=bb[3])
                elif len(bb) == 3:
                    send_message(vk, bb[0], bb[1], message=bb[2])

def found_user(id):
    if id in users_bot:
        return True
    else:
        return False

def add_into_user_bot(id, send, steps, bot):
    users_bot[id] = {'send': send, 'steps': steps, 'vkbot': bot}


def add_data_in_json(id):
    users_json[str(id)] = {'send': {'lang': users_bot[id]['send']['lang'],
                                     'level': users_bot[id]['send']['level'],
                                     'format': users_bot[id]['send']['format'],
                                     'discus': users_bot[id]['send']['discus']},
                            'steps': {'1': users_bot[id]['steps']['1'],
                                      '2': users_bot[id]['steps']['2'],
                                      '3': users_bot[id]['steps']['3'],
                                      '4': users_bot[id]['steps']['4'],
                                      '5': users_bot[id]['steps']['5']}}
    with open('users.json', 'w') as outfile:
        json.dump(users_json, outfile)
        outfile.close()
