import sys, importlib, qtmax, os, pymxs
file_path = os.path.dirname(__file__)
try:
    from config import TOOLS_PATH
except ImportError:
    TOOLS_PATH = ""
paths = [p for p in [file_path, TOOLS_PATH] if p]
for path in paths:
    if path not in sys.path:
        sys.path.append(path)
from PySide2 import QtWidgets, QtCore
from tracking_deco import time_saver

import tool_ui, pivot_operation
imports = [tool_ui, pivot_operation]
for imp in imports:
    importlib.reload(imp)
from tool_ui import Ui_Widget
from pivot_operation import PivotOperation

WINDOWNAME = "PivotPlacer"
class PivotPlacer(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.op = PivotOperation()
        self.ui.copyButton.clicked.connect(self.onCopyButtonClicked)
        self.ui.swapButton.clicked.connect(self.onSwapButtonClicked)
        self.ui.getSourceButton.clicked.connect(self.onGetSourceButtonClicked)
        self.ui.getTargetButton.clicked.connect(self.onGetTargetButtonClicked)
        self.ui.clearButton.clicked.connect(self.onClearButtonClicked)
        
    def closeChildren(main_window, windowName):
        for widget in main_window.findChildren(QtWidgets.QDockWidget):
            if widget.objectName() == windowName:
                widget.close()
    
    def onClearButtonClicked(self):
        self.op.clear_all_list()
        self.ui.sourceTable.clear()
        self.ui.targetTable.clear()
        
    @time_saver(seconds_saved=30.0, tool_name="UbiPivotPlacer")
    def onCopyButtonClicked(self):
        self.op.transfer_pivot()
        
    def onSwapButtonClicked(self):
        tempList = self.op.source_list
        self.op.source_list = self.op.target_list
        self.op.target_list = tempList
        self.updateTable(self.ui.targetTable,self.op.target_list)
        self.updateTable(self.ui.sourceTable, self.op.source_list)
        
    def onGetSourceButtonClicked(self):
        self.op.get_source_objects()
        listTable = self.ui.sourceTable
        objectList = self.op.source_list
        self.updateTable(listTable,objectList)
        
    def onGetTargetButtonClicked(self):
        self.op.get_target_objects()
        listTable = self.ui.targetTable
        objectList = self.op.target_list
        self.updateTable(listTable, objectList)
        
    def updateTable(self, listTable, objectList):
        listTable.clear()
        for obj in objectList:
            item = QtWidgets.QListWidgetItem(obj.name)
            item.setData(QtCore.Qt.UserRole, obj)
            listTable.addItem(item)

    
if __name__ == "__main__":
    main_window = qtmax.GetQMaxMainWindow()
    PivotPlacer.closeChildren(main_window,WINDOWNAME)
    w = PivotPlacer(parent=main_window)
    w.setObjectName(WINDOWNAME)
    w.setFloating(True)
    w.show()