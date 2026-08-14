from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
<<<<<<< HEAD
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
=======

class MainWindow(QMainWindow):
    def __init__(self, created_files=None):
        super().__init__()
        self.setWindowTitle("Update FAMAS Car List")
        self.resize(800, 600)
        self.created_files = created_files or []
        self.setup_ui()
        self.show_created_files()
>>>>>>> cbf5847fa3b92d49fcf12231e752d6e203f690d5

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.status_label = QLabel("Created files:")
        layout.addWidget(self.status_label)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

<<<<<<< HEAD
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
=======
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.show_created_files)
        layout.addWidget(self.refresh_button)

    def show_created_files(self):
        self.result_list.clear()
        if not self.created_files:
            self.result_list.addItem("No files were created.")
            return
        for file_path in self.created_files:
>>>>>>> cbf5847fa3b92d49fcf12231e752d6e203f690d5
            self.result_list.addItem(str(file_path))
