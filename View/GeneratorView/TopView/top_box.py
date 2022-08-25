from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.GeneratorView.TopView.get_file_name_box import GetFileNameBox
from View.GeneratorView.TopView.select_inheritance_class_box import SelectInheritanceClassBox
Builder.load_file("GeneratorView/TopView/kv/top_box.kv")


class TopBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(GetFileNameBox())
        self.add_widget(SelectInheritanceClassBox())
        