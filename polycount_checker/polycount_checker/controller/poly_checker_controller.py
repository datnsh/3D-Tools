import sys, os, importlib, qtmax
path = os.path.dirname(__file__)
try:
    from config import TOOLS_PATH
except ImportError:
    TOOLS_PATH = ""
paths = [path, TOOLS_PATH]
for path in paths:
    if path not in sys.path:
        sys.path.append(path)
from ..view import poly_checker_ui as ui
from ..model import poly_checker_variables as variables
from ..model import poly_checker_utils as utils
mods = [ui,utils, variables]
for mod in mods:
    importlib.reload(mod)
from tracking_deco import time_saver
class PolyController():
    def __init__(self):
        mainWindow = qtmax.GetQMaxMainWindow()
        PolyController.instance = self
        self.ui = ui.PolyCheckerUI(parent=mainWindow)
        self.ui.close_last_instance(mainWindow, variables.UI_NAME)
        self.ui.setFloating(True)
        self.ui.setObjectName(variables.UI_NAME)
        self.ui.show()

        self.util = utils.PolyUtil()
        
        self.ui.check_btn.clicked.connect(self.on_check_btn_clicked)
        self.ui.clear_btn.clicked.connect(self.clear_check_table)
        self.update_file_type_ui(self.util.get_file_type())
        
    
    def set_file_type(self, fileType):
        self.util.set_file_type(fileType)
        self.update_file_type_ui(fileType)
    
    def update_file_type_ui(self, fileType):
        self.ui.radio_group.button(fileType).setChecked(True)

    def clear_check_table(self):
        self.ui.check_table.setRowCount(0) 
        self.util.reset_polyCount()
    
    @time_saver(seconds_saved=5.0, tool_name="UbiPolycountChecker")
    def on_check_btn_clicked(self):
        self.clear_check_table()
        self.set_file_type(self.ui.radio_group.checkedId())
        self.util.check_polycount()
        for lod_name, result in self.util.check_results.items(): # result = [polycount, status]
            polycount = str(result[self.util.count])
            status = result[self.util.status]
            diff = result[self.util.diff]
            self.ui.add_table_item(lod_name, polycount, status,diff)
            #row = self.ui.check_table.rowCount() - 1
            #statusItem = self.ui.check_table.item(row, 2)
            #color = self.get_item_color(status)
            #self.ui.set_item_color(statusItem ,color)