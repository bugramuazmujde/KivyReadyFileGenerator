from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from View.SelectFolderView.driver_buttons import DriverButtons
from View.SelectFolderView.file_chooser_view import FileChooserView
from View.SelectFolderView.lower_bar import LowerBar

Builder.load_file('SelectFolderView/kv/file_chooser.kv')


class FileChooser(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(DriverButtons())
        self.add_widget(FileChooserView())
        self.add_widget(LowerBar())


