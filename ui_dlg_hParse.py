# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workshop\Dakota\Table Analyser\dlg_hParse.ui'
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

class Ui_dlg_HeaderParser(object):
    def setupUi(self, dlg_HeaderParser):
        dlg_HeaderParser.setObjectName(_fromUtf8("dlg_HeaderParser"))
        dlg_HeaderParser.resize(378, 368)
        self.verticalLayout_2 = QtGui.QVBoxLayout(dlg_HeaderParser)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(dlg_HeaderParser)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.wid_lst_main = QtGui.QListWidget(dlg_HeaderParser)
        self.wid_lst_main.setObjectName(_fromUtf8("wid_lst_main"))
        self.verticalLayout.addWidget(self.wid_lst_main)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_Addvar = QtGui.QPushButton(dlg_HeaderParser)
        self.btn_Addvar.setObjectName(_fromUtf8("btn_Addvar"))
        self.horizontalLayout_2.addWidget(self.btn_Addvar)
        self.btn_AddResp = QtGui.QPushButton(dlg_HeaderParser)
        self.btn_AddResp.setObjectName(_fromUtf8("btn_AddResp"))
        self.horizontalLayout_2.addWidget(self.btn_AddResp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(dlg_HeaderParser)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(dlg_HeaderParser)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.btn_delVar = QtGui.QPushButton(dlg_HeaderParser)
        self.btn_delVar.setObjectName(_fromUtf8("btn_delVar"))
        self.gridLayout.addWidget(self.btn_delVar, 4, 0, 1, 1)
        self.btn_delResp = QtGui.QPushButton(dlg_HeaderParser)
        self.btn_delResp.setObjectName(_fromUtf8("btn_delResp"))
        self.gridLayout.addWidget(self.btn_delResp, 4, 1, 1, 1)
        self.wid_lstVar = QtGui.QListWidget(dlg_HeaderParser)
        self.wid_lstVar.setObjectName(_fromUtf8("wid_lstVar"))
        self.gridLayout.addWidget(self.wid_lstVar, 2, 0, 1, 1)
        self.wid_lstResp = QtGui.QListWidget(dlg_HeaderParser)
        self.wid_lstResp.setObjectName(_fromUtf8("wid_lstResp"))
        self.gridLayout.addWidget(self.wid_lstResp, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.btn_Acc = QtGui.QPushButton(dlg_HeaderParser)
        self.btn_Acc.setObjectName(_fromUtf8("btn_Acc"))
        self.verticalLayout.addWidget(self.btn_Acc)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dlg_HeaderParser)
        QtCore.QMetaObject.connectSlotsByName(dlg_HeaderParser)

    def retranslateUi(self, dlg_HeaderParser):
        dlg_HeaderParser.setWindowTitle(_translate("dlg_HeaderParser", "Choose Variables and Responses", None))
        self.label_3.setText(_translate("dlg_HeaderParser", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Dakota File Headers</span></p></body></html>", None))
        self.btn_Addvar.setText(_translate("dlg_HeaderParser", "Add To Variable", None))
        self.btn_AddResp.setText(_translate("dlg_HeaderParser", "Add to Response", None))
        self.label.setText(_translate("dlg_HeaderParser", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Variable</span></p></body></html>", None))
        self.label_2.setText(_translate("dlg_HeaderParser", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Responses</span></p></body></html>", None))
        self.btn_delVar.setText(_translate("dlg_HeaderParser", "Delete Selected Variable", None))
        self.btn_delResp.setText(_translate("dlg_HeaderParser", "Delete Selected Response", None))
        self.btn_Acc.setText(_translate("dlg_HeaderParser", "&OK", None))

