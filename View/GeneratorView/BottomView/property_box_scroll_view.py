from kivy.uix.scrollview import ScrollView
from View.GeneratorView.BottomView.property_box_bucket import PropertyBoxBucket


class PropertyBoxScrollView(ScrollView):
    def __init__(self, properties, **kwargs):
        super().__init__(**kwargs)
        self.bucket = PropertyBoxBucket(properties)
        self.bucket.bind(minimum_height=self.bucket.setter('height'))
        self.add_widget(self.bucket)
