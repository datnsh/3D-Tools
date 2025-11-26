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
    def setupUI(self, widget = QtWidgets.QWidget()):
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.checkBtn = QtWidgets.QPushButton()
        self.verticalLayout.addWidget(self.checkBtn)
        self.checkTable = QtWidgets.QTableWidget()
        self.checkTable.setColumnCount(3)
        self.checkTable.setHorizontalHeaderLabels(["LOD Name", "Current", "Status"])
        self.checkTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.verticalLayout.addWidget(self.checkTable)
        widget.setLayout(self.verticalLayout)
        self.setWidget(widget)
    def retranslateUI(self):
        self.checkBtn.setText("Check polycount")
    def closeLastInstance(self, mainWindow, widgetName):
        for widget in mainWindow.findChildren(QtWidgets.QDockWidget):
            if widget.objectName() == widgetName:
                widget.close()
    def addTableItem(self, firstCol, secondCol, thirdCol):
        row = self.checkTable.rowCount()
        self.checkTable.insertRow(row)
        self.checkTable.setItem(row, 0, QtWidgets.QTableWidgetItem(firstCol))
        self.checkTable.setItem(row, 1, QtWidgets.QTableWidgetItem(secondCol))
        self.checkTable.setItem(row, 2, QtWidgets.QTableWidgetItem(thirdCol))
        
