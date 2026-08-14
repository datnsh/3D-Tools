import openpyxl
from pathlib import Path

class ExcelExporter():
    def __init__(self, destination_folder: str, headers: dict):
        self.destination_folder = Path(destination_folder) # Where to save the updated data
        self.default_header = headers # Header for generated .xlsx files

    def export_drop(self, drop_name: str, car_list: list[str]):
        try:
            file_path = self.destination_folder / f"{drop_name}.xlsx"
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            for cell, value in self.default_header.items():
                sheet[cell] = value
            index = 1
            for car in car_list:
                sheet.append([index, car])
                index += 1
            workbook.save(file_path)
            print("File saved at:", file_path)
        except Exception as e:
            print(e)