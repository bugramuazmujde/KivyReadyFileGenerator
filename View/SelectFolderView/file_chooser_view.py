from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView

from Service.path_service import PathService

Builder.load_file('SelectFolderView/kv/file_chooser_view.kv')


class FileChooserView(FileChooserIconView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_path = PathService.read_path_from_txt()
        print(self.default_path)
        if self.default_path:
            self.path = self.default_path
        else:
            self.path = "C:\\Users"

