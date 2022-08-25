from csv import DictReader
from os.path import exists


class InheritanceAndPropertyService:
    def __init__(self):
        self.property_csv = self.read_properties_from_csv()
        self.inheritance_classes = self.get_inheritance_classes()

    @staticmethod
    def read_properties_from_csv():
        if not exists("../Service/inheritance_and_property.csv"):
            return {}
        else:
            file_handle = open('../Service/inheritance_and_property.csv', 'r', encoding="utf8")
            return DictReader(file_handle)

    def get_inheritance_classes(self):
        if self.property_csv:
            return self.property_csv.fieldnames
        return []

    def get_properties(self, inheritance_class):
        property_list = []
        for property_name in self.property_csv:
            if property_name[inheritance_class]:
                property_list.append(property_name[inheritance_class])
        return property_list
