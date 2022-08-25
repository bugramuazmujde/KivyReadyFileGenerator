from kivy.lang import Builder
from kivy.uix.label import Label
Builder.load_file("GeneratorView/BottomView/PropertyBoxView/kv/property_box_model_label.kv")


class PropertyBoxModelLabel(Label):
    def __init__(self, is_black=None, text=None, **kwargs):
        super().__init__(**kwargs)
        if is_black:
            self.color = (0, 0, 0, 1)
        if text:
            self.text = text


