from kivy.uix.textinput import TextInput


class PropertyBoxModelTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.font_size = "40sp"
