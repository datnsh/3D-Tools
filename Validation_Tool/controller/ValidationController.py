from model.ValidationUtils import ValidationUtils
from model import ValidationVariables
from view.ValidationUI import ValidationUI
import importlib, sys
from pymxs import runtime as rt


mods = ["view.ValidationUI","model.ValidationUtils","model.ValidationVariables"]
for mod in mods:
    importlib.reload(sys.modules[mod])

class ValidationController():
    def __init__(self, ui: ValidationUI, util:ValidationUtils):
        ValidationController.instance = self
        self.ui = ui
        self.util = util
        self.ui.firstBtn.clicked.connect(self.onFirstBtnClicked)
        self.ui.secondBtn.clicked.connect(self.onSecondBtnClicked)
        self.__secondBtnActive = False
        self.ui.thirdBtn.clicked.connect(self.onThirdBtnClicked)
        self.__thirdBtnActive = False
    def onFirstBtnClicked(self):
        self.ui.addToChecklist(rt.selection[0],'test')
        #self.ui.switchButton(self.ui.firstBtn, self.ui.original_palette, 'Check Wheel')
    def onSecondBtnClicked(self):
        if(self.__secondBtnActive):
            self.__secondBtnActive = False
            self.ui.switchButton(self.ui.secondBtn, self.ui.originalColor, ValidationVariables.SECOND_BTN_TEXT[0])
        else:
            self.__secondBtnActive = True
            self.ui.switchButton(self.ui.secondBtn, self.ui.redColor, ValidationVariables.SECOND_BTN_TEXT[1])

    def onThirdBtnClicked(self):
        if(self.__thirdBtnActive):
            self.__thirdBtnActive = False
            self.ui.switchButton(self.ui.thirdBtn, self.ui.originalColor, ValidationVariables.THIRD_BTN_TEXT[0])
        else:
            self.__thirdBtnActive = True
            self.ui.switchButton(self.ui.thirdBtn, self.ui.redColor, ValidationVariables.THIRD_BTN_TEXT[1])
    

    """
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
    """