from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QWidget, QLabel, QListWidget, QPushButton,
    QProgressBar
)
from PySide6.QtCore import Signal,Qt
class LoadingDialog(QDialog):
    def __init__(self, parent=None, message: str = "Working, please wait.."):
        super().__init__(parent)
        self.setWindowTitle("Please wait")
        self.setModal(True)
        self.setWindowFlags(self.windowFlags())

        self.setFixedSize(320, 100)
        layout = QVBoxLayout(self)
        self.label = QLabel(message)
        layout.addWidget(self.label)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        layout.addWidget(self.progress_bar)

    def set_message(self,message: str) ->None:
        self.label.setText(message)