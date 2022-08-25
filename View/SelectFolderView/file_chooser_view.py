from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView
Builder.load_file('SelectFolderView/kv/file_chooser_view.kv')


class FileChooserView(FileChooserIconView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.path = "C:\\Users"

