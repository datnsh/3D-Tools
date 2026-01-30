import sys, os, importlib
from pymxs import runtime as rt
path = os.path.dirname(__file__)
if path not in sys.path:
    sys.path.append(path)
from polycount_checker.controller import poly_checker_controller as poly_checker_controller
from polycount_checker.model import poly_checker_utils as poly_checker_utils
from polycount_checker.model import poly_checker_variables as poly_checker_variables
modules = [poly_checker_utils, poly_checker_controller, poly_checker_variables]
for mod in modules:
    importlib.reload(mod)

def main():
    controller = poly_checker_controller.PolyController()
if __name__ == "__main__":
    main()