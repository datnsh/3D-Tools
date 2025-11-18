import re, qtmax, importlib
from pymxs import runtime as rt
from PySide2 import QtCore, QtWidgets, QtGui
from model.ValidationVariables import LOD_LIST, LOD_MORPH

class ValidationUI(QtWidgets.QDockWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ValidationUI.instance = self
        self.all_objects = rt.objects # Utilities or Controller.
        self.lod_list = ['S0','S','0','1','2','3','4','5']

        self.lod_morph_list = []
        self.object_dict = {}
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowTitle('Tool and Validation')
        
        self.init_ui()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.wheel_colors_active = False
        self.uv2_checker_active = False
    def init_ui(self):
        self.tab_widget = QtWidgets.QTabWidget()
        wheel_tab = QtWidgets.QWidget()
        car_tab = QtWidgets.QWidget()
        wheel_layout = QtWidgets.QVBoxLayout(wheel_tab)
        self.tab_widget.addTab(wheel_tab, "Wheel Checker")
        self.tab_widget.addTab(car_tab, "Car Checker")
        #Wheel Tab's Layout
        lod_group_box = QtWidgets.QGroupBox("LOD")
        option_group_box = QtWidgets.QGroupBox("Options")
        list_group_box = QtWidgets.QGroupBox("Wheel Checklist")
        uv_group_box = QtWidgets.QGroupBox("UV Checker(WIP)")
        # LOD Group Component
        lod_layout = QtWidgets.QHBoxLayout()
        self.combo_box = QtWidgets.QComboBox()
        for i in self.lod_list:
            display = f"LOD{i}"
            self.combo_box.addItem(display)
        self.combo_box.setCurrentIndex(0)
        self.combo_box.currentTextChanged.connect(self.on_lod_group_changed)
        self.spindle_check_box = QtWidgets.QCheckBox("Hide spindle")
        self.morph_check_box = QtWidgets.QCheckBox("Hide morph")
        self.blur_check_box = QtWidgets.QCheckBox("Hide blur")
        self.wheel_check_box = QtWidgets.QCheckBox("Hide wheel")
        lod_layout.addWidget(self.spindle_check_box)
        lod_layout.addWidget(self.morph_check_box)
        lod_layout.addWidget(self.blur_check_box)
        lod_layout.addWidget(self.wheel_check_box)
        lod_layout.addWidget(self.combo_box)
        lod_group_box.setLayout(lod_layout)
        
        # Option Group Component
        option_layout = QtWidgets.QHBoxLayout()
        self.check_box = QtWidgets.QRadioButton("Wheel 5K(WIP)")
        self.check_box_b = QtWidgets.QRadioButton("Wheel 20K(WIP)")
        option_layout.addWidget(self.check_box)
        option_layout.addWidget(self.check_box_b)
        option_group_box.setLayout(option_layout)
        
        # Wheel CheckList Components
        second_layout = QtWidgets.QVBoxLayout()
        self.list_box = QtWidgets.QListWidget()
        self.list_box.itemClicked.connect(self.on_item_selected)
        self.list_box.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        check_btn = QtWidgets.QPushButton("Check Wheel")
        self.assign_material_btn = QtWidgets.QPushButton("Check wheel colors")
        self.assign_material_btn.clicked.connect(self.on_assign_material_btn_clicked)
        self.assign_uv2checker_btn = QtWidgets.QPushButton("Check UV2")
        self.assign_uv2checker_btn.clicked.connect(self.on_uv2checker_btn_clicked)
        
        check_btn.clicked.connect(self.on_check_btn_clicked)
        second_layout.addWidget(self.list_box)
        second_layout.addWidget(check_btn)
        second_layout.addWidget(self.assign_material_btn)
        second_layout.addWidget(self.assign_uv2checker_btn)
        list_group_box.setLayout(second_layout)
        
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
        self.check_uv_btn.clicked.connect(self.on_check_uv_btn_clicked)
        radio_horizontal_layout.addLayout(source_radio_layout)
        radio_horizontal_layout.addSpacerItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        radio_horizontal_layout.addLayout(uv_btn_layout)
        radio_horizontal_layout.addSpacerItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        radio_horizontal_layout.addLayout(target_radio_layout)
        uv_vertical_layout.addLayout(uv_layout)
        uv_vertical_layout.addLayout(radio_horizontal_layout)
        uv_vertical_layout.addWidget(self.check_uv_btn)
        uv_group_box.setLayout(uv_vertical_layout)
        # TestButton for Testing new function
        test_btn = QtWidgets.QPushButton("Test Function Button")
        test_btn.clicked.connect(self.check_asset_path)
        
        #Wheel Tab's Component
        wheel_layout.addWidget(lod_group_box)
        wheel_layout.addWidget(option_group_box)
        wheel_layout.addWidget(list_group_box)
        wheel_layout.addWidget(uv_group_box)
        wheel_layout.addWidget(test_btn)
        
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        
        widget = QtWidgets.QWidget()
        widget.setLayout(main_layout)
        self.setWidget(widget)
        self.resize(300,650)
    def on_uv2checker_btn_clicked(self):
        if(not self.uv2_checker_active):
            self.assign_uv2checker_btn.setText("Restore Material")
            palette = self.assign_uv2checker_btn.palette()
            palette.setColor(QtGui.QPalette.Button, QtGui.QColor('red'))
            self.assign_uv2checker_btn.setPalette(palette)
            self.assign_uv2checker_btn.setAutoFillBackground(True)
            DMA.apply_material_to_polygons(DMA.UV2Checker)
        else:
            self.assign_uv2checker_btn.setText("Check UV2")
            palette = QtWidgets.QApplication.style().standardPalette()
            self.assign_uv2checker_btn.setPalette(palette)
            self.assign_uv2checker_btn.setAutoFillBackground(False)
            DMA.restore_original_materials()
        self.switch_activation_status('uv2_checker_active')
        rt.redrawViews()
    def on_check_uv_btn_clicked(self):
        for obj in self.all_objects:
            pat_match = re.match(DNC.PATTERN,obj.name)
            if(pat_match):
                key = pat_match.group(2)
                if(key in self.object_dict):
                    self.object_dict[key].append(obj)
                else:
                    self.object_dict[key] = [obj]
        current_checked = self.source_radio_group.checkedButton()
        current_lod = current_checked.property(lod_value)
        rt.clearSelection
        rt.selection = rt.array(self.object_dict[current_lod])
        for obj in self.object_dict[current_lod]:
            rt.select(self.object_dict[current_lod])
            print(obj.name)
        rt.redrawViews()
    def on_lod_group_changed(self):
        current_lod = self.combo_box.currentText()
        for obj in self.all_objects:
            if(obj.name == "spindle"):
                if(self.spindle_check_box.isChecked()):
                    obj.isHidden = True
                else:
                    obj.isHidden = False
                continue
            pat_match = re.match(self.pattern, obj.name)
            if(pat_match):
                pat_morph_match = pat_match.group(3)
                pat_wheel_match = pat_match.group(1)
                pat_search = re.search(current_lod,obj.name)
                if(self.morph_check_box.isChecked()):
                    if pat_morph_match is not None:
                        obj.isHidden = True
                        continue
                if(self.blur_check_box.isChecked()):
                    if re.search("blur", obj.name):
                        obj.isHidden = True
                        continue
                if(self.wheel_check_box.isChecked()):
                    if re.search("wheel", obj.name):
                        obj.isHidden = True
                        continue
                if pat_match and not pat_search:
                    obj.isHidden = True
                else:
                    obj.isHidden = False
        rt.redrawViews()
    def switch_activation_status(self, attr_name):
        current_value = getattr(self, attr_name, None)
        if(current_value is None or not isinstance(current_value, bool)):
            return
        new_value = not current_value
        setattr(self, attr_name, new_value)
    def on_assign_material_btn_clicked(self):
        if(not self.wheel_colors_active):
            self.assign_material_btn.setText("Restore Material")
            palette = self.assign_material_btn.palette()
            palette.setColor(QtGui.QPalette.Button, QtGui.QColor('red'))
            self.assign_material_btn.setPalette(palette)
            self.assign_material_btn.setAutoFillBackground(True)
            DMA.apply_material_to_polygons(DMA.WheelColor)
        else:
            self.assign_material_btn.setText("Check wheel colors")
            palette = QtWidgets.QApplication.style().standardPalette()
            self.assign_material_btn.setPalette(palette)
            self.assign_material_btn.setAutoFillBackground(False)
            DMA.restore_original_materials()
        self.switch_activation_status('wheel_colors_active')
        rt.redrawViews()
    def on_item_selected(self):
        selected_objects = []
        for selected_item in self.list_box.selectedItems():
            obj = selected_item.data(QtCore.Qt.UserRole)
            if obj:
                selected_objects.append(obj)
        rt.select(selected_objects)
        rt.redrawViews()
    def add_to_checklist(self,obj, message, color):
        if(obj is not None):
            item_text = f"{obj.name} {message}"
        else:
            item_text = f"{message}"
        list_item = QtWidgets.QListWidgetItem(item_text)
        list_item.setData(QtCore.Qt.UserRole, obj)
        self.set_item_color(list_item, color)
        self.list_box.addItem(list_item)
    def set_item_color(self, item, color):
        if color == ItemColor.RED:
            item.setForeground(QtGui.QColor('red'))
        elif color == ItemColor.GREEN:
            item.setForeground(QtGui.QColor('light green'))
    def check_sub_selection(self,obj):
        if(not DWV.check_sub_selection(obj)):
            self.add_to_checklist(obj, "has sub selection", ItemColor.RED)
            self.check_list[SUB_SELECTION_MSG] = False
    def on_check_btn_clicked(self):
        self.list_box.clear()
        for key in self.check_list:
            self.check_list[key] = True
        if not self.all_objects:
            rt.messageBox(message, "The current scene is empty")
            return
        self.check_layer()
        self.check_isolation()
        self.check_helpers()
        for obj in self.all_objects:
            rt.freeze(obj)
            if(obj.name != "spindle"):
                self.wheel_name_check(obj)
                self.check_pivot(obj)
                self.check_morph(obj)
                self.check_sub_selection(obj)
                if re.search("blur",obj.name, re.IGNORECASE):
                    self.check_blur_id(obj)
            else:
                self.check_spindle(obj)
            rt.unfreeze(obj)
        for key, value in self.check_list.items():
            if value:
                self.add_to_checklist(None, key, ItemColor.GREEN)
    def wheel_name_check(self, obj):
        if(not DNC.check_name(obj.name)):
            self.add_to_checklist(obj," has wrong naming",ItemColor.RED)
            self.check_list[NAME_CHECK_MSG] = False
    def check_asset_path(self):
        pass
    def check_spindle(self, spindle):
        if(not DWV.check_spindle_rotation(spindle)):
            self.add_to_checklist(spindle, "has rotation", ItemColor.RED)
            self.check_list[SPINDLE_CHECK_MSG] = False
        else:
            self.check_list[SPINDLE_CHECK_MSG] = True
    def check_pivot(self, obj):
        if(obj.name == "spindle"):
            return
        is_valid, pivot_transform = DWV.check_pivot(obj)
        if(not is_valid):
            self.add_to_checklist(obj, f"pivot is not at origin (0,0,0): {pivot_transform} ", ItemColor.RED)
            self.check_list[PIVOT_CHECK_MSG] = False
    def check_helpers(self):
        if(not DWV.check_helpers()):
            self.add_to_checklist(None, "Helpers is checked",ItemColor.RED)
            self.check_list[HELPER_CHECK_MSG] = False
    def check_blur_id(self, obj):
        if(not DWV.check_blur_id(obj)):
            self.add_to_checklist(obj, "has wrong material ID", ItemColor.RED)
    def check_isolation(self):
        if(DWV.check_isolation_active()):
            self.add_to_checklist(None,"The current scene has one or more objects isolated", ItemColor.RED)
            self.check_list[ISOLATION_CHECK_MSG] = False
    def check_layer(self):
        if(not DWV.check_layer()):
            self.add_to_checklist(None,"The current scene has two or more layers", ItemColor.RED)
            self.check_list[LAYER_CHECK_MSG] = False
        else:
            self.check_list[LAYER_CHECK_MSG] = True
    def validate_selection(self):
        pass
    def check_morph(self, obj):
        if(not DWV.check_morph(obj)):
            self.add_to_checklist(obj," doesn't have a morph modifier", ItemColor.RED)
            self.check_list[MORPH_CHECK_MSG] = False
def main():
    main_window = qtmax.GetQMaxMainWindow()
    for widget in main_window.findChildren(QtWidgets.QDockWidget):
        if widget.objectName() == "ValidationTool":
            widget.close()
    w = ValidationUI(parent=main_window)
    w.setObjectName("ValidationTool")
    w.setFloating(True)
    w.show()