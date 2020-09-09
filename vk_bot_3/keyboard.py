from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class Keyboard():

    def n_but(self, keyboard, name, color):
        colors = {'green': VkKeyboardColor.POSITIVE, 'red': VkKeyboardColor.NEGATIVE, 'blue': VkKeyboardColor.PRIMARY,
                  'grey': VkKeyboardColor.DEFAULT}
        keyboard.add_button(name, color=colors[color])


    def create_keyboard(self, response, state):
        state = int(state)
        key_list_1 = ['Хочу подборку','Выбрать тему', 'Случайно']
        key_list_2 = ['Русский', 'Английский', 'Случайно', 'Назад', 'Заново']
        key_list_3 = ['Легкая', 'Сложная', 'Случайно', 'Назад', 'Заново']
        key_list_4 = ['Социальная сфера', 'Политика', 'Экономика', 'Наркотики', 'Феминизм', 'Международные отношения',
                      'Спорт', 'СМИ', 'Мигранты', 'Религия', 'Этика', 'Случайно', 'Назад', 'Заново']
        key_list_5 = ['ЭП', 'ЭПСЧ', 'ЭП как', 'Случайно', 'Назад', 'Заново']

        key_list_1_low = [i.lower() for i in key_list_1]
        key_list_2_low = [i.lower() for i in key_list_2]
        key_list_3_low = [i.lower() for i in key_list_3]
        key_list_4_low = [i.lower() for i in key_list_4]
        key_list_5_low = [i.lower() for i in key_list_5]
        start_list = ['старт','поехали', 'заново', 'начать']

        keyboard = VkKeyboard(one_time=False)
        if response in start_list or (response == key_list_1_low[0] and state == 1) or \
            (response == key_list_1_low[2] and state == 1) or (response in key_list_5_low[0:4] and state == 5) or (response == key_list_2_low[3] and state == 2) :
            self.n_but(keyboard, key_list_1[0], 'blue')
            keyboard.add_line()
            self.n_but(keyboard, key_list_1[1], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_1[2], 'red')

        elif (response in key_list_1_low[1] and state == 1) or (response == key_list_3_low[3] and state == 3): #разобраться со случайно
            self.n_but(keyboard, key_list_2[0], 'green')
            self.n_but(keyboard, key_list_2[1], 'blue')
            keyboard.add_line()
            self.n_but(keyboard, key_list_2[2], 'red')
            keyboard.add_line()
            self.n_but(keyboard, key_list_2[3], 'grey')
            self.n_but(keyboard, key_list_2[4], 'grey')

        elif (response in key_list_2_low and state == 2) or (response == key_list_4_low[12] and state == 4):
            self.n_but(keyboard, key_list_3[0], 'green')
            self.n_but(keyboard, key_list_3[1], 'blue')
            keyboard.add_line()
            self.n_but(keyboard, key_list_3[2], 'red')
            keyboard.add_line()
            self.n_but(keyboard, key_list_3[3], 'grey')
            self.n_but(keyboard, key_list_3[4], 'grey')

        elif (response in key_list_3_low and state == 3) or (response == key_list_5_low[4] and state == 5) :
            self.n_but(keyboard, key_list_4[0], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_4[1], 'green')
            self.n_but(keyboard, key_list_4[2], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_4[3], 'green')
            self.n_but(keyboard, key_list_4[4], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_4[5], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_4[6], 'green')
            self.n_but(keyboard, key_list_4[7], 'green')
            self.n_but(keyboard, key_list_4[8], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_4[9], 'green')
            self.n_but(keyboard, key_list_4[10], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_4[11], 'red')
            keyboard.add_line()
            self.n_but(keyboard, key_list_4[12], 'grey')
            self.n_but(keyboard, key_list_4[13], 'grey')

        elif (response in key_list_4_low and state == 4) : # было социалочка
            self.n_but(keyboard, key_list_5[0], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_5[1], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_5[2], 'green')
            keyboard.add_line()
            self.n_but(keyboard, key_list_5[3], 'red')
            keyboard.add_line()
            self.n_but(keyboard, key_list_5[4], 'grey')
            self.n_but(keyboard, key_list_5[5], 'grey')


        keyboard = keyboard.get_keyboard()
        return keyboard