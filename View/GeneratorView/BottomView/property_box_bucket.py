from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from View.GeneratorView.BottomView.PropertyBoxView.property_box import PropertyBox
Builder.load_file("GeneratorView/BottomView/kv/property_box_bucket.kv")


class PropertyBoxBucket(GridLayout):
    def __init__(self, properties, **kwargs):
        super().__init__(**kwargs)
        self.add_property_box_to_widget(properties)

    def add_property_box_to_widget(self, properties):
        for widget in properties:
            self.add_widget(PropertyBox(widget))

