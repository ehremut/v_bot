from pymongo import MongoClient
import random
from datetime import datetime
random.seed(datetime.now())


class VkBot():

    def __init__(self, user_id):
        print("Создан объект бота!")
        self.user_id = user_id
        self.send = {'lang': '', 'level': '', 'format': '', 'discus': ''}
        self.steps = {1: False, 2: False, 3: False, 4: False, 5: False}

    def message(self,response,keyboard):
        if response == "поехали" or response == "заново":
            self.send = {'lang': '', 'level': '', 'format': '', 'discus': ''}
            self.steps = {1: False, 2: False, 3: False, 4: False, 5: False}
            return [ 'user_id', self.user_id, 'Хочешь сам выбрать или доверишься мне?', keyboard]

        elif response == "выбрать тему":
            if self.steps[1] == False:
                self.steps[1] = True
                return( 'user_id', self.user_id,'Выбери язык', keyboard)
            else:
                return( 'user_id', self.user_id,'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')

        elif response == "случайная тема":
            return( 'user_id', self.user_id, self.get_theme(self.send), keyboard)

        elif response == 'русский':
            if self.steps[1] == True and self.steps[2] == False:
                self.steps[2] = True
                self.send['lang'] = 'ru'
                return( 'user_id', self.user_id, 'Выбери сложность', keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')

        elif response == 'английский':
            if self.steps[1] == True and self.steps[2] == False:
                self.steps[2] = True
                self.send['lang'] = 'en'
                return( 'user_id', self.user_id, 'Выбери сложность', keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')

        elif response == 'легкая':
            if self.steps[1] == True and self.steps[2] == True and self.steps[3] == False:
                self.steps[3] = True
                self.send['level'] = 'easy'
                return( 'user_id', self.user_id, 'Выбери сферу', keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')

        elif response == 'сложная':
            if self.steps[1] == True and self.steps[2] == True and self.steps[3] == False:
                self.steps[3] = True
                self.send['level'] = 'hard'
                return( 'user_id', self.user_id, 'Выбери сферу', keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')
        elif response == 'жми далее братишка':  # было "социалочка"
            if self.steps[1] == True and self.steps[2] == True and self.steps[3] == True and self.steps[4] == False:
                self.steps[4] = True
                # здесь будет добавление в словарь тэга "сфера дискуссии"
                return( 'user_id', self.user_id, 'Выбери формат', keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')
        elif response == 'эп':
            if self.steps[1] == True and self.steps[2] == True and self.steps[3] == True and \
                    self.steps[4] == True and self.steps[5] == False:
                self.steps[5] = True
                self.send['format'] = 'th'
                return( 'user_id', self.user_id, self.get_theme(self.send), keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')
        elif response == 'эпсч':
            if self.steps[1] == True and self.steps[2] == True and self.steps[3] == True and \
                    self.steps[4] == True and self.steps[5] == False:
                self.steps[5] = True
                self.send['format'] = 'thbt'
                return( 'user_id', self.user_id, self.get_theme(self.send), keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')
        elif response == 'эп как':
            if self.steps[1] == True and self.steps[2] == True and self.steps[3] == True and \
                    self.steps[4] == True and self.steps[5] == False:
                self.steps[5] = True
                self.send['format'] = 'tha'
                return( 'user_id', self.user_id, self.get_theme(self.send), keyboard)
            else:
                return( 'user_id', self.user_id, 'Много просить нельзя, у тебя же есть кнопочки, \
                                                            пользуйся\nЕсли хочешь начать заново, то напиши заново')
        else:
            return ('user_id', self.user_id, 'Мне нечего тебе на это ответить\n \
                                             Пользуйся кнопочками, они для тебя\n \
                                            Если хочешь начать заново, то напиши поехали')

    def get_theme(self, send):
        client = MongoClient("mongodb://127.0.0.1:27017")
        db = client.dbThemes
        col = db.data
        ss = {}
        t_list = []
        for i in send.items():
            if i[1] != '':
                ss[i[0]] = i[1]
        col = col.find(ss)
        for i in col:
            t_list.append(i['name'])
        if len(list) != 0:
            res = random.choice(t_list)
        else:
            res = 'К сожалению таких тем нет'
        return res
