from kivy.uix.checkbox import CheckBox


class PropertyBoxModelCheckBox(CheckBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = (0, 0, 0, 1)
        self.bind(active=self.on_checkbox_active)

    def on_checkbox_active(self, checkbox, value):
        if value:
            if "py" == checkbox.parent.children[1].text:
                if checkbox.parent.parent.children[2].children[0].active:
                    checkbox.parent.parent.children[2].children[0].active = False
            elif checkbox.parent.children[1].text == "kv":
                if checkbox.parent.parent.children[1].children[0].active:
                    checkbox.parent.parent.children[1].children[0].active = False
            if checkbox.parent.children[1].text == "join":
                for index in [1, 2]:
                    checkbox.parent.parent.children[index].children[0].disabled = False
                checkbox.parent.parent.children[2].children[0].active = True
                if checkbox.parent.parent.children[4].children[0].text == "canvas_color":
                    checkbox.parent.parent.parent.parent.parent.parent.parent.parent.add_color_palette_to_page()
        else:
            if checkbox.parent.children[1].text == "join":
                checkbox.parent.parent.children[2].children[0].active = False
                checkbox.parent.parent.children[1].children[0].active = False
                for index in [1, 2]:
                    checkbox.parent.parent.children[index].children[0].disabled = True
                if checkbox.parent.parent.children[4].children[0].text == "canvas_color":
                    checkbox.parent.parent.parent.parent.parent.parent.parent.parent.remover_color_palette_from_page()
