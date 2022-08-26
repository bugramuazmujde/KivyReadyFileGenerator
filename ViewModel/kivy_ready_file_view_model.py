from Model.kivy_ready_file_model import KivyReadyFileModel
from Service.kivy_ready_file_service import KivyReadyFileService
from Service.property_row_organizer_service import PropertyRowOrganizerService


class KivyReadyFileViewModel:
    def __init__(self, file_path, file_name, inheritance_class, property_dict, build):
        self.kfr_model = KivyReadyFileModel(file_path, file_name, inheritance_class, property_dict)
        self.run_kivy_file_ready_service(build)
        self.organize_rows()

    def run_kivy_file_ready_service(self, build):
        KivyReadyFileService(self.kfr_model, build)

    def organize_rows(self):
        PropertyRowOrganizerService(self.kfr_model.property_dict, self.kfr_model.inheritance_class)

