"""UI Variables"""
TOOL_TITLE = 'Tool and Validation'
FIRST_TAB = 'Wheel Checker'
SECOND_TAB = 'Car Checker'
COMBO_BOX_LIST = ['S0','S','0','1','2','3','4','5']
FIRST_GROUP_BOX = 'LOD'
FIRST_CHECK_BOX = 'Hide spindle'
SECOND_CHECK_BOX = 'Hide morph'
THIRD_CHECK_BOX = 'Hide blur'
FOURTH_CHECK_BOX = 'Hide wheel'
SECOND_GROUP_BOX = 'Wheel Checklist'
FIRST_BTN_TEXT = 'Check Wheel'
SECOND_BTN_TEXT = ['Check Wheel Colors','Restore Materials']
THIRD_BTN_TEXT = ['Check UV2','Restore UV']
THIRD_GROUP_BOX = 'UV Checker'
"""Utilities Variables"""
NAME_PATTERN = r'^([a-zA-Z0-9]+)_LOD([a-zA-Z0-9]+)(?:_([a-zA-Z0-9]+))?$'
UV2CHECKER = "UV2Checker"
WHEELCOLOR = "WheelColor"



LOD_LIST = ['S0','S','0','1','2','3','4','5']
LOD_MORPH = ['S0','S','0','1']
""""""
NAME = 'name'
SPINDLE = 'spindle'
HELPERS = 'helpers'
SUB_SELECTION = 'sub_selection'
LAYER = 'layer'
ISOLATION = 'isolation'
PIVOT = 'pivot'
BLUR_ID = 'blurid'
MORPH = 'morph'
ISO_VERT = 'isolated vertices'

NAME_MSG = ["All objects has correct naming", " has wrong naming"]
BLUR_ID_MSG = ["Blur rims and blur lips have correct material ID"," has wrong ID"]
PIVOT_MSG = ["All objects have pivot at origin (0,0,0)"," pivot not at origin (0,0,0)"]
HELPER_MSG = ["Helper filter is correct","Helper is checked"]
SPINDLE_ROTATION_MSG = ["Spindle rotation is correct"," has rotation"]
ISOLATION_MSG = ["There is no isolated object", "There is isolated objects"]
LAYER_MSG = ["Layer hierarchy is correct", "There is extra layer"]
MORPH_MSG = ["All objects has correct morph modifier"," is missing morph modifier"]
SUB_SELECTION_MSG = ["All objects are in correct sub selection"," has sub selection"]
ISO_VERT_MSG = ["All objects have no isolated vertex", " has isolated vertices"]
ERROR_MSG = {
    NAME : NAME_MSG,
    SPINDLE: SPINDLE_ROTATION_MSG,
    HELPERS: HELPER_MSG,
    SUB_SELECTION: SUB_SELECTION_MSG,
    LAYER : LAYER_MSG,
    BLUR_ID: BLUR_ID_MSG,
    PIVOT : PIVOT_MSG,
    ISOLATION : ISOLATION_MSG,
    MORPH : MORPH_MSG,
    ISO_VERT:ISO_VERT_MSG,
}
""""""