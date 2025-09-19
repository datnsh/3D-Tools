from importlib import reload
import bpy
from bpy.types import Panel
import Extrude_Tools.Function.Extrude_Tools_Properties as Extrude_Tools_Properties
reload(Extrude_Tools_Properties)

class PANEL_PT_extrude_3dsMax(Panel):
    bl_idname = "PANEL_PT_extrude_3dsMax"
    bl_label = "Extrude 3ds Max"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Extrude Tools'

    def draw(self, context):
        scene = context.scene
        main_layout = self.layout.column(align=True)
        row = main_layout.row()
        row.operator("scene.extrude_3dsmax", text="Extrude 3ds Max")

class PANEL_PT_smart_extrude(bpy.types.Panel):
    bl_label = "Smart Extrude"
    bl_idname = "VIEW3D_PT_Extrude"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Extrude Tools"
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("scene.smart_extrude", text='Smart Extrude')

        


        
