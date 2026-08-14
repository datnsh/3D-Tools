import sys

from PySide6.QtWidgets import QApplication
from controller import Controller

def main():
    app = QApplication(sys.argv)
    
    controller = Controller()
    controller.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()