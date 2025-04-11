from kivy.lang import Builder
from kivy.uix.screenmanager import  Screen, ScreenManager
from kivymd.app import MDApp

Builder.load_file("gender.kv")
Builder.load_file("age.kv")
class Gender(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ids.progress_bar.value = 25 #от 100 процентов

    def male_button_press(self):
        self.ids.male.md_bg_color = 0, 0, 0, 1
        self.ids.male.text_color = 1, 1, 1, 1

        self.ids.next.disabled = False
        #dfdff
        self.ids.female.md_bg_color = 0.9, 0.9, 0.9, 1
        self.ids.female.text_color = 0, 0, 0 ,1



    def female_button_press(self):
        self.ids.female.md_bg_color = 0, 0, 0, 1
        self.ids.female.text_color = 1, 1, 1, 1

        self.ids.next.disabled = False

        self.ids.male.md_bg_color = 0.9, 0.9, 0.9, 1
        self.ids.male.text_color = 0, 0, 0, 1

class Age(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ids.progress_bar.value = 40  # от 100 процентов





class FitApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Gender(name='gender'))
        sm.add_widget(Age(name='age'))
        return sm


if __name__=="__main__":
    FitApp().run()
