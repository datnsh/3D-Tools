import qtmax, importlib, sys,os
filePath = os.path.dirname(__file__)
folderPath = os.path.dirname(filePath)
sys.path.append(folderPath)
from PySide2 import QtCore, QtWidgets, QtGui
from model import ValidationVariables
importlib.reload(ValidationVariables)


class ValidationUI(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.redColor = QtGui.QColor('red')
        self.originalColor= QtGui.QColor('#646464')
        container = QtWidgets.QWidget()
        self.setupUi(container)

    def setupUi(self, container):
        self.tabWidget = QtWidgets.QTabWidget()
        firstTab = QtWidgets.QWidget()
        secondTab = QtWidgets.QWidget()
        
        self.tabWidget.addTab(firstTab, ValidationVariables.FIRST_TAB)
        self.tabWidget.addTab(secondTab, ValidationVariables.SECOND_TAB)

        #Wheel Tab's Layout
        firstTabLayout = QtWidgets.QVBoxLayout(firstTab)
        
        #----- First Group ------#
        firstGroupBox = QtWidgets.QGroupBox(ValidationVariables.FIRST_GROUP_BOX)
        firstGroupLayout = QtWidgets.QHBoxLayout()
        self.comboBox = QtWidgets.QComboBox()
        self.firstCheckBox = QtWidgets.QCheckBox(ValidationVariables.FIRST_CHECK_BOX)
        self.secondCheckBox = QtWidgets.QCheckBox(ValidationVariables.SECOND_CHECK_BOX)
        self.thirdCheckBox = QtWidgets.QCheckBox(ValidationVariables.THIRD_CHECK_BOX)
        self.fourthCheckBox = QtWidgets.QCheckBox(ValidationVariables.FOURTH_CHECK_BOX)
        firstGroupLayout.addWidget(self.firstCheckBox)
        firstGroupLayout.addWidget(self.secondCheckBox)
        firstGroupLayout.addWidget(self.thirdCheckBox)
        firstGroupLayout.addWidget(self.fourthCheckBox)
        firstGroupLayout.addWidget(self.comboBox)
        firstGroupBox.setLayout(firstGroupLayout)
        #------ --------------#

        #----- Second Group ------#
        secondGroupBox = QtWidgets.QGroupBox(ValidationVariables.SECOND_GROUP_BOX)
        secondLayout = QtWidgets.QVBoxLayout()
        self.listBox = QtWidgets.QListWidget()
        self.listBox.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.firstBtn = QtWidgets.QPushButton(ValidationVariables.FIRST_BTN_TEXT)
        self.secondBtn = QtWidgets.QPushButton()
        self.thirdBtn = QtWidgets.QPushButton()
        
        secondLayout.addWidget(self.listBox)
        secondLayout.addWidget(self.firstBtn)
        secondLayout.addWidget(self.secondBtn)
        secondLayout.addWidget(self.thirdBtn)
        secondGroupBox.setLayout(secondLayout)
        

        thirdGroupBox = QtWidgets.QGroupBox(ValidationVariables.THIRD_GROUP_BOX)

        #TODO:Refactor and add functions for this layout
        #UV Checker
        uv_layout = QtWidgets.QHBoxLayout()
        uv_vertical_layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Select Channel:")
        self.uv_channel_list = QtWidgets.QComboBox()
        
        uv_layout.addWidget(label)
        uv_layout.addWidget(self.uv_channel_list)
        self.swap_btn = QtWidgets.QPushButton("Swap")
        self.show_both_btn = QtWidgets.QPushButton("Show Both")
        uv_btn_layout = QtWidgets.QVBoxLayout()
        uv_btn_layout.addWidget(self.swap_btn)
        uv_btn_layout.addWidget(self.show_both_btn)
        self.check_uv_btn = QtWidgets.QPushButton("Check UV")
        #self.check_uv_btn.clicked.connect(self.on_check_uv_btn_clicked)
        #radio_horizontal_layout.addLayout(source_radio_layout)
        #radio_horizontal_layout.addSpacerItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        #radio_horizontal_layout.addLayout(uv_btn_layout)
        #radio_horizontal_layout.addSpacerItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        #radio_horizontal_layout.addLayout(target_radio_layout)
        uv_vertical_layout.addLayout(uv_layout)
        #uv_vertical_layout.addLayout(radio_horizontal_layout)
        uv_vertical_layout.addWidget(self.check_uv_btn)
        thirdGroupBox.setLayout(uv_vertical_layout)
        # TestButton for Testing new function
        test_btn = QtWidgets.QPushButton("Test Function Button")
        #test_btn.clicked.connect(self.check_asset_path)
        
        #Wheel Tab's Component
        firstTabLayout.addWidget(firstGroupBox)
        firstTabLayout.addWidget(secondGroupBox)
        firstTabLayout.addWidget(thirdGroupBox)
        #firstTabLayout.addWidget(test_btn)
        
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tabWidget)
        
        container.setLayout(main_layout)
        
        self.setWidget(container)
        self.resize(300,450)
        self.retranslateUi(self)

    def addToComboBox(self, itemList, comboBox):
        for item in itemList:
            display = f"{item}"
            comboBox.addItem(display)
        comboBox.setCurrentIndex(0)

    def closeLastInstance(self, mainWindow, widgetName):
        for widget in mainWindow.findChildren(QtWidgets.QDockWidget):
            if widget.objectName() == widgetName:
                widget.close()

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtCore.QCoreApplication.translate("Widget",ValidationVariables.TOOL_TITLE, None))
        self.addToComboBox(ValidationVariables.LOD_LIST, self.comboBox)
        self.secondBtn.setText(QtCore.QCoreApplication.translate("Widget",ValidationVariables.SECOND_BTN_TEXT, None))
        self.thirdBtn.setText(QtCore.QCoreApplication.translate("Widget",ValidationVariables.THIRD_BTN_TEXT, None))

    def switchButton(self, selectedBtn:QtWidgets.QPushButton, btnColor:QtGui.QColor, btnText:str):
        selectedBtn.setText(btnText)
        palette = selectedBtn.palette()
        palette.setColor(QtGui.QPalette.Button, btnColor)
        selectedBtn.setPalette(palette)
        selectedBtn.setAutoFillBackground(True)

    def addToChecklist(self,obj, message):
        item = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        item_layout = QtWidgets.QHBoxLayout(widget)
        item_layout.setContentsMargins(5, 0, 5, 0)
        item_label = QtWidgets.QLabel(message)
        btn = QtWidgets.QPushButton("Fix")
        btn.setFixedSize(50,20)
        item_layout.addWidget(item_label)
        item_layout.addWidget(btn)
        item.setData(QtCore.Qt.UserRole, obj)
        self.listBox.addItem(item)
        self.listBox.setItemWidget(item,widget)
        """
        if(obj is not None):
            item_text = f"{obj.name} {message}"
        else:
            item_text = f"{message}"
        list_item = QtWidgets.QListWidgetItem(item_text)
        list_item.setData(QtCore.Qt.UserRole, obj)
        self.set_item_color(list_item, color)
        self.list_box.addItem(list_item)
        """