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

def main():
    mainWindow = qtmax.GetQMaxMainWindow()
    ui = ValidationUI(parent=mainWindow)
    util = ValidationUtils()
    controller = ValidationController(ui,util)
    ui.setObjectName(ValidationVariables.TOOL_TITLE)
    ui.closeLastInstance(mainWindow, ValidationVariables.TOOL_TITLE)
    ui.setFloating(True)
    ui.show()

if __name__ == "__main__":
    main()