# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workshop\Dakota\Table Analyser\dlgSetting.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dlgSetting(object):
    def setupUi(self, dlgSetting):
        dlgSetting.setObjectName(_fromUtf8("dlgSetting"))
        dlgSetting.resize(174, 147)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlgSetting.sizePolicy().hasHeightForWidth())
        dlgSetting.setSizePolicy(sizePolicy)
        dlgSetting.setMinimumSize(QtCore.QSize(174, 147))
        dlgSetting.setMaximumSize(QtCore.QSize(174, 147))
        self.verticalLayout = QtGui.QVBoxLayout(dlgSetting)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(dlgSetting)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.cbMarker = QtGui.QComboBox(dlgSetting)
        self.cbMarker.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cbMarker.setObjectName(_fromUtf8("cbMarker"))
        self.cbMarker.addItem(_fromUtf8(""))
        self.cbMarker.addItem(_fromUtf8(""))
        self.cbMarker.addItem(_fromUtf8(""))
        self.cbMarker.addItem(_fromUtf8(""))
        self.cbMarker.addItem(_fromUtf8(""))
        self.cbMarker.addItem(_fromUtf8(""))
        self.cbMarker.addItem(_fromUtf8(""))
        self.cbMarker.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbMarker, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(dlgSetting)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.cbLineStyle = QtGui.QComboBox(dlgSetting)
        self.cbLineStyle.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cbLineStyle.setObjectName(_fromUtf8("cbLineStyle"))
        self.cbLineStyle.addItem(_fromUtf8(""))
        self.cbLineStyle.addItem(_fromUtf8(""))
        self.cbLineStyle.addItem(_fromUtf8(""))
        self.cbLineStyle.addItem(_fromUtf8(""))
        self.cbLineStyle.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbLineStyle, 0, 2, 1, 1)
        self.cbGrid = QtGui.QComboBox(dlgSetting)
        self.cbGrid.setObjectName(_fromUtf8("cbGrid"))
        self.cbGrid.addItem(_fromUtf8(""))
        self.cbGrid.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbGrid, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(dlgSetting)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(dlgSetting)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dlgSetting)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dlgSetting.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dlgSetting.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgSetting)

    def retranslateUi(self, dlgSetting):
        dlgSetting.setWindowTitle(_translate("dlgSetting", "Settings", None))
        self.label.setText(_translate("dlgSetting", "<html><head/><body><p align=\"right\">Line Style</p></body></html>", None))
        self.cbMarker.setItemText(0, _translate("dlgSetting", "o", None))
        self.cbMarker.setItemText(1, _translate("dlgSetting", "x", None))
        self.cbMarker.setItemText(2, _translate("dlgSetting", "s", None))
        self.cbMarker.setItemText(3, _translate("dlgSetting", "+", None))
        self.cbMarker.setItemText(4, _translate("dlgSetting", "^", None))
        self.cbMarker.setItemText(5, _translate("dlgSetting", "p", None))
        self.cbMarker.setItemText(6, _translate("dlgSetting", "D", None))
        self.cbMarker.setItemText(7, _translate("dlgSetting", "v", None))
        self.label_2.setText(_translate("dlgSetting", "<html><head/><body><p align=\"right\">Marker</p></body></html>", None))
        self.cbLineStyle.setItemText(0, _translate("dlgSetting", "-", None))
        self.cbLineStyle.setItemText(1, _translate("dlgSetting", " ", None))
        self.cbLineStyle.setItemText(2, _translate("dlgSetting", "--", None))
        self.cbLineStyle.setItemText(3, _translate("dlgSetting", "-:", None))
        self.cbLineStyle.setItemText(4, _translate("dlgSetting", ":", None))
        self.cbGrid.setItemText(0, _translate("dlgSetting", "0", None))
        self.cbGrid.setItemText(1, _translate("dlgSetting", "1", None))
        self.label_3.setText(_translate("dlgSetting", "<html><head/><body><p align=\"right\">Grid</p></body></html>", None))

