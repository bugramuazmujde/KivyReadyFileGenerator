from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from View.GeneratorView.BottomView.property_box_scroll_view import PropertyBoxScrollView
Builder.load_file("GeneratorView/BottomView/kv/property_box_parent_grid.kv")


class PropertyBoxParentGrid(GridLayout):
    def __init__(self, properties, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(PropertyBoxScrollView(properties))