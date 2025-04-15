from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp


Builder.load_file("gender.kv")
Builder.load_file("age.kv")
Builder.load_file("menu.kv")
Builder.load_file("camera.kv")
Builder.load_file("profile.kv")


class Gender(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.progress_bar.value = 25  # от 100 процентов

    def male_button_press(self):
        self.ids.male.md_bg_color = 0, 0, 0, 1
        self.ids.male.text_color = 1, 1, 1, 1

        self.ids.next.disabled = False

        self.ids.female.md_bg_color = 0.9, 0.9, 0.9, 1
        self.ids.female.text_color = 0, 0, 0, 1

    def female_button_press(self):
        self.ids.female.md_bg_color = 0, 0, 0, 1
        self.ids.female.text_color = 1, 1, 1, 1

        self.ids.next.disabled = False

        self.ids.male.md_bg_color = 0.9, 0.9, 0.9, 1
        self.ids.male.text_color = 0, 0, 0, 1



class Age(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.progress_bar.value = 40  # от 100 процентв






class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Camera(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Profile(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FitApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Gender(name='gender'))
        sm.add_widget(Age(name='age'))
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Camera(name='camera'))
        sm.add_widget(Profile(name='profile'))
        return sm


if __name__ == "__main__":
    FitApp().run()
