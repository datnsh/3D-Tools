import re, qtmax, importlib, sys,os
filePath = os.path.dirname(__file__)
folderPath = os.path.dirname(filePath)
sys.path.append(folderPath)
from PySide2 import QtCore, QtWidgets, QtGui
from model import ValidationVariables
importlib.reload(ValidationVariables)

class ValidationUI(QtWidgets.QDockWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ValidationUI.instance = self
        """
        TODO: refactor to either Utils or controller.
        self.all_objects = rt.objects # Utilities or Controller.
        

        self.lod_morph_list = []
        self.object_dict = {}
        """
        lod_list = ValidationVariables.COMBO_BOX_LIST
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowTitle(ValidationVariables.TOOL_TITLE)
        
        self.init_ui()
        self.addItems(lod_list,self.combo_box)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.wheel_colors_active = False
        self.uv2_checker_active = False
    def init_ui(self):
        self.tab_widget = QtWidgets.QTabWidget()
        first_tab = QtWidgets.QWidget()
        second_tab = QtWidgets.QWidget()
        first_tab_layout = QtWidgets.QVBoxLayout(first_tab)
        self.tab_widget.addTab(first_tab, ValidationVariables.FIRST_TAB)
        self.tab_widget.addTab(second_tab, ValidationVariables.SECOND_TAB)

        #Wheel Tab's Layout
        first_group_box = QtWidgets.QGroupBox(ValidationVariables.FIRST_GROUP_BOX)
        second_group_box = QtWidgets.QGroupBox(ValidationVariables.SECOND_GROUP_BOX)
        third_group_box = QtWidgets.QGroupBox(ValidationVariables.THIRD_GROUP_BOX)

        # LOD Group Component
        lod_layout = QtWidgets.QHBoxLayout()
        self.combo_box = QtWidgets.QComboBox()
        #self.combo_box.currentTextChanged.connect(self.on_lod_group_changed)
        self.first_check_box = QtWidgets.QCheckBox(ValidationVariables.FIRST_CHECK_BOX)
        self.second_check_box = QtWidgets.QCheckBox(ValidationVariables.SECOND_CHECK_BOX)
        self.third_check_box = QtWidgets.QCheckBox(ValidationVariables.THIRD_CHECK_BOX)
        self.fourth_check_box = QtWidgets.QCheckBox(ValidationVariables.FOURTH_CHECK_BOX)
        lod_layout.addWidget(self.first_check_box)
        lod_layout.addWidget(self.second_check_box)
        lod_layout.addWidget(self.third_check_box)
        lod_layout.addWidget(self.fourth_check_box)
        lod_layout.addWidget(self.combo_box)
        first_group_box.setLayout(lod_layout)
        
        # Wheel CheckList Components
        second_layout = QtWidgets.QVBoxLayout()
        self.list_box = QtWidgets.QListWidget()
        #self.list_box.itemClicked.connect(self.on_item_selected)
        self.list_box.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        check_btn = QtWidgets.QPushButton("Check Wheel")
        self.assign_material_btn = QtWidgets.QPushButton("Check wheel colors")
        #self.assign_material_btn.clicked.connect(self.on_assign_material_btn_clicked)
        self.assign_uv2checker_btn = QtWidgets.QPushButton("Check UV2")
        #self.assign_uv2checker_btn.clicked.connect(self.on_uv2checker_btn_clicked)
        
        #check_btn.clicked.connect(self.on_check_btn_clicked)
        second_layout.addWidget(self.list_box)
        second_layout.addWidget(check_btn)
        second_layout.addWidget(self.assign_material_btn)
        second_layout.addWidget(self.assign_uv2checker_btn)
        second_group_box.setLayout(second_layout)
        
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
        first_tab_layout.addWidget(first_group_box)
        first_tab_layout.addWidget(second_group_box)
        first_tab_layout.addWidget(third_group_box)
        first_tab_layout.addWidget(test_btn)
        
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        
        widget = QtWidgets.QWidget()
        widget.setLayout(main_layout)
        self.setWidget(widget)
        self.resize(300,650)

    def wheel_color_btn_active(self):
        self.wheel_colors_active = False
    def uv2_checker_active(self):
        self.uv2_checker_active = False
    def addItems(self, itemList, combo_box):
        for item in itemList:
            display = f"LOD{item}"
            combo_box.addItem(display)
        combo_box.setCurrentIndex(0)
    
def main():
    main_window = qtmax.GetQMaxMainWindow()
    for widget in main_window.findChildren(QtWidgets.QDockWidget):
        if widget.objectName() == "ValidationTool":
            widget.close()
    w = ValidationUI(parent=main_window)
    w.setObjectName("ValidationTool")
    w.setFloating(True)
    w.show()

if __name__ == "__main__":
    main()