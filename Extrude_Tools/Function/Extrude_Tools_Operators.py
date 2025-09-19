from importlib import reload
from mathutils import Vector
import bpy, bmesh
from bpy.props import FloatProperty, BoolProperty
from bpy.types import Operator
import Extrude_Tools.Function.Extrude_Tools_Utilities as Extrude_Tools_Utilities
reload(Extrude_Tools_Utilities)

class OBJECT_OT_extrude_3dsMax(Operator):
    bl_idname = 'scene.extrude_3dsmax'
    bl_label = "Extrude current edge"
    bl_description ="Click to extrude current edge"
    bl_options = {'REGISTER', 'UNDO'}
    height: FloatProperty(name="Height", default=0.001)
    width: FloatProperty(name="Width", default=0.001, min=-1.0,max=1.0) 
    cap_endpoint: BoolProperty(name="Cap Endpoint",default=True)
    original_edge_indices: list[int] = []

    def execute(self, context):
        obj = context.active_object
        if not (obj and obj.type =='MESH' and context.mode == 'EDIT_MESH'):
            self.report({'ERROR'}, "Edit Mode on a mesh object is required")
            return {'CANCELLED'}
        
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        bm.edges.ensure_lookup_table()
        if not self.original_edge_indices:
            sel_edges = [e for e in bm.edges if e.select]
            if not sel_edges:
                self.report({'ERROR'},"Select one edge first")
                return {'CANCELLED'}
            self.original_edge_indices = [e.index for e in sel_edges]
        
        bpy.ops.mesh.select_mode(use_extend=True, use_expand=False, type='EDGE')
        bpy.ops.mesh.offset_edge_loops_slide('EXEC_DEFAULT',
            MESH_OT_offset_edge_loops={"use_cap_endpoint":self.cap_endpoint},
            TRANSFORM_OT_edge_slide={"value":self.width}
        )
        bm = bmesh.from_edit_mesh(me)
        bm.edges.ensure_lookup_table()
        for index in self.original_edge_indices:
            if index >= len(bm.edges):
                continue
            edge = bm.edges[index]
            push_dir = Extrude_Tools_Utilities.edge_push_dir(edge)
            move_vec = push_dir * self.height
            for v in edge.verts:
                v.co += move_vec
        bmesh.update_edit_mesh(me, loop_triangles=False, destructive=False)
        
        return {'FINISHED'}

class OBJECT_OT_smart_extrude(bpy.types.Operator):
	bl_idname = "scene.smart_extrude"
	bl_label = "Smart Extrude"    
	bl_description = "Perform extrusion similar to 3ds Max extrusion"
	bl_options = {"REGISTER", "UNDO"}
	
	thicknessNum : bpy.props.FloatProperty(name="Thickness", description="offset", default=0.2, min = 0.0001)
	depthNum : bpy.props.FloatProperty(name="Depth/height", default=0.2)
	bevelNum : bpy.props.FloatProperty(name="Bevel", default=0.1, min=0)
	bevelSlideNum : bpy.props.FloatProperty(name="Bevel_Slide", default=0.0)
	
	def draw(self, context):
		layout = self.layout
		layout.prop(self, "thicknessNum")
		layout.prop(self, "depthNum")
		layout.prop(self, "bevelNum")
		layout.prop(self, "bevelSlideNum")

	@classmethod
	def poll(cls, context):
		return	bpy.context.mode =='EDIT_MESH'
	
	def execute(self, context):
		try:
			Obj = bpy.context.object.select_get()
			currentMode = bpy.context.mode

			if Obj == True and currentMode == 'EDIT_MESH':
				bpy.ops.transform.edge_slide(value=self.bevelSlideNum, mirror=False, correct_uv=False)

				bpy.ops.mesh.bevel(
						offset=self.thicknessNum/2,
						segments=0
						)

				thk = self.bevelNum if self.bevelNum <= self.thicknessNum/2 else self.thicknessNum/2

				bpy.ops.mesh.inset(thickness=thk , depth=self.depthNum)

		except TypeError as E:
			self.report({'ERROR'},str(E))
		return {"FINISHED"}