from models.constants import ConfigKeys
from zipfile import ZipFile, ZIP_DEFLATED
from services.drop_scanner import DropScanner
from services.config_manager import ConfigManager
from pathlib import Path
import shutil

class FamasOptimizer:
    def __init__(self, drop_scanner: DropScanner, config_manager: ConfigManager):
        self.drop_scanner = drop_scanner
        self.source_folder = Path(config_manager.get(ConfigKeys.SOURCE_FOLDER))
        self.desination_folder = Path(config_manager.get(ConfigKeys.DESTINATION_FOLDER))
        self.archive_folder = Path(config_manager.get(ConfigKeys.ARCHIVE_FOLDER))
        #self.test_desination_folder = Path(r"C:/Users/dat.nguyen_b/Desktop/Test/TEST_DESTINATION")
        self.output_folder = Path(config_manager.get(ConfigKeys.OUTPUT_FOLDER))
        #self.output_folder = Path(r"C:/Users/dat.nguyen_b/Desktop/Test/DESTINATION")
        #self.database_folder = Path(r"C:/Users/dat.nguyen_b/Desktop/Test/SOURCE")
        self.database_folder = Path(config_manager.get(ConfigKeys.DATABASE_FOLDER))

    def optimize_car_list(self) -> list[str]:
        source_drop, destination_drop = self.drop_scanner.check_drop_difference(self.source_folder, self.desination_folder)
        result = []
        if source_drop <= destination_drop:
            return result
        car_list = self.get_car_list(destination_drop,source_drop)
        for car_drop, cars in car_list.items():
            output = Path(self.output_folder/ f"Drop_{car_drop}.zip")
            if self.zip_cars(cars,self.database_folder,output):         
                self.delete_original_files(cars, self.database_folder)
                self.delete_excel_file(car_drop)
            result.append(car_drop)
        return result

    def get_car_list(self,start:int,end:int):
        car_list = {}
        for i in range(start, end):
            cars = self.drop_scanner.get_drop_car_list(i,self.archive_folder)
            car_list[i] = cars
        return car_list
    def check_zip_file(self, car_drops: list, folder_path: Path) -> set[str]:
        already_zip = {}
        for f in folder_path.iterdir():
            if f.is_file():
                pass
      
    def zip_cars(self, car_list: list[str], database_folder: Path, output: Path) -> None:
        try:
            files_added = False
            with ZipFile(output, "w",ZIP_DEFLATED) as zip_file:
                for car_name in car_list:
                    car_folder = database_folder / car_name
                    if not car_folder.is_dir():
                        continue
                    folder_arcname = car_folder.relative_to(database_folder).as_posix() + "/"
                    zip_file.writestr(folder_arcname,"")
                    files_added = True
                    for file in car_folder.rglob("*"):
                        if file.is_file():
                            zip_file.write(
                                file,
                                arcname= file.relative_to(database_folder)
                            )
                            files_added = True
            if not files_added:
                output.unlink(missing_ok=True)
                return False
            return True
        except Exception as e:
            print("Cannot zip these cars:",car_list)
            print("Errors Message: ",e)
            output.unlink(missing_ok=True)
            return False

    def delete_original_files(self,car_list: list[str], database_folder: Path):
        for car in car_list:
            car_folder = database_folder / car
            if not car_folder.is_dir():
                continue
            try:
                shutil.rmtree(car_folder)
                print(f"Deleted Car: {car_folder}")
            except OSError as e:
                print("Cannot delete: ",{e})

    def delete_excel_file(self,car_drop: int):
        file = self.desination_folder / f"Drop_{car_drop}.xlsx"
        if file.is_file():
            file.unlink()
            print(f"Deleted File: {file}")
            

