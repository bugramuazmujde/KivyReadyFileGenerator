from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

from View.GeneratorView.generator_view_main_box import GeneratorViewMainBox
from View.SelectFolderView.file_chooser import FileChooser
Builder.load_file('kv/KFRG.kv')


class KFRG(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(FileChooser())
        self.selected_path = None

    def change_view(self, selected_path=None):
        self.clear_widgets(self.children)
        self.add_widget(GeneratorViewMainBox())
        self.selected_path = selected_path

    def change_view_to_choose(self):
        self.clear_widgets(self.children)
        self.add_widget(FileChooser())


class KFRGApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return KFRG()


if __name__ == "__main__":
    KFRGApp().run()