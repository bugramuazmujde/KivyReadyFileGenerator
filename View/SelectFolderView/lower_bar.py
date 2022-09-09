from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from Service.path_service import PathService
from View.error_popup import ErrorPopup

Builder.load_file("SelectFolderView/kv/lower_bar.kv")


class LowerBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.select_folder_button = Button(text="Choose Folder", size_hint=(.35, 1))
        self.select_folder_button.bind(on_press=self.select_folder)
        self.create_folder = Label(text="Create Directory", size_hint=(.4, 1))
        self.create_folder_text_input = TextInput(multiline=False, font_size="22sp", size_hint=(.5, 1))
        self.create_folder_text_input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.create_folder)
        self.add_widget(self.create_folder_text_input)
        self.add_widget(Label())
        self.add_widget(self.select_folder_button)

    def select_folder(self, value):
        selected_path = self.parent.children[1].path
        PathService().write_path_to_txt(selected_path)
        self.parent.parent.change_view(selected_path)

    def on_enter(self, value):
        selected_path = self.parent.children[1].path
        create_folder = PathService.create_folder(selected_path, value.text)
        value.text = ""
        self.parent.children[1]._update_files()
        if create_folder:
            ErrorPopup(create_folder).open()
