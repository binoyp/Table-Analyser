# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workshop\Dakota\Table Analyser\TabAnalWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(823, 608)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblOut = QtGui.QLabel(self.centralwidget)
        self.lblOut.setObjectName(_fromUtf8("lblOut"))
        self.gridLayout.addWidget(self.lblOut, 5, 0, 1, 2)
        self.vlay1 = QtGui.QVBoxLayout()
        self.vlay1.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.vlay1.setObjectName(_fromUtf8("vlay1"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.vlay1.addWidget(self.label_3)
        self.chkVar = QtGui.QCheckBox(self.centralwidget)
        self.chkVar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.chkVar.setObjectName(_fromUtf8("chkVar"))
        self.vlay1.addWidget(self.chkVar)
        self.formLay1 = QtGui.QFormLayout()
        self.formLay1.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.formLay1.setObjectName(_fromUtf8("formLay1"))
        self.lblAnalyse = QtGui.QLabel(self.centralwidget)
        self.lblAnalyse.setObjectName(_fromUtf8("lblAnalyse"))
        self.formLay1.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblAnalyse)
        self.cBoxVar = QtGui.QComboBox(self.centralwidget)
        self.cBoxVar.setMinimumSize(QtCore.QSize(100, 0))
        self.cBoxVar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cBoxVar.setObjectName(_fromUtf8("cBoxVar"))
        self.formLay1.setWidget(1, QtGui.QFormLayout.FieldRole, self.cBoxVar)
        self.vlay1.addLayout(self.formLay1)
        self.gridLayout.addLayout(self.vlay1, 0, 1, 1, 1)
        self.btnQuit = QtGui.QPushButton(self.centralwidget)
        self.btnQuit.setMaximumSize(QtCore.QSize(200, 25))
        self.btnQuit.setObjectName(_fromUtf8("btnQuit"))
        self.gridLayout.addWidget(self.btnQuit, 1, 1, 1, 1)
        self.hl1 = QtGui.QHBoxLayout()
        self.hl1.setObjectName(_fromUtf8("hl1"))
        self.mplwid = MatplotlibWidget(self.centralwidget)
        self.mplwid.setObjectName(_fromUtf8("mplwid"))
        self.hl1.addWidget(self.mplwid)
        self.gridLayout.addLayout(self.hl1, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cBoxXaxis = QtGui.QComboBox(self.centralwidget)
        self.cBoxXaxis.setObjectName(_fromUtf8("cBoxXaxis"))
        self.horizontalLayout_3.addWidget(self.cBoxXaxis)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.cBoxYaxis = QtGui.QComboBox(self.centralwidget)
        self.cBoxYaxis.setObjectName(_fromUtf8("cBoxYaxis"))
        self.horizontalLayout_3.addWidget(self.cBoxYaxis)
        self.btnPlot = QtGui.QPushButton(self.centralwidget)
        self.btnPlot.setObjectName(_fromUtf8("btnPlot"))
        self.horizontalLayout_3.addWidget(self.btnPlot)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.actionPlot_Settings = QtGui.QAction(MainWindow)
        self.actionPlot_Settings.setObjectName(_fromUtf8("actionPlot_Settings"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Exit)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionPlot_Settings)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btnQuit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.action_Exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Dakota Table out analyser", None))
        self.lblOut.setText(_translate("MainWindow", "TextLabel", None))
        self.label_3.setText(_translate("MainWindow", "Filter", None))
        self.chkVar.setText(_translate("MainWindow", "Fix a Variable", None))
        self.lblAnalyse.setText(_translate("MainWindow", "Analyse", None))
        self.btnQuit.setText(_translate("MainWindow", "&Quit", None))
        self.label_2.setText(_translate("MainWindow", "x axis", None))
        self.label.setText(_translate("MainWindow", "y axis", None))
        self.btnPlot.setText(_translate("MainWindow", "&Plot", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Exit.setText(_translate("MainWindow", "&Exit", None))
        self.actionPlot_Settings.setText(_translate("MainWindow", "Plot Settings", None))

from matplotlibwidget import MatplotlibWidget
