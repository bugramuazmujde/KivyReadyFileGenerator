import os
from Service.file_name_parser_service import FileNameParserService


class KivyReadyFileService:
    def __init__(self, kfr_model, build, spaces=4):
        self.kfr_model = kfr_model
        self.py_path = None
        self.kv_path = None
        self.build = build
        self.parser_service = FileNameParserService(self.kfr_model.file_name)
        self.spaces = spaces
        self.generate()
        if self.build:
            self.add_build_class()

    def generate(self):
        self.create_python_file()
        self.create_kv_file()
        self.prepare_ready_file()

    def create_python_file(self):
        if self.build:
            self.py_path = os.path.join(self.kfr_model.file_path, self.parser_service.get_class_name() + "App.py")
        else:
            self.py_path = os.path.join(self.kfr_model.file_path, self.parser_service.get_py_name())
        self.create_file(self.py_path)

    def create_kv_file(self):
        self.kv_path = os.path.join(self.kfr_model.file_path, "kv")
        if not os.path.exists(self.kv_path):
            os.mkdir(self.kv_path)
        self.kv_path = os.path.join(self.kv_path, self.parser_service.get_kv_name())
        self.create_file(self.kv_path)

    @staticmethod
    def create_file(path):
        open(path, "a").close()

    def prepare_ready_file(self):
        self.add_imports_to_py()
        self.add_class_to_files()
        self.add_properties_to_files()

    def add_class_to_files(self):
        self.write_a_line_to_kv(
            "<" + self.parser_service.get_class_name() + ">"
        )
        lines = [
            "class " + self.parser_service.get_class_name() + "(" + self.kfr_model.inheritance_class + "):",
            " " * self.spaces + "def __init__(self, **kwargs):",
            " " * (self.spaces * 2) + "super().__init__(**kwargs)"
        ]
        for line in lines:
            self.write_a_line_to_py(line)

    def add_properties_to_files(self):
        for property_name in self.kfr_model.property_dict:
            if property_name == "canvas_color":
                self.add_canvas_to_kv(self.kfr_model.property_dict[property_name]["kv"])
            else:
                for file_name in self.kfr_model.property_dict[property_name]:
                    if file_name == "kv":
                        self.write_a_line_to_kv(
                            " " * self.spaces + property_name + ": " + self.kfr_model.property_dict[property_name][file_name]
                        )
                    else:
                        self.write_a_line_to_py(
                            " " * (self.spaces * 2) + "self." + property_name + " = " + self.kfr_model.property_dict[
                                property_name
                            ][file_name]
                        )

    def write_a_line_to_py(self, line):
        with open(self.py_path, "a") as py_file:
            py_file.write(line + "\n")

    def write_a_line_to_kv(self, line):
        with open(self.kv_path, "a") as kv_file:
            kv_file.write(line + "\n")

    def add_imports_to_py(self):
        for import_line in self.read_imports():
            if self.kfr_model.inheritance_class in import_line:
                self.write_a_line_to_py(import_line)
            if self.build and "App" in import_line:
                self.write_a_line_to_py(import_line)
            if "Builder" in import_line:
                self.write_a_line_to_py(import_line)
                self.write_a_line_to_py("Builder.load_file(\"" + self.kv_path.replace("\\", "\\\\") + "\")\n\n")

    @staticmethod
    def read_imports():
        f = open('../Service/from_file_import_class.txt', "r")
        imports = f.read().split("\n")
        f.close()
        return imports

    def add_build_class(self):
        build_lines = [
            "\nclass " + self.parser_service.get_class_name() + "App" + "(App):",
            " " * self.spaces + "def __init__(self, **kwargs):",
            " " * (self.spaces * 2) + "super().__init__(**kwargs)\n",
            " " * self.spaces + "def build(self):",
            " " * (self.spaces * 2) + "return " + self.parser_service.get_class_name() + "()\n\n",
            "if __name__ == \"__main__\":",
            " " * self.spaces + self.parser_service.get_class_name() + "App()" + ".run()"
        ]
        for line in build_lines:
            self.write_a_line_to_py(line)

    def add_canvas_to_kv(self, value):
        lines = [
            " " * self.spaces + "canvas.before:",
            " " * (self.spaces * 2) + "Color:",
            " " * (self.spaces * 3) + "rgba: " + value,
            " " * (self.spaces * 2) + "Rectangle:",
            " " * (self.spaces * 3) + "size: self.size",
            " " * (self.spaces * 3) + "pos: self.pos"
        ]
        for line in lines:
            self.write_a_line_to_kv(line)
