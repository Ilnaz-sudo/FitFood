from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import PushMatrix, PopMatrix, Scale


class SquishedLabel(Label):
    def __init__(self, scale_y=1.0, **kwargs):
        super().__init__(**kwargs)
        self.scale_y = scale_y
        with self.canvas.before:
            PushMatrix()
            self.scaler = Scale(1, self.scale_y, 1)
        with self.canvas.after:
            PopMatrix()

        self.bind(pos=self.update_scale, size=self.update_scale)

    def update_scale(self, *args):
        self.scaler.origin = self.center

    def set_vertical_scale(self, scale_y):
        self.scale_y = scale_y
        self.scaler.y = scale_y


class AgePicker(BoxLayout):

    fl = StringProperty("int")
    min_value = NumericProperty(0)
    max_value = NumericProperty(100)
    text_list = ListProperty(["", ""])



    def on_kv_post(self, base_widget):
        self.ids.rv.scroll_y = 0.82
        self.label_age()
        self.ids.rv.bind(scroll_y=self.step_scroll)













    def label_age(self):
        self.labels = []

        for _ in range(5):
            lbl = SquishedLabel(text="", size_hint_y=None, height=50, halign='center', color="black")
            self.ids.rv_layout.add_widget(lbl)
        if self.fl == "int":
            for i in range(self.min_value, self.max_value):
                lbl = SquishedLabel(text=str(i), size_hint_y=None, height=50, halign='center', color="black")
                self.ids.rv_layout.add_widget(lbl)
                self.labels.append(lbl)
        if self.fl == "string":
            for i in range(len(self.text_list)):
                lbl = SquishedLabel(text=str(self.text_list[i]), size_hint_y=None, height=50, halign='center', color="black")
                self.ids.rv_layout.add_widget(lbl)
                self.labels.append(lbl)

        for _ in range(5):
            lbl = SquishedLabel(text="", size_hint_y=None, height=50, halign='center', color="black")
            self.ids.rv_layout.add_widget(lbl)

    def step_scroll(self, instance, value):
        layout_height = self.ids.rv_layout.height
        scrollview_height = self.ids.rv.height

        scrolled_pixels = value * (layout_height - scrollview_height)
        step_height = 50
        nearest_step = round(scrolled_pixels / step_height)


        try:
            if self.fl == "int":
                self.age = self.max_value - 1 - nearest_step
                inx = self.max_value - self.min_value
                for i in range(inx):
                    self.labels[i].color = (0, 0, 0, 0.00)
                    self.labels[i].font_size = 32
                    self.labels[i].set_vertical_scale(0.6)

                self.labels[self.age].color = (0, 0, 0, 1)
                self.labels[self.age].font_size = 55
                self.labels[self.age].set_vertical_scale(1)

                for offset, alpha, size, scale in [
                    (1, 0.5, 45, 0.6),
                    (2, 0.3, 30, 0.3),
                    (3, 0.05, 18, 0.2),
                    (4, 0.02, 16, 0.05),
                ]:
                    for sign in (-1, 1):
                        idx = self.age + sign * offset
                        if self.min_value <= idx < self.max_value:
                            self.labels[idx].color = (0, 0, 0, alpha)
                            self.labels[idx].font_size = size
                            self.labels[idx].set_vertical_scale(scale)
            if self.fl == "string":
                self.txt = len(self.text_list) - 1 - nearest_step
                inx = len(self.text_list)
                for i in range(inx):
                    self.labels[i].color = (0, 0, 0, 0.00)
                    self.labels[i].font_size = 32
                    self.labels[i].set_vertical_scale(0.6)
                self.labels[self.txt].color = (0, 0, 0, 1)
                self.labels[self.txt].font_size = 55
                self.labels[self.txt].set_vertical_scale(1)
                for offset, alpha, size, scale in [
                    (1, 0.5, 45, 0.6),
                    (2, 0.3, 30, 0.3),
                    (3, 0.05, 18, 0.2),
                    (4, 0.02, 16, 0.05),
                ]:
                    for sign in (-1, 1):
                        idx = self.txt + sign * offset
                        if 0 <= idx < len(self.text_list):
                            self.labels[idx].color = (0, 0, 0, alpha)
                            self.labels[idx].font_size = size
                            self.labels[idx].set_vertical_scale(scale)

        except:
            pass

        new_scroll_pixel = nearest_step * step_height
        new_scroll_y = new_scroll_pixel / (layout_height - scrollview_height)
        self.ids.rv.scroll_y = new_scroll_y




