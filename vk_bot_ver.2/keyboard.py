from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class Keyboard():
    def create_keyboard(response):
        keyboard = VkKeyboard(one_time=False)

        if response == 'поехали' or response == 'заново':
            keyboard.add_button('Выбрать тему', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()  # Переход на вторую строку
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)

        elif response == 'выбрать тему':
            keyboard.add_button('Русский', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('Английский', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)

        elif response == 'английский' or response == 'русский':
            keyboard.add_button('Легкая', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('Сложная', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)

        elif response == 'легкая' or response == 'сложная':
            keyboard.add_button('жми далее братишка', color=VkKeyboardColor.POSITIVE)
            keyboard.add_line()
            keyboard.add_button('Случайная тема', color=VkKeyboardColor.NEGATIVE)

        elif response == 'жми далее братишка': # было социалочка
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
