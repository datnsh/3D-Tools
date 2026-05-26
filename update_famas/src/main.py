import sys

from PySide6.QtWidgets import QApplication

from controller import UpdateFamas
from gui import MainWindow
def main():
    app = QApplication(sys.argv)

    controller = UpdateFamas()
    controller.update_car_list()
    created_files = controller.add_files()

    main_window = MainWindow(created_files)
    main_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()