import os
if os.name == "nt":
    import win32api
    drivers = win32api.GetLogicalDriveStrings()
    drivers = drivers.split('\000')[:-1]
elif os.name == "posix":
    drivers = ["/"]
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
Builder.load_file("SelectFolderView/kv/driver_buttons.kv")


class DriverButtons(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_driver_buttons_to_widget()

    def add_driver_buttons_to_widget(self):
        for driver in drivers:
            driver_btn = Button(text=driver[0], font_size="30sp")
            driver_btn.bind(on_press=self.get_driver_name)
            self.add_widget(driver_btn)

    def get_driver_name(self, value):
        if os.name == "nt":
            if value.text == "C":
                self.parent.children[1].path = "C:\\Users"
            else:
                self.parent.children[1].path = value.text + ":"
        else:
            self.parent.children[1].path = value.text
