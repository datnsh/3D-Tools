bl_info = {
    "name": "Scale Plane",
    "author": "DatNguyen",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Scale Plane",
    "description": "Resize and align faces of a mesh by their normals",
    "category": "Object",
}

import os, sys
from importlib import reload
# Uncomment this to deploy
"""TOOL_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
TOOL_ROOT_PATH = TOOL_ROOT_PATH.replace("\\","/")
sys.path.append(TOOL_ROOT_PATH)"""

from .Model import Scale_Plane_Properties
from .Controller import Scale_Plane_Operators
from .View import Scale_Plane_UI

reload(Scale_Plane_Operators)
reload(Scale_Plane_UI)
reload(Scale_Plane_Properties)


def register():
    Scale_Plane_Operators.register()
    Scale_Plane_UI.register()
    Scale_Plane_Properties.register()


def unregister():
    Scale_Plane_Properties.unregister()
    Scale_Plane_UI.unregister()
    Scale_Plane_Operators.unregister()
