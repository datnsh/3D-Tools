import bpy, bmesh
from bpy.types import PropertyGroup

class ScalePlaneProperties(bpy.types.PropertyGroup):
    source_face_object: bpy.props.StringProperty(
        name="Source Face Object", 
    ) # type: ignore
    source_face_area: bpy.props.FloatProperty(
        name="Source Face Area Value"
    ) # type: ignore

def register():
    bpy.utils.register_class(ScalePlaneProperties)
    bpy.types.Scene.scale_plane = bpy.props.PointerProperty(type=ScalePlaneProperties)
def unregister():
    del bpy.types.Scene.scale_plane
    bpy.utils.unregister_class(ScalePlaneProperties)