from PySide2 import QtWidgets, QtGui,QtCore
from polycount_checker.model import poly_checker_variables as pv
import importlib
importlib.reload(pv)

class PolyCheckerUI(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(pv.UI_NAME)
        widget = QtWidgets.QWidget()
        self.setup_ui(widget)
        self.resize(360,300)
        self.retranslate_ui()
        self.item_color_dict = pv.ITEM_COLOR
        self.item_status = pv.STATUS
        
    def setup_ui(self, widget = QtWidgets.QWidget()):
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.radio_group_layout = QtWidgets.QHBoxLayout()
        self.stock_radio_btn = QtWidgets.QRadioButton(pv.STOCK)
        self.racer_radio_btn = QtWidgets.QRadioButton(pv.RACER)
        self.inter_radio_btn = QtWidgets.QRadioButton(pv.INTERIOR)
        #self.wiperRadioBtn = QtWidgets.QRadioButton("Wipers")
        #self.engineRadioBtn = QtWidgets.QRadioButton("Engine")
        self.rim_radio_btn = QtWidgets.QRadioButton(pv.RIMS)
        self.radio_group = QtWidgets.QButtonGroup()
        self.radio_group.addButton(self.stock_radio_btn,pv.BODY_TYPE)
        self.radio_group.addButton(self.racer_radio_btn,pv.RACER_TYPE)
        self.radio_group.addButton(self.inter_radio_btn,pv.INTERIOR_TYPE)
        #self.radio_group.addButton(self.wiperRadioBtn,2)
        #self.radio_group.addButton(self.engineRadioBtn,3)
        self.radio_group.addButton(self.rim_radio_btn,pv.RIM_TYPE) #Change this to 4 or subsequent index if uncomment above buttons
        for btn in self.radio_group.buttons():
            self.radio_group_layout.addWidget(btn)
        self.vertical_layout.addLayout(self.radio_group_layout)
        self.horizontal_btn_layout = QtWidgets.QHBoxLayout()
        self.check_btn = QtWidgets.QPushButton()
        self.clear_btn = QtWidgets.QPushButton()
        self.horizontal_btn_layout.addWidget(self.check_btn)
        self.horizontal_btn_layout.addWidget(self.clear_btn)
        self.vertical_layout.addLayout(self.horizontal_btn_layout)

        self.check_table = QtWidgets.QTableWidget()
        self.check_table.setColumnCount(3)
        self.check_table.setHorizontalHeaderLabels(["LOD Name", "Current", "Status"])
        self.check_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.check_table.setSortingEnabled(True)
        self.vertical_layout.addWidget(self.check_table)
        widget.setLayout(self.vertical_layout)
        self.setWidget(widget)

    def retranslate_ui(self):
        self.check_btn.setText("Check polycount")
        self.clear_btn.setText("Clear")
        self.stock_radio_btn.setChecked(True)

    def close_last_instance(self, main_window: QtWidgets.QMainWindow, widgetName : str):
        for widget in main_window.findChildren(QtWidgets.QDockWidget):
            if widget.objectName() == widgetName:
                widget.close()

    def add_table_item(self, firstCol, secondCol, thirdCol):
        self.check_table.setSortingEnabled(False)
        row = self.check_table.rowCount()
        tableFirstCol = QtWidgets.QTableWidgetItem(firstCol)
        tableSecondCol = QtWidgets.QTableWidgetItem(secondCol)
        tableThirdCol = QtWidgets.QTableWidgetItem(thirdCol)
        self.check_table.insertRow(row)
        tableThirdCol.setData(QtCore.Qt.UserRole, thirdCol)

        color = self.get_item_color(thirdCol)
        self.set_item_color(tableThirdCol,color)

        self.check_table.setItem(row, 0, tableFirstCol)
        self.check_table.setItem(row, 1, tableSecondCol)
        self.check_table.setItem(row, 2, tableThirdCol)
        self.check_table.setSortingEnabled(True)
    
    def set_item_color(self, item: QtWidgets.QTableWidgetItem, color: QtGui.QColor):
        item.setTextColor(color)
        if color != pv.LIGHT_GREEN:
            item.setBackgroundColor(self.item_color_dict[3])

    def get_status_msg(self, statusId: int):
        return self.item_status[statusId]
    
    def set_status_msg(self, item: QtWidgets.QTableWidgetItem, key: int):
        itemText = self.get_status_msg(key)
        item.setText(itemText)

    def get_item_color(self, status):
        if(pv.STATUS[0] in status):
            return pv.ITEM_COLOR[0]
        elif(pv.STATUS[1] in status):
            return pv.ITEM_COLOR[1]
        else:
            return pv.ITEM_COLOR[2]
        
