from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.pagelayout import PageLayout

from View.GeneratorView.BottomView.select_widget_properties_box import SelectWidgetPropertiesBox
Builder.load_file("GeneratorView/BottomView/kv/bottom_box.kv")


class BottomBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rgba = None

    def add_select_widget_properties_box_to_widget(self, properties):
        self.clear_widgets(self.children)
        page_view = PageLayout()
        page_view.border = "40dp"
        page_view.add_widget(SelectWidgetPropertiesBox(properties))
        self.add_widget(page_view)

    def add_color_palette_to_page(self):
        if self.children:
            clr_picker = ColorPicker()
            clr_picker.bind(color=self.on_color)
            self.children[0].add_widget(clr_picker)

    def on_color(self, value, color):
        self.rgba = list(color)

    def remover_color_palette_from_page(self):
        if self.children:
            self.children[0].remove_widget(self.children[0].children[0])
