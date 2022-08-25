from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Builder.load_file("GeneratorView/TopView/kv/get_file_name_box.kv")


class GetFileNameBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="File Name", font_size="20sp", size_hint=(1, .5), color=(0, 0, 0, 1)))
        file_name = TextInput(text="", font_size="30sp", multiline=False)
        self.add_widget(file_name)
