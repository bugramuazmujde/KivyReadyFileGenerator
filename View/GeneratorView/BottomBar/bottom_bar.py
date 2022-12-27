from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from ViewModel.kivy_ready_file_view_model import KivyReadyFileViewModel

Builder.load_file("GeneratorView/BottomBar/kv/bottom_bar.kv")


class BottomBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        build_button = Button(text="BUILD", size_hint=(.3, 1))
        build_button.bind(on_press=self.build)
        generate_button = Button(text="GENERATE", size_hint=(.3, 1))
        generate_button.bind(on_press=self.generate)
        btn = Button(text="BUGRA")
        btn.bind(on_press=self.bugra)
        self.add_widget(build_button)
        self.add_widget(btn)
        self.add_widget(BoxLayout())
        self.add_widget(generate_button)

    def generate(self, value, build=False):
        inheritance_class = self.parent.children[2].children[0].children[0].text
        file_name = self.parent.children[2].children[1].children[0].text
        self.parent.children[2].children[1].children[0].text = ""
        selected_path = self.parent.parent.selected_path
        KivyReadyFileViewModel(selected_path, file_name, inheritance_class, self.get_selected_properties(), build)
        self.parent.children[1].clear_widgets(self.parent.children[1].children)

    def build(self, value):
        self.generate(value, True)

    def get_selected_properties(self):
        selected_properties = {}
        page_index = 0
        if len(self.parent.children[1].children[0].children) > 1:
            page_index = 1
        if self.parent.children[1].children:
            for child in self.parent.children[1].children[0].children[page_index].children[0].children[0].children[0].children:
                if child.children[3].children[0].active:
                    if child.children[2].children[0].active:
                        selected_properties[child.children[4].children[0].text] = {
                            "kv": child.children[0].children[0].text
                        }
                    elif child.children[1].children[0].active:
                        selected_properties[child.children[4].children[0].text] = {
                            "py": child.children[0].children[0].text
                        }
            return selected_properties
        return []

    def bugra(self, value):
        if value.text == "BUGRA":
            print("asdasda")
