<<<<<<< HEAD
from gui import MainWindow
from ui_components.loading_dialog import LoadingDialog
from services.worker import Worker
from services.config_manager import ConfigManager
from services.famas_updater import FamasUpdater
from services.famas_optimizer import FamasOptimizer
from services.excel_exporter import ExcelExporter
from services.drop_scanner import DropScanner
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
from models.constants import Excel, ConfigKeys

class Controller(QObject):
    files_updated = Signal(list)  # Signal to notify when files are updated
    files_optimized = Signal(list)  # Signal to notify when files are optimized

    def __init__(self):
        super().__init__()
        
        self.config_manager = ConfigManager()
        self.excel_exporter = ExcelExporter(
            self.config_manager.get(ConfigKeys.DESTINATION_FOLDER),
            Excel.HEADERS
        )
        self.drop_scanner = DropScanner(self.config_manager)

        self.famas_updater = FamasUpdater(self.config_manager,self.drop_scanner,self.excel_exporter)
        self.famas_optimizer = FamasOptimizer(self.drop_scanner,self.config_manager)

        self.main_window = MainWindow()
        self.loading_dialog = LoadingDialog(self.main_window)

        self.worker = None

        self.connect_signals()

    def handle_update_requested(self):
        self._run_in_background(
            self.famas_updater.update_car_list,
            message="Updating FAMAS car list...",
            on_success=self.files_updated.emit,
        )

    def handle_optimize_requested(self):
        self._run_in_background(
            self.famas_optimizer.optimize_car_list,
            message="Optimizing FAMAS car list, this can take a while...",
            on_success=self.files_optimized.emit,
        )

    def connect_signals(self):
        self.main_window.update_requested.connect(
            self.handle_update_requested
        )

        self.main_window.optimize_requested.connect(
            self.handle_optimize_requested
        )

        self.files_updated.connect(
            self.main_window.show_created_files
        )
    def _run_in_background(self, task, message: str, on_success):
        self._set_buttons_enabled(False)
        self.loading_dialog.set_message(message)
        self.loading_dialog.show()

        self.worker = Worker(task)
        self.worker.finished_with_result.connect(
            lambda result: self._on_task_finished(result, on_success)
        )
        self.worker.failed.connect(self._on_task_failed)
        self.worker.start()

    def _on_task_finished(self, result, on_success):
        self.loading_dialog.hide()
        self._set_buttons_enabled(True)
        on_success(result)

    def _on_task_failed(self, error_message: str):
        self.loading_dialog.hide()
        self._set_buttons_enabled(True)
        QMessageBox.critical(self.main_window, "Error", error_message)

    def _set_buttons_enabled(self, enabled: bool):
        self.main_window.update_button.setEnabled(enabled)
        self.main_window.optimize_button.setEnabled(enabled)
        self.main_window.refresh_button.setEnabled(enabled)
    
    def show(self):
        self.main_window.show()
=======
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
>>>>>>> cbf5847fa3b92d49fcf12231e752d6e203f690d5
    