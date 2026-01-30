import importlib, sys,os
filePath = os.path.dirname(__file__)
folderPath = os.path.dirname(filePath)
sys.path.append(folderPath)
from PySide2 import QtCore, QtWidgets, QtGui
from validation_tool.model import validation_variables
importlib.reload(validation_variables)


class ValidationUI(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.red_color = QtGui.QColor('red')
        self.original_color= QtGui.QColor('#646464')
        container = QtWidgets.QWidget()
        self.setupUi(container)

    def setupUi(self, container):
        self.tab_widget = QtWidgets.QTabWidget()
        first_tab = QtWidgets.QWidget()
        second_tab = QtWidgets.QWidget()
        
        self.tab_widget.addTab(first_tab, validation_variables.FIRST_TAB)
        self.tab_widget.addTab(second_tab, validation_variables.SECOND_TAB)

        #Wheel Tab's Layout
        firstTabLayout = QtWidgets.QVBoxLayout(first_tab)
        
        #----- First Group ------#
        first_group_box = QtWidgets.QGroupBox(validation_variables.FIRST_GROUP_BOX)
        first_group_layout = QtWidgets.QHBoxLayout()
        self.combo_box = QtWidgets.QComboBox()
        self.first_check_box = QtWidgets.QCheckBox(validation_variables.FIRST_CHECK_BOX)
        self.second_check_box = QtWidgets.QCheckBox(validation_variables.SECOND_CHECK_BOX)
        self.third_check_box = QtWidgets.QCheckBox(validation_variables.THIRD_CHECK_BOX)
        self.fourth_check_box = QtWidgets.QCheckBox(validation_variables.FOURTH_CHECK_BOX)
        first_group_layout.addWidget(self.first_check_box)
        first_group_layout.addWidget(self.second_check_box)
        first_group_layout.addWidget(self.third_check_box)
        first_group_layout.addWidget(self.fourth_check_box)
        first_group_layout.addWidget(self.combo_box)
        first_group_box.setLayout(first_group_layout)
        #------ --------------#

        #----- Second Group ------#
        second_group_box = QtWidgets.QGroupBox(validation_variables.SECOND_GROUP_BOX)
        second_layout = QtWidgets.QVBoxLayout()
        self.list_box = QtWidgets.QListWidget()
        self.list_box.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.first_btn = QtWidgets.QPushButton(validation_variables.FIRST_BTN_TEXT)
        self.second_btn = QtWidgets.QPushButton()
        self.third_btn = QtWidgets.QPushButton()
        
        second_layout.addWidget(self.list_box)
        second_layout.addWidget(self.first_btn)
        second_layout.addWidget(self.second_btn)
        second_layout.addWidget(self.third_btn)
        second_group_box.setLayout(second_layout)
        

        third_group_box = QtWidgets.QGroupBox(validation_variables.THIRD_GROUP_BOX)

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
        third_group_box.setLayout(uv_vertical_layout)
        # TestButton for Testing new function
        test_btn = QtWidgets.QPushButton("Test Function Button")
        #test_btn.clicked.connect(self.check_asset_path)
        
        #Wheel Tab's Component
        firstTabLayout.addWidget(first_group_box)
        firstTabLayout.addWidget(second_group_box)
        firstTabLayout.addWidget(third_group_box)
        #firstTabLayout.addWidget(test_btn)
        
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        
        container.setLayout(main_layout)
        
        self.setWidget(container)
        self.resize(300,450)
        self.retranslate_ui(self)

    def add_to_combo_box(self, itemList: list, combo_box : QtWidgets.QComboBox):
        for item in itemList:
            display = f"{item}"
            combo_box.addItem(display)
        combo_box.setCurrentIndex(0)

    def close_last_instance(self, mainWindow, widgetName):
        for widget in mainWindow.findChildren(QtWidgets.QDockWidget):
            if widget.objectName() == widgetName:
                widget.close()

    def retranslate_ui(self, Widget : QtWidgets.QWidget):
        Widget.setWindowTitle(QtCore.QCoreApplication.translate("Widget",validation_variables.TOOL_TITLE, None))
        self.add_to_combo_box(validation_variables.LOD_LIST, self.combo_box)
        self.second_btn.setText(QtCore.QCoreApplication.translate("Widget",validation_variables.SECOND_BTN_TEXT[0], None))
        self.third_btn.setText(QtCore.QCoreApplication.translate("Widget",validation_variables.THIRD_BTN_TEXT[0], None))

    def switch_button(self, selected_btn:QtWidgets.QPushButton, btn_color:QtGui.QColor, btnText:str):
        selected_btn.setText(btnText)
        palette = selected_btn.palette()
        palette.setColor(QtGui.QPalette.Button, btn_color)
        selected_btn.setPalette(palette)
        selected_btn.setAutoFillBackground(True)
    
    def clear_check_table(self):
        self.list_box.clear()

    def add_to_checklist(self,obj: any, item_text : str, res: bool): # Pass in 3ds Max scene objects for obj
        item = QtWidgets.QListWidgetItem()
        widget = QtWidgets.QWidget()
        item_layout = QtWidgets.QHBoxLayout(widget)
        item_layout.setContentsMargins(5, 0, 5, 0)
        item_label = QtWidgets.QLabel(item_text)
        item_layout.addWidget(item_label)
        item.setData(QtCore.Qt.UserRole, obj)
        self.set_label_color(label=item_label, ok=res)
        self.add_fix_btn(item_layout=item_layout)
        self.list_box.addItem(item)
        self.list_box.setItemWidget(item,widget)
    
    def set_label_color(self, label: QtWidgets.QLabel, ok: bool):
        if(ok):
            label.setStyleSheet(
                "color: 'light green';"
            )
        else:
            label.setStyleSheet(
                "color: 'red';" 
                "background: 'white';"
            )
    
    def add_fix_btn(self, item_layout: QtWidgets.QHBoxLayout):
        btn = QtWidgets.QPushButton("Fix")
        btn.setFixedSize(50,20)
        item_layout.addWidget(btn)
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