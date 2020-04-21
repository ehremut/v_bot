from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class Keyboard():
    def create_keyboard(response):
        themes = ['Социальная сфера','Политика','Экономика','Наркотики','Феминизм','Международные отношения',\
                  'Спорт', 'СМИ', 'Мигранты', 'Религия', 'Этика']
        themes_low = ['социальная сфера', 'политика', 'экономика', 'наркотики', 'феминизм', 'международные отношения', \
                      'спорт', 'сми', 'мигранты', 'религия', 'этика']
        keyboard = VkKeyboard(one_time=False)

        if response == 'поехали' or response == 'заново' or response == 'начать' or response == 'start':
            keyboard.add_button('Выбрать тему', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()  # Переход на вторую строку
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)

        elif response == 'выбрать тему':
            keyboard.add_button('Русский', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('Английский', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)

        elif response == 'английский' or response == 'русский':
            keyboard.add_button('Легкая', color=VkKeyboardColor.POSITIVE)
            keyboard.add_button('Сложная', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)

        elif response == 'легкая' or response == 'сложная':
            keyboard.add_button(themes[0], color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button(themes[1], color=VkKeyboardColor.POSITIVE)
            keyboard.add_button(themes[2], color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button(themes[3], color=VkKeyboardColor.POSITIVE)
            keyboard.add_button(themes[4], color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button(themes[5], color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button(themes[6], color=VkKeyboardColor.POSITIVE)
            keyboard.add_button(themes[7], color=VkKeyboardColor.POSITIVE)
            keyboard.add_button(themes[8], color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button(themes[9], color=VkKeyboardColor.POSITIVE)
            keyboard.add_button(themes[10], color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)



        elif response in themes_low: # было социалочка
            keyboard.add_button('ЭП', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('ЭПСЧ', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('ЭП как', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)


        elif response == 'случайная тема' or response == 'эп' or response == 'эпсч' or response == 'эп как':
            keyboard.add_button('Заново', color=VkKeyboardColor.POSITIVE)

        keyboard = keyboard.get_keyboard()
        return keyboard
