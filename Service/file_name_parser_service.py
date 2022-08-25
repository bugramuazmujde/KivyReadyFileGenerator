

class FileNameParserService:
    def __init__(self, file_name):
        self.file_name = file_name
        self.arrange_file_name()

    def arrange_file_name(self):
        if " " in self.file_name:
            self.file_name = self.file_name.replace(" ", "_").split(".")[0]
        arranged_file_name = ""
        for index, char in enumerate(self.file_name):
            if char.isupper() and arranged_file_name == "":
                arranged_file_name += char.lower()
            elif char.isupper():
                if self.file_name[index - 1] == "_":
                    arranged_file_name += char.lower()
                else:
                    arranged_file_name += "_"
                    arranged_file_name += char.lower()
            else:
                arranged_file_name += char
        self.file_name = arranged_file_name

    def get_py_name(self):
        return self.file_name + ".py"

    def get_kv_name(self):
        return self.file_name + ".kv"

    def get_class_name(self):
        class_name = ""
        index = 0
        while index < len(self.file_name):
            if index == 0:
                class_name += self.file_name[index].upper()
            elif self.file_name[index] == "_":
                class_name += self.file_name[index + 1].upper()
                index += 1
            else:
                class_name += self.file_name[index]
            index += 1
        return class_name

