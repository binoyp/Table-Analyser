
from PyQt4.uic import loadUiType
from ui_TabAnalWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui	
from PyQt4.QtCore import *
import numpy as np
import ui_dlgSetting as dlgSetting
#Ui_MainWindow, QMainWindow = loadUiType('TabAnalWindow.ui')
from dakota_headerParser import headerParser




class dakota_tabfile:

    def __init__(self, fname, i_iter = 0, i_resp=[-1], i_vars = [1, 2]):
        try:
            f = open(fname, 'r')
        except IOError:
            print "file error"
        _line1 = f.readline()
        _l1split = _line1.split()
        self.vars = [_l1split[i_iter]] + [_l1split[i] for i in i_vars]
        self.vars2 = [_l1split[i] for i in i_vars]
        self.resps = [ _l1split[i] for i in i_resp]
        tempList = []
        resp = []
        for _l in f:
            _lspl = _l.split()
            tempList.append([int(_lspl[0])]+[float(_lspl[i]) for i in i_vars]\
            +[float(_lspl[i]) for i  in i_resp])
#            resp.append()
        hdr = self.vars + self.resps
        nrow = len(tempList)
        ncol = len(hdr)
        dtyp = zip(hdr, ['f8' for i in range(ncol)])
        self.data = np.array(tempList)
        self.data.dtype = dtyp
#        print self.data[self.resps[0]]
        
        
        
    def make_var_set( self, var):
        try:
            assert var in self.vars
            return set(self.data[var].flatten())
        except AssertionError:
            return None
        
    def filtervariable(self, var, ovardic, tol = 0.001):
        """
        var - var_value to be filterd
        ovardic - the other varibles values in a dictionary
        tol = tolerace for the filtering process
        """
        def subfun((var,val)):
            return np.abs(self.data[var] - val) < tol
        lst = map(subfun, ovardic.items())
#        print lst
        return self.data[var][reduce(lambda x, y: x & y, lst)]
        
        
        
        
        
        
        
        
class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        
        self.dlgS = dlgSetting.Ui_dlgSetting()
        self.dlgSetting = QtGui.QDialog(self)
        self.dlgS.setupUi(self.dlgSetting)
        self.objDic = {}
        self.flgused = 0
#        self.readSettings()
#        self.connect(self.cBoxVar,)
#           
            
    def readSettings(self):
        self.plotMarker = str(self.dlgS.cbMarker.currentText())
        self.plotStyle = str(self.dlgS.cbLineStyle.currentText())
        self.plotGrid = int(self.dlgS.cbGrid.currentText())
        
        
    @pyqtSignature("")
    
    def on_action_Open_triggered(self):
        
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    r'D:\Workshop\Dakota\script')
 
        f = open(self.fname, 'r')
        _line1 = f.readline()
        _l1split = _line1.split()
        gui = headerParser(_l1split)
        f.close()
#        gui.show()
        
        gui.exec_()
        ivars, resps = gui.returnvalues()
        print "RES", ivars, resps
        
        if self.flgused:
            self.cBoxVar.clear()
            self.cBoxXaxis.clear()
            self.cBoxYaxis.clear()
        else:
            self.flgused = 1
            
        self.lblOut.setText("file Opened:" + self.fname)
        self.Table = dakota_tabfile(self.fname, i_resp=resps, i_vars = ivars)
        self.cBoxXaxis.addItems(self.Table.vars)
        self.cBoxYaxis.addItems(self.Table.resps)
        self.cBoxVar.addItems(self.Table.vars2)
        
    @pyqtSignature("")        
    def on_actionPlot_Settings_triggered(self):
        print "Settings Trig"
        self.dlgSetting.show()
        
        
        
        
    @pyqtSignature("")
    def on_btnPlot_clicked(self):
        self.readSettings()
        print self.cBoxXaxis.currentText()
        print self.Table.vars
        if self.chkVar.isChecked():
            argDic = {it:float(self.objDic[it].currentText()) for it in self.objDic}
            print "argDic", argDic
            xdat = self.Table.filtervariable(str(self.cBoxVar.currentText()), \
            argDic)
            ydat = self.Table.filtervariable(str(self.cBoxYaxis.currentText()), \
            argDic)
            print 'x',xdat
            print 'y', ydat
            self.plotscatter(xdat, ydat, self.cBoxVar.currentText(),\
            self.cBoxYaxis.currentText())
        else:
            xdat = self.Table.data[str(self.cBoxXaxis.currentText())]
            ydat = self.Table.data[str(self.cBoxYaxis.currentText())]
            self.plotscatter(xdat, ydat,self.cBoxXaxis.currentText(), \
            self.cBoxYaxis.currentText())
                
 
    
    @pyqtSignature("int")
    def on_chkVar_stateChanged(self):
        print "Check var changed"

    @pyqtSignature("QString")
    def on_cBoxVar_currentIndexChanged(self):
        print "CBoxVar changed"
        if self.chkVar.isChecked():
            self.objDic =  {}
#            if not self.tempObj:
#                print "removing widgets"
            while self.formLay1.count()>2:
                item = self.formLay1.takeAt(2)
                item.widget().deleteLater()

            actVar = self.cBoxVar.currentText()
            
            remItem = self.Table.vars2[:]
            remItem.remove(actVar)
            for it in remItem:
                lbl = QtGui.QLabel(parent = self)
                lbl.setText(it)
                cbx = QtGui.QComboBox(parent = self)
                self.objDic[it] = cbx
                datlist = [str(v) for v in self.Table.make_var_set(it) ]
                self.objDic[it].addItems(datlist)
#                self.tempObj.append(lbl)
#                self.tempObj.append(cbx)
                self.formLay1.addRow(lbl, cbx)
                
    def plotscatter(self, xdat, ydat, xl, yl):
        
        self.mplwid.axes.plot(xdat, ydat, marker = self.plotMarker,\
        linestyle = self.plotStyle)
        self.mplwid.axes.set_xlabel(str(xl))
        self.mplwid.axes.set_ylabel(str(yl))
        self.mplwid.axes.grid(self.plotGrid)
        self.mplwid.draw()              

if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
#    d = dakota_tabfile(r"D:\Workshop\Dakota\script\tabular_out.dat")
#    print d.data['%eval_id']
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
#    print d.data.dtype
