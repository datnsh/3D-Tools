import bpy
from bpy.types import Panel


class VIEW3D_PT_scale_plane(Panel):
    bl_label = "Scale Plane"
    bl_idname = "VIEW3D_PT_scale_plane"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Scale Plane"

    def draw(self, context):
        layout = self.layout
        layout.operator('object.select_source_face', text="Select Source Face")
        layout.operator('object.resize_faces_uniform', text="Resize Faces Uniform")

classes = [VIEW3D_PT_scale_plane]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
