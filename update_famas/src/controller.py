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
    