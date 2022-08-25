from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
Builder.load_file("SelectFolderView/kv/lower_bar.kv")


class LowerBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.select_folder_button = Button(text="Choose Folder", size_hint=(.3, 1))
        self.select_folder_button.bind(on_press=self.select_folder)
        self.add_widget(Label())
        self.add_widget(self.select_folder_button)

    def select_folder(self, value):
        selected_path = self.parent.children[1].path
        self.parent.parent.change_view(selected_path)
