from PySide2 import QtWidgets, QtGui
from model import poly_checker_variables as pv
import importlib
importlib.reload(pv)

class PolyCheckerUI(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(pv.UINAME)
        widget = QtWidgets.QWidget()
        self.setupUI(widget)
        self.resize(320,300)
        self.retranslateUI()
        self.itemColorDict = pv.ITEMCOLOR
        self.itemStatus = pv.STATUS
    def setupUI(self, widget = QtWidgets.QWidget()):
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.radioGroupLayout = QtWidgets.QHBoxLayout()
        self.stockRadioBtn = QtWidgets.QRadioButton(pv.STOCK)
        self.racerRadioBtn = QtWidgets.QRadioButton(pv.RACER)
        self.interRadioBtn = QtWidgets.QRadioButton(pv.INTERIOR)
        #self.wiperRadioBtn = QtWidgets.QRadioButton("Wipers")
        #self.engineRadioBtn = QtWidgets.QRadioButton("Engine")
        self.rimRadioBtn = QtWidgets.QRadioButton(pv.RIMS)
        self.radioGroup = QtWidgets.QButtonGroup()
        self.radioGroup.addButton(self.stockRadioBtn,0)
        self.radioGroup.addButton(self.racerRadioBtn,1)
        self.radioGroup.addButton(self.interRadioBtn,2)
        #self.radioGroup.addButton(self.wiperRadioBtn,2)
        #self.radioGroup.addButton(self.engineRadioBtn,3)
        self.radioGroup.addButton(self.rimRadioBtn,3) #Change this to 4 or subsequent index if uncomment above buttons
        for btn in self.radioGroup.buttons():
            self.radioGroupLayout.addWidget(btn)
        self.verticalLayout.addLayout(self.radioGroupLayout)
        self.horizontalBtnLayout = QtWidgets.QHBoxLayout()
        self.checkBtn = QtWidgets.QPushButton()
        self.clearBtn = QtWidgets.QPushButton()
        self.horizontalBtnLayout.addWidget(self.checkBtn)
        self.horizontalBtnLayout.addWidget(self.clearBtn)
        self.verticalLayout.addLayout(self.horizontalBtnLayout)

        self.checkTable = QtWidgets.QTableWidget()
        self.checkTable.setColumnCount(3)
        self.checkTable.setHorizontalHeaderLabels(["LOD Name", "Current", "Status"])
        self.checkTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.checkTable.setSortingEnabled(True)
        self.verticalLayout.addWidget(self.checkTable)
        widget.setLayout(self.verticalLayout)
        self.setWidget(widget)

    def retranslateUI(self):
        self.checkBtn.setText("Check polycount")
        self.clearBtn.setText("Clear")
        self.stockRadioBtn.setChecked(True)

    def closeLastInstance(self, mainWindow, widgetName):
        for widget in mainWindow.findChildren(QtWidgets.QDockWidget):
            if widget.objectName() == widgetName:
                widget.close()

    def addTableItem(self, firstCol, secondCol, thirdCol, ):
        row = self.checkTable.rowCount()
        tableFirstCol = QtWidgets.QTableWidgetItem(firstCol)

        tableSecondCol = QtWidgets.QTableWidgetItem(secondCol)
        
        tableThirdCol = QtWidgets.QTableWidgetItem(thirdCol)
        self.checkTable.insertRow(row)
        self.checkTable.setItem(row, 0, tableFirstCol)
        self.checkTable.setItem(row, 1, tableSecondCol)
        self.checkTable.setItem(row, 2, tableThirdCol)

    def getTableItemColor(self,key: int):
        return self.itemColorDict[key]
    
    def setItemColor(self, item: QtWidgets.QTableWidgetItem, color: QtGui.QColor):
        item.setTextColor(color)
        if color != pv.LIGHTGREEN:
            item.setBackgroundColor(self.itemColorDict[3])

    def getStatusMsg(self, statusId: int):
        return self.itemStatus[statusId]
    
    def setStatusMsg(self, item: QtWidgets.QTableWidgetItem, key: int):
        itemText = self.getStatusMsg(key)
        item.setText(itemText)
        
