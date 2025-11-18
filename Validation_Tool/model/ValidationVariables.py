NAME_PATTERN = ''

LOD_LIST = ['S0','S','0','1','2','3','4','5']

LOD_MORPH = ['S0','S','0','1']

NAME_CHECK_MSG = "All objects has correct naming"
BLUR_ID_CHECK_MSG = "Blur rims and blur lips have correct material ID"
PIVOT_CHECK_MSG = "All objects have pivot at origin (0,0,0)"
HELPER_CHECK_MSG = "Helper filter is correct"
SPINDLE_CHECK_MSG = "Spindle rotation is correct"
ISOLATION_CHECK_MSG = "There is no isolated object"
LAYER_CHECK_MSG = "Layer hierarchy is correct"
MORPH_CHECK_MSG = "All objects has correct morph modifier"
SUB_SELECTION_MSG = "All objects are in correct sub selection"

CHECK_LIST = {
    SPINDLE_CHECK_MSG: True,
    NAME_CHECK_MSG: True,
    BLUR_ID_CHECK_MSG: True,
    PIVOT_CHECK_MSG: True,
    HELPER_CHECK_MSG: True,
    ISOLATION_CHECK_MSG: True,
    MORPH_CHECK_MSG: True,
    SUB_SELECTION_MSG: True
}
