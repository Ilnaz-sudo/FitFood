from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp

# Подгружаем kv файлы
Builder.load_file("gender.kv")
Builder.load_file("age.kv")


# Окно выбора пола
class Gender(Screen):
    # Функция для реализации задач при первом обращении к окну
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.progress_bar.value = 25  # от 100 процентов/устанавливаем значение прогрессбара

    # Меняем цвета кнопки, активируем кнопку Next при нажатии на кнопку
    def male_button_press(self):
        self.ids.male.md_bg_color = 0, 0, 0, 1  # Черный цвет фона кнопки
        self.ids.male.text_color = 1, 1, 1, 1  # Белый цвет текста

        self.ids.next.disabled = False  # Включаем кнопку Next

        self.ids.female.md_bg_color = 0.9, 0.9, 0.9, 1  # Светло серый цвет фона кнопки
        self.ids.female.text_color = 0, 0, 0, 1  # Белый цвет текста

    # Меняем цвета кнопки, активируем кнопку Next при нажатии на кнопку
    def female_button_press(self):
        self.ids.female.md_bg_color = 0, 0, 0, 1  # Черный цвет фона кнопки
        self.ids.female.text_color = 1, 1, 1, 1  # Белый цвет текста

        self.ids.next.disabled = False  # Включаем кнопку Next

        self.ids.male.md_bg_color = 0.9, 0.9, 0.9, 1  # Светло серый цвет фона кнопки
        self.ids.male.text_color = 0, 0, 0, 1   # Белый цвет текста

#Окно выбора возраста
class Age(Screen):
    # Функция для реализации задач при первом обращении к окну
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.progress_bar.value = 40  # от 100 процентов/устанавливаем значение прогрессбара

#Основной класс
class FitApp(MDApp):
    def build(self):
        sm = ScreenManager()    # Позволяет нам переключаться между окнами
        sm.add_widget(Gender(name='gender'))    # Открываем окно gender
        sm.add_widget(Age(name='age'))  # Открываем окно age
        return sm   # Возращаем наши окна

# Основной цикл программы
if __name__ == "__main__":
    FitApp().run()  # Запускаем приложение
