from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from View.GeneratorView.BottomView.property_box_parent_grid import PropertyBoxParentGrid
Builder.load_file("GeneratorView/BottomView/kv/select_widget_properties_box.kv")


class SelectWidgetPropertiesBox(BoxLayout):
    def __init__(self, properties, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(PropertyBoxParentGrid(properties))
