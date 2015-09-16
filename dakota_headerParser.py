# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:46:59 2015

@author: Binoy
"""

from ui_dlg_hParse import Ui_dlg_HeaderParser
from PyQt4 import QtGui	
from PyQt4.QtCore import *

class headerParser(QtGui.QDialog, Ui_dlg_HeaderParser):
    def __init__(self, inpList, parent = None):
        super(headerParser, self).__init__()
        self.setupUi(self)
        self.indexDic ={}
        for (num, val) in enumerate(inpList):
            self.indexDic[val] = num
            
        self.wid_lst_main.addItems(inpList)
#        self.show()
        
    @pyqtSignature("bool")
    def on_btn_Addvar_clicked(self):
        print "button Var click"
#        if self.wid_lst_main.isItemSelected()
        self.wid_lstVar.addItem(self.wid_lst_main.takeItem(self.wid_lst_main.currentRow()))
    
    @pyqtSignature("")
    def on_btn_AddResp_clicked(self):    
        self.wid_lstResp.addItem(self.wid_lst_main.takeItem(self.wid_lst_main.currentRow()))
        
    @pyqtSignature("")
    def on_btn_delResp_clicked(self):
        self.wid_lst_main.addItem(self.wid_lstResp.takeItem(self.wid_lstResp.currentRow()))
        
    @pyqtSignature("")
    def on_btn_delVar_clicked(self):
        self.wid_lst_main.addItem(self.wid_lstVar.takeItem(self.wid_lstVar.currentRow()))        
        
    @pyqtSignature("")
    def on_btn_Acc_clicked(self):
        print "closing"
        self.close()

        
        
    def returnvalues(self):
        _var =[]
        for i in range(self.wid_lstVar.count()):
            _var.append(self.indexDic[str(self.wid_lstVar.item(i).text())])
        _resp = []
        for i in range(self.wid_lstResp.count()):
            _resp.append(self.indexDic[str(self.wid_lstResp.item(i).text())])
#        self.close()
        return  _var, _resp        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    lst ="%eval_id             x1             x2         obj_fn ".split()
    gui = headerParser(lst)
    gui.show()
    
    app.exec_()
    if gui.result() == 0:
        print gui.returnvalues()
    d = raw_input("dd")