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
import model.poly_checker_variables as pv


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
        return self.util.LOD[keyValue]     
    def getItemColor(self, status):
        if(pv.STATUS[0] in status):
            return pv.ITEMCOLOR[0]
        elif(pv.STATUS[1] in status):
            return pv.ITEMCOLOR[1]
        else:
            return pv.ITEMCOLOR[2]
    def onCheckBtnClicked(self):
        self.ui.checkTable.setRowCount(0)
        self.util.resetPolyCount()
        self.util.getPolycount()
        checkedBtnId = self.ui.radioGroup.checkedId()
        self.util.polycountTypeDict = self.util.getPolycountTypeDict(checkedBtnId)
        for k, v in self.util.polyDict.items():
            itemStatus = self.util.checkPolycount(k,v)
            self.ui.addTableItem(k, str(v), itemStatus)
            row = self.ui.checkTable.rowCount() - 1

            statusItem = self.ui.checkTable.item(row, 2)
            color = self.getItemColor(itemStatus)
            self.ui.setItemColor(statusItem ,color)