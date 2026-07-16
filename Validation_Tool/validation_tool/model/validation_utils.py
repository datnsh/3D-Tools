import importlib,re, pymxs
from pymxs import runtime as rt
from validation_tool.model import validation_variables as var
from PySide2 import QtCore
importlib.reload(var)


class ValidationUtils():
    def __init__(self):
        ValidationUtils.instance = self
        self.name_pattern = re.compile(var.NAME_PATTERN)
        self.name_list = {"blurRim","blurLip", "wheel", "morph", "morph2","spindle"}
        self.lod_morph_list = {'S0','S','1','0'}
        self.valid_lods = {'S0','S','0','1','2','3','4','5'}
        self.original_material = {}
        self.material_map = {
            var.UV2CHECKER: self.create_uv2_material(),
            var.WHEELCOLOR: self.create_standard_material()
        }
        self.isolated_vertex = {}

    def redraw_view(func):
        def wrapper(*args,**kwargs):
            func(*args,**kwargs)
            rt.redrawViews()
        return wrapper
    
    def check_name(self,obj):
        obj_name = obj.name
        match = re.match(self.name_pattern, obj_name)
        if match:
            name_group = match.group(1)
            lod_group = match.group(2)
            morph_group = match.group(3)
            if(name_group != None and name_group not in self.name_list):
                return False
            if(morph_group != None and lod_group not in self.lod_morph_list):
                return False
            if(lod_group != None and lod_group not in self.valid_lods):
                print(f"Invalid Lod:{lod_group}")
                return False
            return True
        else:
            if obj_name in self.name_list:
                return True
            return False

    def get_all_objects(self):
        return rt.objects
    
    def check_sub_selection(self,obj):
        selection = rt.getSelectionLevel(obj)
        if(str(selection) != 'object'):
            return False
        return True
    
    def check_wheel_size(obj):
        pass

    def check_spindle_rotation(self,spindle):
        rotation = spindle.rotation
        rotation = rt.quatToEuler(rotation)
        if rotation.x != 0 or rotation.y != 0 or rotation.z != 0:
            return False
        else:
            return True
        
    def check_helpers(self):
        if rt.hideByCategory.helpers:
            return False
        else:
            return True
        
    def save_modifier_stack(obj):
        return [rt.copy(mod) for mod in obj.modifiers]
    
    def restore_modifiers(obj, modifiers):
        while(len(obj.modifiers) >0):
            rt.deleteModifier(obj, 1)
        for mod in modifiers:
            rt.addModifier(obj, rt.copy(mod))

    def check_blur_id(self, obj):
        original_mod = [rt.copy(mod) for mod in obj.modifiers]
        if not rt.isKindOf(obj, rt.Editable_Poly):
            obj = rt.convertTo(obj, rt.Editable_Poly)
        try:
            num_faces = rt.polyOp.getNumFaces(obj)
            for i in range(1, num_faces + 1):
                mat_id = rt.polyOp.getFaceMatID(obj, i)
                if re.search("blurLip", obj.name):
                    if mat_id != 15:
                        return False
                elif re.search("blurRim", obj.name):
                    if mat_id != 14:
                        return False
            return True
        finally:
            while obj.modifiers.count>0:
                rt.deleteModifier(obj, 1)
            for mod in original_mod:
                rt.addModifier(obj, rt.copy(mod))

    def check_morph(self, obj):
        match = re.match(self.name_pattern, obj.name)
        if match:
            lod_part = match.group(2)
            string_lod = str(lod_part)
            if(not match.group(3) and string_lod[-1] in var.LOD_MORPH):
                modifier_count = obj.modifiers.count
                if(modifier_count == 0):
                    return False
                else:
                    top_modifier = obj.modifiers[modifier_count - 1]
                    modifier_class =str(rt.classOf(top_modifier))
                    if modifier_class !="Morpher":
                        return False
        return True
    
    def check_pivot(self,obj):
        pivot = obj.pivot
        buffer = 1e-2
        if(abs(pivot.x) < buffer and abs(pivot.y) < buffer and abs(pivot.z) < buffer):
            return True
        else:
            return False
        
    def check_layer(self):
        layer_count = rt.LayerManager.count
        if layer_count > 1:
            return False
        return True
    
    def check_isolation(self):
        if(rt.IsolateSelection.IsolateSelectionModeActive()):
            return False
        else:
            return True
    
    def check_asset_path():
        pass

    def check_isolated_vertices(self,obj):
        check_res = []
        isoVerts = rt.IsolatedVertices.Check(rt.currentTime,obj,pymxs.byref(check_res))
        if len(isoVerts[1]) != 0:
            return False
        return True
    
    def get_objects(self, name_path:str):
        return rt.safeExecute(name_path)
    def hide_objects(self, name_path:str):
        for o in rt.safeExecute(name_path):
            o.isHidden = True
    def unhide_objects(self, name_path:str):
        for o in rt.safeExecute(name_path):
            o.isHidden = False
    

    def create_uv2_material(self):
        uv2_mat = rt.StandardMaterial()
        checker_map = rt.Checker()
        checker_map.name = "CheckerMap"
        checker_map.color1 = (0,0,0)
        checker_map.color2 = (255,255,255)
        checker_map.coordinates.U_Tiling = 15
        checker_map.coordinates.V_Tiling = 15
        checker_map.coordinates.mapChannel = 2
        uv2_mat.diffuseMap = checker_map
        return uv2_mat
    
    def create_standard_material(self):
        colors = [
            rt.color(255, 0, 0),        # ID 1
            rt.color(255, 255, 0),      # ID 2
            rt.color(186, 186, 186),    # ID 3
            rt.color(0, 255, 0),        # ID 4
            rt.color(0, 0, 255),        # ID 5
            rt.color(220, 0, 254),      # ID 6
            rt.color(202, 156, 111),    # ID 7
            rt.color(0, 0, 0),          # ID 8
            rt.color(255, 186, 0),      # ID 9
            rt.color(134, 50, 0),       # ID 10
            rt.color(186, 222, 255),    # ID 11
            rt.color(186, 222, 255),    # ID 12
            rt.color(255, 153, 240),    # ID 13
            rt.color(186, 186, 186),    # ID 14
            rt.color(186, 186, 186),    # ID 15
            rt.color(186, 186, 186),    # ID 16
            rt.color(255, 255, 255),    # ID 17
            rt.color(255, 255, 255),    # ID 18
            rt.color(255, 255, 255),    # ID 19
            rt.color(255, 255, 255),    # ID 20
            rt.color(255, 167, 167),    # ID 21
            rt.color(255, 167, 167),    # ID 22
            rt.color(255, 255, 181),    # ID 23
            rt.color(255, 255, 181),    # ID 24
            rt.color(232, 175, 255),    # ID 25
            rt.color(232, 175, 255),    # ID 26
            rt.color(245, 239, 234)     # ID 27
        ]
        multi_mat = rt.MultiMaterial()
        multi_mat.numsubs = len(colors)
        multi_mat.name = "27_ID_MultiMat"
        for i in range(len(colors)):
            mat = rt.StandardMaterial()
            mat.name = f"Mat_ID_{i+1}"
            mat.diffuse = colors[i]
            multi_mat[i] = mat
        return multi_mat
    
    @redraw_view
    def apply_material_to_polygons(self,material):
        all_object = rt.objects
        material_box = self.material_map[material]
        for obj in all_object:
            if obj.name == "spindle":
                continue
            print(f"Applying new material for {obj.name}")
            if obj.name not in self.original_material:
                self.original_material[obj.name] = obj.material
            obj.material = material_box
        rt.redrawViews()

    @redraw_view
    def restore_original_materials(self):
        all_object = rt.objects
        for obj in all_object:
            if obj.name in self.original_material:
                print(f"restoring original material for: {obj.name}")
                obj.material = self.original_material[obj.name]
            else:
                print(f"No original material stored for {obj.name}")
    
    @redraw_view
    def livery_grid_check(self):
        mat = self.create_livery_grid_material()
        

    def create_livery_grid_material(self):
        wing = "D:\P4\FMBase_Main\Forza2\Main\Media\Src\cars\_Assets\Textures\Test\wing.tga"
        back = "D:\P4\FMBase_Main\Forza2\Main\Media\Src\cars\_Assets\Textures\Test\back.tga"
        top = "D:\P4\FMBase_Main\Forza2\Main\Media\Src\cars\_Assets\Textures\Test\top.tga"
        left = "D:\P4\FMBase_Main\Forza2\Main\Media\Src\cars\_Assets\Textures\Test\left.tga"
        right = "D:\P4\FMBase_Main\Forza2\Main\Media\Src\cars\_Assets\Textures\Test\right.tga"
        front = "D:\P4\FMBase_Main\Forza2\Main\Media\Src\cars\_Assets\Textures\Test\front.tga"
        bmaps = [wing,back,front,right,left,top]
        prev_mix = rt.Mix()
        for m in bmaps:
            curr_mix = rt.Mix()
            curr_mix.color1 = m
            curr_mix.color2 = m
        mat = rt.StandardMaterial()
        mat.diffuseMap = curr_mix
        mat.showInViewport = True



    




            
        