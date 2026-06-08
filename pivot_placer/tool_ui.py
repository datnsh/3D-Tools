from PySide2 import QtCore, QtWidgets, QtGui

class Ui_Widget(QtWidgets.QDockWidget):
    def setupUi(self, Widget):
        #Overall Top Layout
        Widget.resize(340, 182)
        self.mainWidget = QtWidgets.QWidget(Widget)
        Widget.setWidget(self.mainWidget)
        self.vLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.vLayout.setObjectName(u"vLayout")
        self.vLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.vLayout.setContentsMargins(0, 0, 0, 0)
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName(u"hLayout")
        #-----------------------
        #Source Layout (List, Get Source Button)
        self.sourceVerticalLayout = QtWidgets.QVBoxLayout()
        self.sourceVerticalLayout.setSpacing(6)
        self.sourceVerticalLayout.setObjectName(u"sourceVerticalLayout")
        self.sourceTable = QtWidgets.QListWidget(self.mainWidget)
        self.sourceTable.setObjectName(u"sourceTable")
        self.sourceVerticalLayout.addWidget(self.sourceTable)
        self.getSourceButton = QtWidgets.QPushButton(self.mainWidget)
        self.getSourceButton.setObjectName(u"getSourceButton")
        self.sourceVerticalLayout.addWidget(self.getSourceButton)

        self.hLayout.addLayout(self.sourceVerticalLayout)
        #------------------------------------------------
        self.buttonVerticalLayout = QtWidgets.QVBoxLayout()
        self.swapButton = QtWidgets.QPushButton(self.mainWidget)
        self.swapButton.setObjectName(u"swapButton")
        self.clearButton = QtWidgets.QPushButton(self.mainWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.buttonVerticalLayout.setSpacing(4)
        self.buttonVerticalLayout.addStretch(1)
        self.buttonVerticalLayout.addWidget(self.swapButton)
        self.buttonVerticalLayout.addWidget(self.clearButton)
        self.buttonVerticalLayout.addStretch(1)
        self.hLayout.addLayout(self.buttonVerticalLayout)

        #------------------------------------------------
        
        self.targetVerticalLayout = QtWidgets.QVBoxLayout()
        self.targetVerticalLayout.setObjectName(u"targetVerticalLayout")
        self.targetTable = QtWidgets.QListWidget(self.mainWidget)
        self.targetTable.setObjectName(u"targetTable")
        self.targetVerticalLayout.addWidget(self.targetTable)
        self.getTargetButton = QtWidgets.QPushButton(self.mainWidget)
        self.getTargetButton.setObjectName(u"getTargetButton")
        self.targetVerticalLayout.addWidget(self.getTargetButton)
        self.hLayout.addLayout(self.targetVerticalLayout)
        #--------------------

        self.vLayout.addLayout(self.hLayout)
        self.copyButton = QtWidgets.QPushButton(self.mainWidget)
        self.copyButton.setObjectName(u"copyButton")
        self.vLayout.addWidget(self.copyButton)
        

        self.retranslateUi(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtCore.QCoreApplication.translate("Widget", u"Transfer Pivots", None))
        self.swapButton.setText(QtCore.QCoreApplication.translate("Widget", u"Swap", None))
        self.copyButton.setText(QtCore.QCoreApplication.translate("Widget", u"Copy Pivots", None))
        self.getTargetButton.setText(QtCore.QCoreApplication.translate("Widget", u"Get Target", None))
        self.getSourceButton.setText(QtCore.QCoreApplication.translate("Widget", u"Get Source", None))
        self.clearButton.setText(QtCore.QCoreApplication.translate("Widget", u"Clear", None))
