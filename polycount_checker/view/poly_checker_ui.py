from PySide2 import QtCore, QtWidgets, QtGui
from model import poly_checker_variables as pv

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
        self.stockRadioBtn = QtWidgets.QRadioButton("Stock")
        self.racerRadioBtn = QtWidgets.QRadioButton("Racer")
        self.interRadioBtn = QtWidgets.QRadioButton("Interior")
        self.wiperRadioBtn = QtWidgets.QRadioButton("Wipers")
        self.engineRadioBtn = QtWidgets.QRadioButton("Engine")
        self.rimRadioBtn = QtWidgets.QRadioButton("Rims")
        self.radioGroup = QtWidgets.QButtonGroup()
        self.radioGroup.addButton(self.stockRadioBtn,-1)
        self.radioGroup.addButton(self.racerRadioBtn,0)
        self.radioGroup.addButton(self.interRadioBtn,1)
        self.radioGroup.addButton(self.wiperRadioBtn,2)
        self.radioGroup.addButton(self.engineRadioBtn,3)
        self.radioGroup.addButton(self.rimRadioBtn,4)
        for btn in self.radioGroup.buttons():
            self.radioGroupLayout.addWidget(btn)
        self.verticalLayout.addLayout(self.radioGroupLayout)
        self.checkBtn = QtWidgets.QPushButton()
        self.verticalLayout.addWidget(self.checkBtn)
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

    def getTableItemColor(self,key = int()):
        return self.itemColorDict[key]
    
    def setItemColor(self, item = QtWidgets.QTableWidgetItem(), color = QtGui.QColor()):
        item.setTextColor(color)

    def getStatusMsg(self, statusId = int()):
        return self.itemStatus[statusId]
    
    def setStatusMsg(self, item = QtWidgets.QTableWidgetItem(), key = int()):
        itemText = self.getStatusMsg(key)
        item.setText(itemText)
        
