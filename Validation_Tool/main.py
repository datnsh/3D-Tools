<<<<<<< HEAD
import qtmax, importlib
from controller import ValidationController
from model import ValidationVariables
from view import ValidationUI
from pymxs import runtime as rt
mods = [ValidationController, ValidationVariables, ValidationUI]
for mod in mods:
    importlib.reload(mod)
from controller.ValidationController import ValidationController
from model.ValidationUtils import ValidationUtils
from view.ValidationUI import ValidationUI

=======
import qtmax, importlib, sys, os
from pymxs import runtime as rt
path = os.path.dirname(__file__)
if path not in sys.path:
    sys.path.append(path)
from validation_tool.model import validation_utils as utils
from validation_tool.model import validation_variables as var
from validation_tool.view import validation_ui as ui
from validation_tool.controller import validation_controller as control
mods = [utils, var, ui, control]
for mod in mods:
    importlib.reload(mod)
>>>>>>> b65d765 (Update)
def main():
    mainWindow = qtmax.GetQMaxMainWindow()
    main_ui = ui.ValidationUI(parent=mainWindow)
    util = utils.ValidationUtils()
    controller = control.ValidationController(main_ui,util)
    main_ui.setObjectName(var.TOOL_TITLE)
    main_ui.close_last_instance(mainWindow, var.TOOL_TITLE)
    main_ui.setFloating(True)
    main_ui.show()
if __name__ == "__main__":
    main()