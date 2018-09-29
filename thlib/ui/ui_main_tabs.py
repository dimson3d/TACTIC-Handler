# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_main_tabs.ui'
#
# Created: Fri Jun  8 17:27:04 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from thlib.side.Qt import QtWidgets as QtGui
from thlib.side.Qt import QtCore

class Ui_mainTabsForm(object):
    def setupUi(self, mainTabsForm):
        mainTabsForm.setObjectName("mainTabsForm")
        self.mainTabsLayout = QtGui.QGridLayout(mainTabsForm)
        self.mainTabsLayout.setContentsMargins(6, 0, 0, 0)
        self.mainTabsLayout.setObjectName("mainTabsLayout")
        self.main_tabWidget = QtGui.QTabWidget(mainTabsForm)
        self.main_tabWidget.setStyleSheet("#main_tabWidget::pane {\n"
"    border: 0px;\n"
"}\n"
"#main_tabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"#main_tabWidget > QTabBar::tab {\n"
"    background: transparent;\n"
"    border: 2px solid transparent;\n"
"    border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    padding: 4px;\n"
"}\n"
"#main_tabWidget > QTabBar::tab:selected, #main_tabWidget > QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 rgba(255, 255, 255, 48), stop: 1 rgba(255, 255, 255, 32));\n"
"}\n"
"\n"
"#main_tabWidget > QTabBar::tab:selected {\n"
"    border-color: transparent;\n"
"}\n"
"#main_tabWidget > QTabBar::tab:!selected {\n"
"    margin-top: 0px;\n"
"}")
        self.main_tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.main_tabWidget.setObjectName("main_tabWidget")
        self.checkInOutTab = QtGui.QWidget()
        self.checkInOutTab.setObjectName("checkInOutTab")
        self.checkInOutLayout = QtGui.QVBoxLayout(self.checkInOutTab)
        self.checkInOutLayout.setSpacing(0)
        self.checkInOutLayout.setContentsMargins(0, 0, 0, 0)
        self.checkInOutLayout.setObjectName("checkInOutLayout")
        self.main_tabWidget.addTab(self.checkInOutTab, "")
        self.myTacticTab = QtGui.QWidget()
        self.myTacticTab.setObjectName("myTacticTab")
        self.myTacticLayout = QtGui.QVBoxLayout(self.myTacticTab)
        self.myTacticLayout.setSpacing(0)
        self.myTacticLayout.setContentsMargins(0, 0, 0, 0)
        self.myTacticLayout.setObjectName("myTacticLayout")
        self.main_tabWidget.addTab(self.myTacticTab, "")
        self.assetsBrowserTab = QtGui.QWidget()
        self.assetsBrowserTab.setObjectName("assetsBrowserTab")
        self.assetsBrowserLayout = QtGui.QVBoxLayout(self.assetsBrowserTab)
        self.assetsBrowserLayout.setSpacing(0)
        self.assetsBrowserLayout.setContentsMargins(0, 0, 0, 0)
        self.assetsBrowserLayout.setObjectName("assetsBrowserLayout")
        self.main_tabWidget.addTab(self.assetsBrowserTab, "")
        self.mainTabsLayout.addWidget(self.main_tabWidget, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(28, -1, 10, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.skeyLineEdit = QtGui.QLineEdit(mainTabsForm)
        self.skeyLineEdit.setStyleSheet("QLineEdit {\n"
"    border: 0px;\n"
"    border-radius: 8px;\n"
"    show-decoration-selected: 1;\n"
"    padding: 0px 8px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 64), stop:1 rgba(255, 255, 255, 0));\n"
"    background-position: bottom left;\n"
"    background-image: url(\":/ui_check/gliph/search_16.png\");\n"
"    background-repeat: fixed;\n"
"    selection-background-color: darkgray;\n"
"    padding-left: 15px;\n"
"}\n"
"QLineEdit:hover{\n"
"    color: white;\n"
"    background-image: url(\":/ui_check/gliph/searchHover_16.png\");\n"
"}")
        self.skeyLineEdit.setObjectName("skeyLineEdit")
        self.verticalLayout_2.addWidget(self.skeyLineEdit)
        self.mainTabsLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 2)

        self.retranslateUi(mainTabsForm)
        self.main_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainTabsForm)

    def retranslateUi(self, mainTabsForm):
        mainTabsForm.setWindowTitle(u"Form")
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.checkInOutTab), u"Checkin / Checkout")
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.myTacticTab), u"My Tactic")
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.assetsBrowserTab), u"Assets browser")
        self.skeyLineEdit.setText(u"skey://")

