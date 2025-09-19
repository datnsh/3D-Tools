bl_info = {
    "name" : "Extrude_Tools",
    "author" : "dat.nguyen_b",
    "description" : "Toolset for common working tools in Blender",
    "blender" : (4,0,0),
    "version" : (0,0,1),
    "location" : "3D View",
    "warning" : "",
    "category" : "Object",
}
try:
    from imp import reload
except:
    reload
import bpy
import os
import sys
TOOL_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
TOOL_ROOT_PATH = TOOL_ROOT_PATH.replace("\\","/")
print(TOOL_ROOT_PATH)
sys.path.append(TOOL_ROOT_PATH)
import Extrude_Tools.Controller.Extrude_Tools_UI as Extrude_Tools_UI
import Extrude_Tools.Function.Extrude_Tools_Operators as Extrude_Tools_Operators
import Extrude_Tools.Function.Extrude_Tools_Properties as Extrude_Tools_Properties
modules = [Extrude_Tools_Properties, Extrude_Tools_Operators, Extrude_Tools_UI]

def register():
    for module in modules:
        reload(module)
    #-- register Properties --#
    bpy.utils.register_class(Extrude_Tools_Properties.Extrude_Custom_Properties)
    #-- register PANELs --#
    bpy.utils.register_class(Extrude_Tools_UI.PANEL_PT_extrude_3dsMax)
    bpy.utils.register_class(Extrude_Tools_UI.PANEL_PT_smart_extrude)
    #--register Operators --#
    bpy.utils.register_class(Extrude_Tools_Operators.OBJECT_OT_extrude_3dsMax)
    bpy.utils.register_class(Extrude_Tools_Operators.OBJECT_OT_smart_extrude)

def unregister():
    bpy.utils.unregister_class(Extrude_Tools_Properties.Extrude_Custom_Properties)
    bpy.utils.unregister_class(Extrude_Tools_UI.PANEL_PT_extrude_3dsMax)
    bpy.utils.unregister_class(Extrude_Tools_UI.PANEL_PT_smart_extrude)
    #-- unregister Operators --#
    bpy.utils.unregister_class(Extrude_Tools_Operators.OBJECT_OT_extrude_3dsMax)
    bpy.utils.unregister_class(Extrude_Tools_Operators.OBJECT_OT_smart_extrude)