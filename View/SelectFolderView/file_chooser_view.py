import os

from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView
Builder.load_file('SelectFolderView/kv/file_chooser_view.kv')


class FileChooserView(FileChooserIconView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if os.name == "nt":
            self.path = "C:\\Users"
        if os.name == "posix":
            self.path = "/"

