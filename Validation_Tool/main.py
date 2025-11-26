import qtmax, importlib, sys, os
sys.path.append(os.path.dirname(__file__))
from pymxs import runtime as rt
from model import ValidationVariables
from controller.ValidationController import ValidationController
from model.ValidationUtils import ValidationUtils
from view.ValidationUI import ValidationUI
mods = [controller.ValidationController, model.ValidationUtils, view.ValidationUI, ValidationUtils]
for mod in mods:
    importlib.reload(mod)

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