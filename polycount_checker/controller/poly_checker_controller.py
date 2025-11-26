import sys, os, importlib, qtmax
path = os.path.dirname(__file__)
if path not in sys.path:
    sys.path.append(path)
import view.poly_checker_ui as poly_checker_ui_m
import model.poly_checker_variables as poly_checker_variables
import model.poly_checker_utils as poly_checker_utils
mods = [poly_checker_ui_m,poly_checker_utils, poly_checker_variables]
for mod in mods:
    importlib.reload(mod)
from view.poly_checker_ui import PolyCheckerUI
from model.poly_checker_utils import PolyUtil


class PolyController():
    def __init__(self):
        mainWindow = qtmax.GetQMaxMainWindow()
        PolyController.instance = self
        self.ui = PolyCheckerUI(parent=mainWindow)
        self.ui.closeLastInstance(mainWindow, poly_checker_variables.UINAME)
        self.ui.setFloating(True)
        self.ui.setObjectName(poly_checker_variables.UINAME)
        self.ui.show()
        self.util = PolyUtil()
        self.ui.checkBtn.clicked.connect(self.onCheckBtnClicked)
    def formatKey(self,keyValue = int()):
        return poly_checker_variables.INVERSELOD[keyValue]
    def onCheckBtnClicked(self):
        self.ui.checkTable.setRowCount(0)
        self.util.resetPolyCount()
        self.util.checkPolycount()
        for key, value in self.util.polyDict.items():
            self.ui.addTableItem(self.formatKey(key), str(value), 'OK')