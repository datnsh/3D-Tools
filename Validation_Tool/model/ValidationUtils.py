from pymxs import runtime as rt
import re

class ValidationUtils():
    def check_sub_selection(obj):
        selection = rt.getSelectionLevel(obj)
        if(str(selection) != 'object'):
            return False
        return True
    def check_wheel_size(obj):
        pass
    def check_spindle_rotation(spindle):
        rotation = spindle.rotation
        rotation = rt.quatToEuler(rotation)
        if rotation.x != 0 or rotation.y != 0 or rotation.z != 0:
            return False
        else:
            return True
    def check_helpers():
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
    def check_blur_id(obj):
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
    def check_morph(obj):
        match = re.match(DNC.PATTERN, obj.name)
        if match:
            lod_part = match.group(2)
            string_lod = str(lod_part)
            morph_part = match.group(3)
            if(not match.group(3) and string_lod[-1] in DNC.lod_morph_list):
                modifier_count = obj.modifiers.count
                if(modifier_count == 0):
                    return False
                else:
                    top_modifier = obj.modifiers[modifier_count - 1]
                    modifier_class =str(rt.classOf(top_modifier))
                    if modifier_class !="Morpher":
                        return False
        return True
    def check_pivot(obj):
        pivot = obj.pivot
        buffer = 1e-3
        if(abs(pivot.x) < buffer and abs(pivot.y) < buffer and abs(pivot.z) < buffer):
            return (True, None)
        else:
            return (False, [pivot.x, pivot.y, pivot.z])
    def check_layer():
        layer_count = rt.LayerManager.count
        if layer_count > 1:
            return False
        #The commented code is for check the layers name if the project required multiple layers
        #current_layer = rt.LayerManager.getLayer(0)
        #if(current_layer.name != '0'):
            #return False, "The current layer has the wrong name"
        return True
    def check_isolation_active():
        return rt.IsolateSelection.IsolateSelectionModeActive()
    def check_asset_path():
        pass
    