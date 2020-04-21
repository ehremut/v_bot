from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
from keyboard import Keyboard
from vk_bot import VkBot
import random


vk = vk_api.VkApi(token="") #токен паблика/группы
vk._auth_token()
vk.get_api()
longpoll = VkLongPoll(vk)

users_bot = {}

def send_message(vk, id_type, id, message=None, keyboard=None):
    vk.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483647, 2147483647), 'keyboard': keyboard})

def get_name(id):
    user = vk.method("users.get", {"user_ids": id}) 
    fullname = user[0]['first_name'] + ' ' + user[0]['last_name']
    return fullname

def run():
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                print('\n'+get_name(event.user_id) + ' (id: ' + str(event.user_id) + ')')
                print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
                print('Текст сообщения: ' + str(event.text))
                print("---------------------------------\n")
                response = event.text.lower()
                keyboard = Keyboard.create_keyboard(response)

                if event.from_user and event.to_me:
                    if event.user_id not in users_bot:
                        users_bot[event.user_id] = VkBot(event.user_id)
                    bb = users_bot[event.user_id].message(response, keyboard)
                    print(users_bot[event.user_id].send)
                    print(users_bot[event.user_id].steps)
                    if len(bb) == 4 :
                        send_message(vk,bb[0], bb[1],message=bb[2], keyboard=bb[3])
                    elif len(bb) == 3:
                        send_message(vk, bb[0], bb[1], message=bb[2])
    except Exception as E:
        time.sleep(3)

