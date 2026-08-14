from services.drop_scanner import DropScanner
from services.excel_exporter import ExcelExporter
from services.config_manager import ConfigManager
from models.constants import ConfigKeys
from pathlib import Path
class FamasUpdater():
    def __init__(self, config_manager: ConfigManager, drop_scanner : DropScanner, excel_exporter: ExcelExporter):
        self.drop_scanner = drop_scanner
        self.excel_exporter = excel_exporter
        self.source_folder = Path(config_manager.get(ConfigKeys.SOURCE_FOLDER))
        self.destination_folder = Path(config_manager.get(ConfigKeys.DESTINATION_FOLDER))

    def update_car_list(self) -> list[str]:
        new_drop, added_drop = self.drop_scanner.check_drop(self.source_folder, self.destination_folder)
        result = []
        if(new_drop != added_drop):
            for i in range(added_drop + 1, new_drop + 1):
                drop_name = "Drop_" + str(i)
                car_list = self.drop_scanner.get_drop_car_list(i, self.source_folder)
                print(f"Exporting {drop_name} with {len(car_list)} cars to Excel.")
                self.excel_exporter.export_drop(drop_name, car_list)
                result.append(f"{drop_name}.xlsx")
        return result
        