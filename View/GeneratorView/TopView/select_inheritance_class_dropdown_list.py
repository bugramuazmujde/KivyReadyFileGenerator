from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from Service.inheritance_and_property_service import InheritanceAndPropertyService

Builder.load_file("GeneratorView/TopView/kv/select_inheritance_class_dropdown_list.kv")


class SelectInheritanceClassDropdownList(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_inheritance_buttons_to_widget()
        self.max_height = 150

    def add_inheritance_buttons_to_widget(self):
        inheritance_instance = InheritanceAndPropertyService()
        for wid in inheritance_instance.inheritance_classes:
            btn = Button(text=wid, size_hint_y=None, height=44)
            btn.background_color = (4 / 255, 157 / 255, 191 / 255, 1)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            btn.bind(on_press=self.pressed)
            self.add_widget(btn)

    def pressed(self, value):
        inheritance_instance = InheritanceAndPropertyService()
        value.parent.parent.parent.children[1].children[0].children[1].add_select_widget_properties_box_to_widget(
            inheritance_instance.get_properties(value.text)
        )