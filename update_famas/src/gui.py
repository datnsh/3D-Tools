from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, created_files=None):
        super().__init__()
        self.setWindowTitle("Update FAMAS Car List")
        self.resize(800, 600)
        self.created_files = created_files or []
        self.setup_ui()
        self.show_created_files()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.status_label = QLabel("Created files:")
        layout.addWidget(self.status_label)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.show_created_files)
        layout.addWidget(self.refresh_button)

    def show_created_files(self):
        self.result_list.clear()
        if not self.created_files:
            self.result_list.addItem("No files were created.")
            return
        for file_path in self.created_files:
            self.result_list.addItem(str(file_path))
