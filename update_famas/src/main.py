import sys

from PySide6.QtWidgets import QApplication
<<<<<<< HEAD
from controller import Controller

def main():
    app = QApplication(sys.argv)
    
    controller = Controller()
    controller.show()
=======

from controller import UpdateFamas
from gui import MainWindow
def main():
    app = QApplication(sys.argv)

    controller = UpdateFamas()
    controller.update_car_list()
    created_files = controller.add_files()

    main_window = MainWindow(created_files)
    main_window.show()
>>>>>>> cbf5847fa3b92d49fcf12231e752d6e203f690d5

    sys.exit(app.exec())


if __name__ == "__main__":
    main()