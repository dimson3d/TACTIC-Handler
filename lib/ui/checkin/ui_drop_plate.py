# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkin\ui_drop_plate.ui'
#
# Created: Sun Sep 11 00:28:02 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dropPlateGroupBox(object):
    def setupUi(self, dropPlateGroupBox):
        dropPlateGroupBox.setObjectName("dropPlateGroupBox")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dropPlateGroupBox.sizePolicy().hasHeightForWidth())
        dropPlateGroupBox.setSizePolicy(sizePolicy)
        dropPlateGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        dropPlateGroupBox.setFlat(True)
        self.gridLayout = QtGui.QGridLayout(dropPlateGroupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.clearPushButton = QtGui.QPushButton(dropPlateGroupBox)
        self.clearPushButton.setMinimumSize(QtCore.QSize(75, 0))
        self.clearPushButton.setObjectName("clearPushButton")
        self.gridLayout.addWidget(self.clearPushButton, 2, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        self.dropTreeWidget = QtGui.QTreeWidget(dropPlateGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropTreeWidget.sizePolicy().hasHeightForWidth())
        self.dropTreeWidget.setSizePolicy(sizePolicy)
        self.dropTreeWidget.setStyleSheet("QTreeView::item {\n"
"    padding: 2px;\n"
"}")
        self.dropTreeWidget.setAlternatingRowColors(True)
        self.dropTreeWidget.setRootIsDecorated(False)
        self.dropTreeWidget.setUniformRowHeights(True)
        self.dropTreeWidget.setItemsExpandable(False)
        self.dropTreeWidget.setAllColumnsShowFocus(True)
        self.dropTreeWidget.setHeaderHidden(False)
        self.dropTreeWidget.setObjectName("dropTreeWidget")
        self.dropTreeWidget.header().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.dropTreeWidget, 0, 0, 1, 6)
        self.fromDropListCheckBox = QtGui.QCheckBox(dropPlateGroupBox)
        self.fromDropListCheckBox.setObjectName("fromDropListCheckBox")
        self.gridLayout.addWidget(self.fromDropListCheckBox, 2, 0, 1, 1)
        self.fileTypeLabel = QtGui.QLabel(dropPlateGroupBox)
        self.fileTypeLabel.setObjectName("fileTypeLabel")
        self.gridLayout.addWidget(self.fileTypeLabel, 2, 2, 1, 1)
        self.groupCheckinCheckBox = QtGui.QCheckBox(dropPlateGroupBox)
        self.groupCheckinCheckBox.setObjectName("groupCheckinCheckBox")
        self.gridLayout.addWidget(self.groupCheckinCheckBox, 2, 1, 1, 1)
        self.fileTypeLineEdit = QtGui.QLineEdit(dropPlateGroupBox)
        self.fileTypeLineEdit.setObjectName("fileTypeLineEdit")
        self.gridLayout.addWidget(self.fileTypeLineEdit, 2, 3, 1, 1)

        self.retranslateUi(dropPlateGroupBox)
        QtCore.QMetaObject.connectSlotsByName(dropPlateGroupBox)

    def retranslateUi(self, dropPlateGroupBox):
        dropPlateGroupBox.setWindowTitle(QtGui.QApplication.translate("dropPlateGroupBox", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        dropPlateGroupBox.setTitle(QtGui.QApplication.translate("dropPlateGroupBox", "Drop Files/Folders/Sequences Here:", None, QtGui.QApplication.UnicodeUTF8))
        self.clearPushButton.setText(QtGui.QApplication.translate("dropPlateGroupBox", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.dropTreeWidget.setSortingEnabled(True)
        self.dropTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("dropPlateGroupBox", "File Names", None, QtGui.QApplication.UnicodeUTF8))
        self.dropTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("dropPlateGroupBox", "Type/Ext", None, QtGui.QApplication.UnicodeUTF8))
        self.dropTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("dropPlateGroupBox", "File Path", None, QtGui.QApplication.UnicodeUTF8))
        self.fromDropListCheckBox.setText(QtGui.QApplication.translate("dropPlateGroupBox", "From Droplist", None, QtGui.QApplication.UnicodeUTF8))
        self.fileTypeLabel.setText(QtGui.QApplication.translate("dropPlateGroupBox", "File Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupCheckinCheckBox.setText(QtGui.QApplication.translate("dropPlateGroupBox", "Group Checkin", None, QtGui.QApplication.UnicodeUTF8))
