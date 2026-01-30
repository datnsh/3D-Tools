import importlib, sys, re
from dataclasses import dataclass
from pymxs import runtime as rt
from PySide2 import QtCore

from validation_tool.model import validation_utils as util
from validation_tool.model import validation_variables as var
from validation_tool.view import validation_ui as ui
from validation_tool.model import validation_error as ve
mods = [util, var, ui,ve]
for mod in mods:
    importlib.reload(mod)

class ValidationController():
    def __init__(self, validation_ui: ui.ValidationUI, validation_util: util.ValidationUtils):
        ValidationController.instance = self
        self.ui = validation_ui
        self.util = validation_util
        self.ui.first_btn.clicked.connect(self.on_first_btn_clicked)
        self.ui.second_btn.clicked.connect(self.on_second_btn_clicked)
        self.__second_btn_active = False
        self.ui.third_btn.clicked.connect(self.on_third_btn_clicked)
        self.ui.list_box.itemSelectionChanged.connect(self.on_item_select)
        self.ui.combo_box.currentTextChanged.connect(self.on_combo_box_changed)
        self.ui.first_check_box.stateChanged.connect(lambda state: self.on_check_box_checked(state, "$*spindle"))
        self.ui.second_check_box.stateChanged.connect(lambda state: self.on_check_box_checked(state, "$*morph*"))
        self.ui.third_check_box.stateChanged.connect(lambda state: self.on_check_box_checked(state, "$blur*"))
        self.ui.fourth_check_box.stateChanged.connect(lambda state: self.on_check_box_checked(state, "$wheel*"))
        self.__third_btn_active = False
        self.default_keys = var.ERROR_MSG
        self._init_error_dict()
        self._init_check_result()

    def on_item_select(self):
        items = self.ui.list_box.selectedItems()
        if not items:
            return
        item = items[0]
        obj = item.data(QtCore.Qt.UserRole)
        if not obj:
            return
        try:
            rt.select(obj)
        except RuntimeError:
            print("False")

    def _init_error_dict(self):
        self.error_dict = {key: [] for key in self.default_keys}
    
    def _init_check_result(self):
        self.check_result = {key: True for key in self.default_keys}
    
    def on_first_btn_clicked(self):
        self.ui.clear_check_table()
        self._init_check_result()
        self._init_error_dict()
        self.validate_scene()
    
    def on_check_box_checked(self,state,name_path):
        if(state == QtCore.Qt.Checked):
            self.util.hide_objects(name_path=name_path)
        else:
            self.util.unhide_objects(name_path=name_path)

    def on_second_btn_clicked(self):
        if(self.__second_btn_active):
            self.__second_btn_active = False
            self.ui.switch_button(self.ui.second_btn, self.ui.original_color, var.SECOND_BTN_TEXT[0])
            self.util.restore_original_materials()
        else:
            self.__second_btn_active = True
            self.ui.switch_button(self.ui.second_btn, self.ui.red_color, var.SECOND_BTN_TEXT[1])
            self.util.apply_material_to_polygons(var.WHEELCOLOR)
            

    def on_third_btn_clicked(self):
        if(self.__third_btn_active):
            self.__third_btn_active = False
            self.ui.switch_button(self.ui.third_btn, self.ui.original_color, var.THIRD_BTN_TEXT[0])
            self.util.restore_original_materials()
        else:
            self.__third_btn_active = True
            self.ui.switch_button(self.ui.third_btn, self.ui.red_color, var.THIRD_BTN_TEXT[1])
            self.util.apply_material_to_polygons(var.UV2CHECKER)
            
    
    def on_combo_box_changed(self):
        current_lod = self.ui.combo_box.currentText()
        name_path = f"$*LOD{current_lod}*"
        self.util.hide_objects(name_path="$*")
        self.util.unhide_objects(name_path=name_path)
        if(self.ui.first_check_box.isChecked()):
            self.util.hide_objects(name_path="$*spindle")
        if(self.ui.second_check_box.isChecked()):
            self.util.hide_objects(name_path="$*morph*")
        if(self.ui.third_check_box.isChecked()):
            self.util.hide_objects(name_path="$*blur*")
        if(self.ui.fourth_check_box.isChecked()):
            self.util.hide_objects(name_path="$*wheel*")
        rt.redrawViews()
        
    def check_helpers(self):
        self._run_check(
            type=var.HELPERS,
            check_func=self.util.check_helpers,
            can_fix=False,
            fix_func=None,
            data=None
        )
    
    def check_spindle_rotation(self,obj):
        self._run_check(
            type=var.SPINDLE,
            check_func=self.util.check_spindle_rotation,
            check_args=(obj,),
            can_fix=False,
            fix_func=None,
            data=obj
        )

    def check_sub_selection(self, obj):
        self._run_check(
            type=var.SUB_SELECTION,
            check_func=self.util.check_sub_selection,
            check_args=(obj,),
            can_fix=False,
            fix_func=None,
            data=obj
        )
    
    def check_layer(self):
        self._run_check(
            type=var.LAYER,
            check_func=self.util.check_layer,
            can_fix=False,
            fix_func=None,
            data=None
        )
    def check_pivot(self,obj):
        self._run_check(
            type=var.PIVOT,
            check_func=self.util.check_pivot,
            check_args=(obj,),
            can_fix=False,
            fix_func=None,
            data=obj
        )
    def check_blur_id(self,obj):
        self._run_check(
            type=var.BLUR_ID,
            check_func=self.util.check_blur_id,
            check_args=(obj,),
            can_fix=False,
            fix_func=None,
            data=obj
        )
    
    def check_morph(self,obj):
        self._run_check(
            type=var.MORPH, 
            check_func=self.util.check_morph,
            check_args=(obj,),
            can_fix=False,
            fix_func=None,
            data=obj
        )
    
    def check_isolation(self):
        self._run_check(
            type=var.ISOLATION,
            check_func=self.util.check_isolation,
            can_fix=False,
            fix_func=None,
            data=None
        )
    def check_name(self,obj):
        self._run_check(
            type=var.NAME,
            check_func=self.util.check_name,
            check_args=(obj,),
            can_fix=False,
            fix_func=None,
            data=obj
        )

    def validate_scene(self):
        all_objects = self.util.get_all_objects()
        rt.clearSelection()
        self.check_helpers()
        self.check_isolation()
        for obj in all_objects:
            self.check_name(obj)
            if(obj.name == "spindle"):
                self.check_spindle_rotation(obj)
            else:
                if("blur" in obj.name):
                    self.check_blur_id(obj)
                self.check_sub_selection(obj)
                self.check_morph(obj)
                self.check_pivot(obj)
                self.check_layer()
        self.print_result()

    def print_result(self):
        for type, res in self.check_result.items():
            if(not res):
                obj_list = self.error_dict[type]
                for error in obj_list:
                    obj = error.data
                    message = error.message
                    self.ui.add_to_checklist(obj=obj,item_text=message,res=False)
            else:
                self.ui.add_to_checklist(obj=None,item_text=var.ERROR_MSG[type][0],res=True)
    
    def _run_check(self,type: str, check_func,*,can_fix=False,fix_func=None,data=None,check_args=None,check_kwargs=None):
        args = check_args or ()
        kwargs = check_kwargs or {}
        res = check_func(*args, **kwargs)
        message = ""
        if(not res):
            if(data):
                message += data.name
            message += var.ERROR_MSG[type][1]
            error = ve.ValidationError(
                message=message,
                can_fix=can_fix,
                fix_func=fix_func,
                data=data,
                type=type
            )
            self.check_result[error.type] = False
            self.error_dict[error.type].append(error)

    def test_error_dict(self):
        for key, value in self.error_dict.items():
            print(f"{key}:")
            if(len(value) > 0):
                error = value[0]
                print(error.type)