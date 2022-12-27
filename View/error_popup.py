from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder
Builder.load_file("C:\\Users\\QueFact\\PycharmProjects\\KivyReadyFileGenerator\\View\\kv\\error_popup.kv")


class ErrorPopup(Popup):
    def __init__(self, error, **kwargs):
        super().__init__(**kwargs)
        self.content = Label(text=error)
