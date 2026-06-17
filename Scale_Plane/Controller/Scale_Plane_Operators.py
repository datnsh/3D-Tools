import bpy, bmesh, math
from bpy.types import Operator

class OBJECT_OT_select_source_face(Operator):
    bl_idname = 'object.select_source_face'
    bl_label = "Select Source Face"
    bl_description = "Select the source face for alignment operations"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, "Active object must be a mesh")
            return {'CANCELLED'}

        if obj.mode != 'EDIT':
            self.report({'ERROR'}, "Object must be in Edit Mode")
            return {'CANCELLED'}

        bm = bmesh.from_edit_mesh(obj.data)
        active_face = bm.faces.active

        if not active_face:
            self.report({'WARNING'}, "Select a face first")
            return {'CANCELLED'}

        # Store the index of the first selected face as the source face
        context.scene.scale_plane.source_face_area = active_face.calc_area()

        self.report({'INFO'}, f"Selected face {context.scene.scale_plane.source_face_area} as source face")
        return {'FINISHED'}

class OBJECT_OT_resize_faces_uniform(Operator):
    bl_idname = 'object.resize_faces_uniform'
    bl_label = "Resize Faces Uniform"
    bl_description = (
        "Scale each selected face around its own center so all faces "
        "reach the same average radius, preserving their position and normal"
    )
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, "Active object must be a mesh")
            return {'CANCELLED'}


        if obj.mode != 'EDIT':
            self.report({'ERROR'}, "Must be in Edit Mode")
            return {'CANCELLED'}
        source_area = context.scene.scale_plane.source_face_area
        bm = bmesh.from_edit_mesh(obj.data)
        selected_faces = [f for f in bm.faces if f.select]

        if not selected_faces:
            self.report({'WARNING'}, "No faces to operate on")
            return {'CANCELLED'}
        
        for face in selected_faces:
            current_area = face.calc_area()
            scale = math.sqrt(source_area / current_area)
            center = face.calc_center_median()
            for v in face.verts:
                v.co = center + (v.co - center) * scale
        bmesh.update_edit_mesh(obj.data)
        return {'FINISHED'}


classes = [
    OBJECT_OT_resize_faces_uniform,
    OBJECT_OT_select_source_face,
]


def register():
    """bpy.types.Scene.source_face_area = bpy.props.FloatProperty(
        name="Source Face Area",
        description="Area of the picked source face",
        default = -1.0,
    )"""
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    #del bpy.types.Scene.source_face_area
