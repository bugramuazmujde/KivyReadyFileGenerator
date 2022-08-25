from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_file("GeneratorView/BottomView/PropertyBoxView/kv/property_box_model_box.kv")


class PropertyBoxModelBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
