from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from age_picker.age_picker import AgePicker
from kivy.lang import Builder
from language import tr, set_language

Builder.load_file("age_picker/age_picker.kv")
Builder.load_file("language.kv")
Builder.load_file("gender.kv")
Builder.load_file("age.kv")
Builder.load_file("menu.kv")
Builder.load_file("camera.kv")
Builder.load_file("profile.kv")
Builder.load_file("anthropometry.kv")


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

        self.picker = []
        self.ids.progress_bar.value = 50  # от 100 процентв
        weight_picker = AgePicker(fl="int", min_value = 0, max_value = 100)
        self.ids.box.add_widget(weight_picker)
        self.picker.append(weight_picker)
        self.picker[0].size_hint = None, None
        self.picker[0].size = "50dp", "250dp"
        self.picker[0].pos_hint =  {"center_x": 0.5, "center_y": 0.5}

class Anthropometry(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def unit_button(self):
        if self.ids.unit1.text == "кг":
            self.ids.unit1.text = "lb"
        else:
            self.ids.unit1.text = "кг"

    def unit_button2(self):
        if self.ids.unit2.text == "см":
            self.ids.unit2.text = "in"
        else:
            self.ids.unit2.text = "см"


    def on_kv_post(self, base_widget):
        self.picker = []
        self.ids.progress_bar.value = 100  # от 100 процентв
        weight_picker = AgePicker(fl="int", min_value = 0, max_value = 200)
        self.ids.box.add_widget(weight_picker)
        self.picker.append(weight_picker)
        self.picker[0].size_hint = None, None
        self.picker[0].size = "50dp", "250dp"
        self.picker[0].pos_hint =  {"center_x": 0.3, "center_y": 0.5}

        heigth_picker = AgePicker(fl = "int", min_value = 0, max_value = 215)
        self.ids.box.add_widget(heigth_picker)
        self.picker.append(heigth_picker)
        self.picker[1].size_hint = None, None
        self.picker[1].size = "50dp", "250dp"
        self.picker[1].pos_hint =  {"center_x": 0.7, "center_y": 0.5}











class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Camera(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Profile(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Language(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.picker = []
        language_pickcer = AgePicker(fl="string", text_list = [
            "English",  "France", "Germany", "Italian", "Russian"
        ])
        self.ids.lng.add_widget(language_pickcer)
        self.picker.append(language_pickcer)
        self.picker[0].size_hint = None, None
        self.picker[0].size = "250dp", "250dp"
        self.picker[0].pos_hint =  {"center_x": 0.5, "center_y": 0.5}

    def select_language(self, lang_code):
        set_language(lang_code)



class FitApp(MDApp):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Language(name='language'))
        sm.add_widget(Gender(name='gender'))
        sm.add_widget(Age(name='age'))
        sm.add_widget(Anthropometry(name='anthropometry'))
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Camera(name='camera'))
        sm.add_widget(Profile(name='profile'))
        return sm

    def translate(self, key):
        return tr(key)


if __name__ == "__main__":
    FitApp().run()
