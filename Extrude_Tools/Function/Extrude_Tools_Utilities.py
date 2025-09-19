from importlib import reload
import bpy
import bmesh
from mathutils import Vector

def edge_push_dir(edge: bmesh.types.BMEdge) -> Vector:
    if edge.link_faces:
        n = sum((f.normal for f in edge.link_faces), Vector())
        if n.length > 0:
            return n.normalized()
    n = edge.verts[0].normal + edge.verts[1].normal
    return n .normalized() if n.length > 0 else Vector((0,0,1))