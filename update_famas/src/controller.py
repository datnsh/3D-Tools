import constants,re
from importlib import reload
from pathlib import Path
from openpyxl import Workbook
import json
reload(constants)

class UpdateFamas():

    def __init__(self):
        self.cars_list = {}
        self.created_files = []
        self.source_folder = constants.SOURCE_FOLDER # Where to get the data
        self.destination_folder = constants.DESTIONATION_FOLDER # Where to save the updated data
        self.default_header = constants.DEFAULT_HEADER
        self.check_drop()

    def check_drop(self):
        newest_item = max(self.source_folder.iterdir(), key=lambda item : item.stat().st_birthtime,default=None)
        newest_item_des = max(self.destination_folder.iterdir(), key=lambda item: item.stat().st_birthtime,default=None)
        if(newest_item.name == newest_item_des.stem):
            self.latest_drop = self.get_latest_drop(newest_item)
            self.last_updated_drop = self.get_latest_drop(newest_item_des)
            print("Already at newest drop: ",self.last_updated_drop)
        else:
            self.latest_drop = self.get_latest_drop(newest_item)
            self.last_updated_drop = self.get_latest_drop(newest_item_des)
            self.update_config(constants.LATEST_DROP,self.latest_drop)
            print("Update config:",self.last_updated_drop)
            self.update_config(constants.LAST_UPDATED_DROP, self.last_updated_drop)

    def update_config(self, key : str, value : any):
        with open("../assets/config.json","r") as f:
            config = json.load(f)
        config[key] = value
        with open("../assets/config.json","w") as f:
            json.dump(config,f,indent=4)

    def get_latest_drop(self, item : Path):
        number = 0
        match = re.search(r"(\d+)$",item.stem)
        if match:
            number = int(match.group())
        return number
    
    def update_car_list(self):
        for i in range(self.last_updated_drop + 1, self.latest_drop + 1):
            drop_name = "Drop_" + str(i)
            drop_path = self.source_folder / drop_name
            self.cars_list[drop_name] = []
            for folder in drop_path.iterdir():
                if "feature" in folder.name.lower() or "update" in folder.name.lower():
                    for inner in folder.iterdir():
                        self.cars_list[drop_name].append(inner.name)
                else:
                    self.cars_list[drop_name].append(folder.name)

    def add_files(self):
        for drop, car_list in self.cars_list.items():
            file_path = self.destination_folder / f"{drop}.xlsx"
            workbook = Workbook()
            sheet = workbook.active
            for cell, value in self.default_header.items():
                sheet[cell] = value
            index = 1
            for car in car_list:
                sheet.append([index,car])
                index += 1
            workbook.save(file_path)
            self.created_files.append(file_path)
            print("File saved at:", file_path)
        return self.created_files
    