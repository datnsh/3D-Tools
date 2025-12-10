import sys, os, importlib, qtmax
path = os.path.dirname(__file__)
if path not in sys.path:
    sys.path.append(path)
import view.poly_checker_ui as poly_checker_ui
import model.poly_checker_variables as poly_checker_variables
import model.poly_checker_utils as poly_checker_utils
mods = [poly_checker_ui,poly_checker_utils, poly_checker_variables]
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
        self.setFileType()
        self.ui.checkBtn.clicked.connect(self.onCheckBtnClicked)
        self.ui.clearBtn.clicked.connect(self.clearCheckTable)
    
    def setFileType(self):
        self.util.fileType = self.util.getFileType()
        self.ui.radioGroup.button(self.util.fileType).setChecked(True)
    def clearCheckTable(self):
        self.setFileType()
        self.ui.checkTable.setRowCount(0)
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
        self.clearCheckTable()
        self.util.resetPolyCount()
        self.util.sortObjects()
        self.util.getPolycount()
        #checkedBtnId = self.ui.radioGroup.checkedId()
        self.util.checkPolycount()
        for k, v in self.util.checkResults.items():
            self.ui.addTableItem(k, str(v[0]), v[1])
            row = self.ui.checkTable.rowCount() - 1

            statusItem = self.ui.checkTable.item(row, 2)
            color = self.getItemColor(v[1])
            self.ui.setItemColor(statusItem ,color)
        if(len(self.util.invalidObjectList) > 0):
            msg = "These objects have no LODs:\n"
            for obj in self.util.invalidObjectList:
                msg += f"obj.name\n"
            rt.messageBox(msg)