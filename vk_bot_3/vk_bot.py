from pymongo import MongoClient
import random
from datetime import datetime
random.seed(datetime.now())

class VkBot():

    def __init__(self, user_id, send, steps):
        print("Создан объект бота!")
        self.user_id = user_id
        self.send = send
        self.STEPS = steps

    def get_step(self): # возвращать словарь из previos now next и использовать для случайно
        if self.STEPS['1'] == False:
            return '1'
        if self.STEPS['1'] == True and self.STEPS['2'] == False:
            return '2'
        if self.STEPS['1'] == True and self.STEPS['2'] == True and self.STEPS['3'] == False:
            return '3'
        if self.STEPS['1'] == True and self.STEPS['2'] == True and self.STEPS['3'] == True and self.STEPS['4'] == False:
            return '4'
        if self.STEPS['1'] == True and self.STEPS['2'] == True and self.STEPS['3'] == True and self.STEPS['4'] == True and \
                self.STEPS['5'] == False:
            return '5'
    

    def get_random(self, part, ch_list, step):
        self.send[part] = random.choice(ch_list)
        self.STEPS[str(step)] = True


    def message(self,response,keyboard):

        STEP_1 = ['хочу подборку', 'выбрать тему', 'случайно']
        STEP_2 = ['русский', 'английский', 'случайно', 'назад']
        STEP_3 = ['легкая', 'сложная', 'случайно', 'назад']
        STEP_4 = ['социальная сфера', 'политика', 'экономика', 'наркотики', 'феминизм', 'международные отношения',
                  'спорт', 'сми', 'мигранты', 'религия', 'этика', 'случайно', 'назад']
        STEP_5 = ['эп', 'эпсч', 'эп как', 'случайно', 'назад']
        sys_words = ['старт','поехали', 'заново', 'начать']
        list_lang = ['ru', 'en']
        list_level = ['easy', 'hard']
        list_discus = ['soc', 'polit', 'econ', 'narco', 'fem', 'inter', 'sport', 'media', 'migr', 'relig', 'ethics']
        list_format = ['th', 'thbt', 'tha']

        youtube_mess = 'Для чего нужны дебаты\nhttps://vk.com/video-64852945_456239685?list=6edc3a9c9e4f180ab8' \
                       '\n\nРечь финалиста чемпионата мира по дебатам\n' \
                       'https://www.youtube.com/watch?v=K45gUjK3OIc&feature=youtu.be&ab_channel=RussianSchoolsDebateNetwork\n' \
                       '\n\nВидео, на котором наглядно видно, насколько можно прокачаться в дебатах:\n' \
                       'https://vk.com/video76208855_456239030\n' \
                       '\n\nИстория успеха дебатера и тренера по дебатам: как дебаты помогли ему выйти за грани возможного\n' \
                       'https://www.youtube.com/watch?v=ejlg4Cfgeso&feature=youtu.be&ab_channel=TEDxTalks\n' \
                       '\n\nЧто общего у дебатов и Гарри Поттера?\n' \
                       'https://www.youtube.com/watch?v=BBuVAs0s--I&feature=youtu.be&ab_channel=TEDxTalks\n' \
                       '\n\nКак дебаты могут изменить Вашу жизнь\n' \
                       'https://www.youtube.com/watch?v=WJaMtU1P-3w&feature=youtu.be&ab_channel=TEDxTalks\n'

        if response in sys_words:
            self.clear()
            return ('user_id', self.user_id, 'Хочешь сам выбрать или доверишься мне?', keyboard)

        elif response in STEP_1 and self.get_step() == '1':
            i = STEP_1.index(response)
            if i == 0:
                return ( 'user_id', self.user_id, youtube_mess, keyboard)
            if i == 1:
                self.STEPS['1'] = True
                return( 'user_id', self.user_id,'Выбери язык', keyboard)
            post = ('user_id', self.user_id, self.get_theme(self.send, 0), keyboard)
            self.clear()
            return post

        elif response in STEP_2 and self.get_step() == '2':
            self.STEPS['2'] = True
            i = STEP_2.index(response)
            if i < 2:
                self.send['lang'] = list_lang[i]
            elif i == 2:
                self.send['lang'] = random.choice(list_lang)
            elif i == 3:
                self.send['lang'] == ''
                self.STEPS['1'] = False
                self.STEPS['2'] = False
                return ('user_id', self.user_id, 'Хочешь сам выбрать или доверишься мне?', keyboard)
            return self.check('2', 'lang', 'Выбери сложность', keyboard)


        elif response in STEP_3 and self.get_step() == '3':
            self.STEPS['3'] = True
            i = STEP_3.index(response)
            if i < 2:
                self.send['level'] = list_level[i]
            elif i == 2:
                self.send['level'] = random.choice(list_level)
            elif i == 3:
                self.send['level'] == ''
                self.STEPS['2'] = False
                self.STEPS['3'] = False
                return ('user_id', self.user_id, 'Выбери язык', keyboard)
            return self.check('3', 'level', 'Выбери сферу', keyboard)


        elif response in STEP_4  and self.get_step() == '4':
            self.STEPS['4'] = True
            i = STEP_4.index(response)
            if i < 11:
                self.send['discus'] = list_discus[i]
            elif i == 11:
                self.send['discus'] = random.choice(list_discus)
            elif i == 12:
                self.send['discus'] == ''
                self.STEPS['3'] = False
                self.STEPS['4'] = False
                return ('user_id', self.user_id, 'Выбери сложность', keyboard)
            return self.check('4', 'discus', 'Выбери формат', keyboard)



        elif response in STEP_5 and self.get_step() == '5':
            self.STEPS['5'] = True
            i = STEP_5.index(response)
            if i < 3:
                self.send['format'] = list_format[i]
            elif i == 3:
                self.send['format'] = random.choice(list_format)
            elif i == 4:
                self.send['format'] == ''
                self.STEPS['4'] = False
                self.STEPS['5'] = False
                return ('user_id', self.user_id, 'Выбери сферу', keyboard)
            return self.check('5', 'format', self.get_theme(self.send, 0), keyboard)



    def check(self, step, type, text, keyboard):
        if self.get_theme(self.send, 1) == False:
            self.STEPS[str(step)] = False
            self.send[type] = ''
            return ('user_id', self.user_id, 'Таких тем нет')
        elif step == '5':
            self.clear()
            return ('user_id', self.user_id, self.get_theme(self.send, 0), keyboard)
        else:
            return ('user_id', self.user_id, text, keyboard)

    def clear(self):
        self.send = {'lang': '', 'level': '', 'format': '', 'discus': ''}
        self.STEPS = {'1': False, '2': False, '3': False, '4': False, '5': False}

    def get_theme(self, send, mode):
        client = MongoClient("mongodb://user1:password@10.128.0.2:27017")
        db = client.dbThemes
        col = db.data
        ss = {}
        t_list = []
        res = 0
        for i in send.items():
            if i[1] != '':
                ss[i[0]] = i[1]
        print(ss)
        col = col.find(ss)
        for i in col:
            t_list.append(i['name'])
        if mode == 0:
            if len(t_list) != 0:
                res = random.choice(t_list)
            else:
                res = 'К сожалению таких тем нет'
        if mode == 1:
            if len(t_list) != 0:
                res = True
            else:
                res = False
        return res
