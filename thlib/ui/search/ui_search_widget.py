# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search/ui_search_widget.ui'
#
# Created: Fri Aug 17 09:38:55 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from thlib.side.Qt import QtWidgets as QtGui
from thlib.side.Qt import QtCore

class Ui_searchWidget(object):
    def setupUi(self, searchWidget):
        searchWidget.setObjectName("searchWidget")
        self.searchWidgetGridLayout = QtGui.QGridLayout(searchWidget)
        self.searchWidgetGridLayout.setContentsMargins(0, 0, 0, 0)
        self.searchWidgetGridLayout.setSpacing(0)
        self.searchWidgetGridLayout.setObjectName("searchWidgetGridLayout")
        self.expandingLayout = QtGui.QVBoxLayout()
        self.expandingLayout.setSpacing(0)
        self.expandingLayout.setObjectName("expandingLayout")
        self.searchWidgetGridLayout.addLayout(self.expandingLayout, 0, 1, 1, 1)
        self.gearMenuToolButton = QtGui.QToolButton(searchWidget)
        self.gearMenuToolButton.setMaximumSize(QtCore.QSize(22, 22))
        self.gearMenuToolButton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.gearMenuToolButton.setAutoRaise(True)
        self.gearMenuToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.gearMenuToolButton.setObjectName("gearMenuToolButton")
        self.searchWidgetGridLayout.addWidget(self.gearMenuToolButton, 0, 2, 1, 1)
        self.searchFiltersVerticalLayout = QtGui.QVBoxLayout()
        self.searchFiltersVerticalLayout.setSpacing(0)
        self.searchFiltersVerticalLayout.setObjectName("searchFiltersVerticalLayout")
        self.searchWidgetGridLayout.addLayout(self.searchFiltersVerticalLayout, 1, 0, 1, 3)
        self.searchWidgetGridLayout.setColumnStretch(0, 1)

        self.retranslateUi(searchWidget)
        QtCore.QMetaObject.connectSlotsByName(searchWidget)

    def retranslateUi(self, searchWidget):
        pass

