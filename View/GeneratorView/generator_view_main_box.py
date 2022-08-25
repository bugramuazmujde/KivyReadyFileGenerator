from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.GeneratorView.BottomBar.bottom_bar import BottomBar
from View.GeneratorView.BottomView.bottom_box import BottomBox
from View.GeneratorView.TopView.top_box import TopBox
Builder.load_file("GeneratorView/kv/generator_view_main_box.kv")


class GeneratorViewMainBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TopBox())
        self.add_widget(BottomBox())
        self.add_widget(BottomBar())
