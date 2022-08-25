from Model.kivy_ready_file_model import KivyReadyFileModel
from Service.kivy_ready_file_service import KivyReadyFileService


class KivyReadyFileViewModel:
    def __init__(self, file_path, file_name, inheritance_class, property_dict, build):
        self.kfr_model = KivyReadyFileModel(file_path, file_name, inheritance_class, property_dict)
        self.run_kivy_file_ready_service(build)

    def run_kivy_file_ready_service(self, build):
        KivyReadyFileService(self.kfr_model, build)

