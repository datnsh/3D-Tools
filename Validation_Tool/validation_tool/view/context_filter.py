import sys
from PySide2 import QtWidgets, QtCore
class ContextMenuFilter(QtWidgets.QObject):
    def eventFilter(self,obj,event):
        menu = QMenu(obj)
