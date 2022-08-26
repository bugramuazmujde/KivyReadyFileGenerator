import csv
from csv import DictReader
from os.path import exists
import pandas as pd


class PropertyRowOrganizerService:
    def __init__(self, property_dict, inheritance_class):
        self.property_dict = property_dict
        self.inheritance_class = inheritance_class
        self.property_row_organizer()

    def property_row_organizer(self):
        df = pd.read_csv("../Service/inheritance_and_property.csv")
        new_data = pd.DataFrame({self.inheritance_class: ["canvas_color"]})
        for key in self.property_dict:
            if key != "canvas_color":
                new_data.loc[len(new_data.index)] = [key]
        for index, inheritance_class in enumerate(df[self.inheritance_class]):
            if index != 0 and inheritance_class not in self.property_dict.keys():
                new_data.loc[len(new_data.index)] = [inheritance_class]
        df.drop(self.inheritance_class, inplace=True, axis=1)
        new_data = new_data.join(df)
        new_data.to_csv("../Service/inheritance_and_property.csv", index=False)
