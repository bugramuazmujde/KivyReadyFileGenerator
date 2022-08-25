from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from View.GeneratorView.BottomView.PropertyBoxView.property_box_model_box import PropertyBoxModelBox
from View.GeneratorView.BottomView.PropertyBoxView.property_box_model_check_box import PropertyBoxModelCheckBox
from View.GeneratorView.BottomView.PropertyBoxView.property_box_model_label import PropertyBoxModelLabel
from View.GeneratorView.BottomView.PropertyBoxView.property_box_model_text_input import PropertyBoxModelTextInput

Builder.load_file("GeneratorView/BottomView/PropertyBoxView/kv/property_box.kv")


class PropertyBox(BoxLayout):
    def __init__(self, widget_name, **kwargs):
        super().__init__(**kwargs)
        self.label_texts = ["property", "join", "kv", "py", "value"]
        kv_check = PropertyBoxModelCheckBox()
        kv_check.disabled = True
        py_check = PropertyBoxModelCheckBox()
        py_check.disabled = True
        self.value_classes = [
            PropertyBoxModelLabel(True, widget_name),
            PropertyBoxModelCheckBox(),
            kv_check,
            py_check,
            PropertyBoxModelTextInput()
        ]
        self.add_boxes_to_widgets()

    def add_boxes_to_widgets(self):
        for text, value_class in zip(self.label_texts, self.value_classes):
            box = PropertyBoxModelBox()
            label = PropertyBoxModelLabel()
            label.text = text
            label.size_hint = (1, .3)
            if text == "kv" or text == "py" or text == "join":
                box.size_hint = (.4, 1)
            if text == "value":
                box.size_hint = (1.4, 1)
            box.add_widget(label)
            box.add_widget(value_class)
            self.add_widget(box)

