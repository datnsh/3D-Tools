import sys, os, importlib
path = os.path.dirname(__file__)
if path not in sys.path:
    sys.path.append(path)
import controller.poly_checker_controller as poly_checker_controller
importlib.reload(poly_checker_controller)
from controller.poly_checker_controller import PolyController

def main():
    controller = PolyController()
if __name__ == "__main__":
    main()