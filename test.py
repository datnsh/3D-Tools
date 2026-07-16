import bpy
import sys
import importlib
# Point Python at the add-on folder
addon_dir = r"D:\DatNguyen\Projects\3D-Tools\Align_Normal"
if addon_dir not in sys.path:
    sys.path.insert(0, addon_dir)
  # Force reimport on every run
for key in list(sys.modules.keys()):
    if "Align_Normal" in key:
        del sys.modules[key]
import Controller.Align_Normal_Operators as ops
import View.Align_Normal_UI as ui
import Model.Align_Normal_Properties as props
props.register()
ops.register()
ui.register()
print("Registered OK")