from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from PySide6.QtCore import Signal
class MainWindow(QMainWindow):
    update_requested = Signal()
    optimize_requested = Signal()
    refresh_requested = Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update FAMAS Car List")
        self.resize(600, 400)
        self.created_files = []
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.status_label = QLabel("Created files:")
        layout.addWidget(self.status_label)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.update_button = QPushButton("Update FAMAS Car List")
        self.update_button.clicked.connect(self.update_requested.emit)
        layout.addWidget(self.update_button)

        self.optimize_button = QPushButton("Optimize FAMAS Car List")
        self.optimize_button.clicked.connect(self.optimize_requested.emit)
        layout.addWidget(self.optimize_button)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_requested.emit)
        layout.addWidget(self.refresh_button)

    def show_created_files(self, created_files: list[str])-> None:
        self.result_list.clear()
        if not created_files:
            self.result_list.addItem("No files were created.")
            return
        for file_path in created_files:
            self.result_list.addItem(str(file_path))
