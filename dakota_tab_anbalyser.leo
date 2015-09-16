<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="bin.20150912113354.2" a="E"><vh>Dakota Table Analyse GUI</vh>
<v t="bin.20150912113443.1" a="E"><vh>@auto ui_TabAnalWindow.py</vh></v>
<v t="bin.20150912113628.1" a="E"><vh>@clean tab_anal.py</vh>
<v t="bin.20150912114036.1"><vh>imports and declarations</vh></v>
<v t="bin.20150912132556.1" a="E"><vh>class dakota_tab_file</vh>
<v t="bin.20150912132627.1"><vh>init</vh></v>
<v t="bin.20150912151924.1"><vh>get_var_sets</vh></v>
<v t="bin.20150912154225.1"><vh>customFiler</vh></v>
</v>
<v t="bin.20150912113853.1" a="E"><vh>class Main</vh>
<v t="bin.20150912122535.1"><vh>init</vh></v>
<v t="bin.20150912124601.1"><vh>fileopen</vh></v>
<v t="bin.20150912203408.1"><vh>buttonclick</vh></v>
</v>
</v>
</v>
<v t="bin.20150912203711.1" a="E"><vh>Recovered Nodes</vh>
<v t="bin.20150912203711.2"><vh>Recovered node "class Main" from @clean tab_anal.py</vh>
<v t="bin.20150912203711.3"><vh>old:class Main</vh></v>
<v t="bin.20150912203711.4"><vh>new:class Main</vh></v>
</v>
<v t="bin.20150912203711.5"><vh>Recovered node "init" from @clean tab_anal.py</vh>
<v t="bin.20150912203711.6"><vh>old:init</vh></v>
<v t="bin.20150912203711.7"><vh>new:init</vh></v>
</v>
<v t="bin.20150912203711.8"><vh>Recovered node "fileopen" from @clean tab_anal.py</vh>
<v t="bin.20150912203711.9"><vh>old:fileopen</vh></v>
<v t="bin.20150912203711.10"><vh>new:fileopen</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="bin.20150912113354.2"></t>
<t tx="bin.20150912113628.1">@language python
@tabwidth -4 

@others

if __name__ == '__main__':
    import sys
    from PyQt4 import QtGui
    d = dakota_tabfile(r"D:\Workshop\Dakota\script\tabular_out.dat")
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
#    print d.filtervariable('v1',{'v2':-500.0, 'v3':-100.0, 'v4':-60.0, 'v5':-20.0})
</t>
<t tx="bin.20150912113853.1">class Main(QtGui.QMainWindow, Ui_MainWindow):
    @others
        self.mplwid.axes.set_xlabel(self.cBoxXaxis.currentText)
        self.mplwid.axes.set_ylabel(self.cBoxYaxis.currentText)   
   

    


</t>
<t tx="bin.20150912114036.1">from PyQt4.uic import loadUiType
from ui_TabAnalWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui	
from PyQt4.QtCore import *
import numpy as np

#Ui_MainWindow, QMainWindow = loadUiType('TabAnalWindow.ui')





</t>
<t tx="bin.20150912122535.1">def __init__(self, ):
    super(Main, self).__init__()
    self.setupUi(self)
    
    x=[0,10,100]
    y=[3,4,5]
            
    #        self.mplwid.axes.set_xscale('log') # Nothing Happens 
    
\\-4.#        self.mplwid.axes.set_visible(0)
\\-4.#        ax1= self.mplwid.figure.add_subplot(211)
\\-4.#        ax1.plot(x,y)
\\-4.#        self.mplwid.figure.suptitle(r"$\alpha + \gamma = \rho$")
\\-4.#        ax1.grid(1)
\\-4.#        ax2= self.mplwid.figure.add_subplot(212)
\\-4.#        
\\-4.#        
\\-4.#        ax2.plot(x,y)
\\-4.#        
\\-4.#        ax2.grid(1)

    #        self.mplwid.draw()
    
</t>
<t tx="bin.20150912124601.1">@pyqtSignature("")
def on_action_Open_triggered(self):
    self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                r'D:\Workshop\Dakota\script')
    self.lblOut.setText("file Opened:" + self.fname)
    data = dakota_tabfile(self.fname)
     


</t>
<t tx="bin.20150912132556.1">class dakota_tabfile:
    @others
</t>
<t tx="bin.20150912132627.1">
def __init__(self, fname, i_iter = 0, i_resp=[-1], i_vars = [2, 6]):
    try:
        f = open(fname, 'r')
    except IOError:
        print "file error"
    _line1 = f.readline()
    _l1split = _line1.split()
    self.vars = _l1split[i_vars[0]:i_vars[1]+1]
    self.resps = [ _l1split[i] for i in i_resp]
    tempList = []
    resp = []
    for _l in f:
        _lspl = _l.split()
        tempList.append([float(_lspl[i]) for i in range(i_vars[0],\
        i_vars[1]+1)]+[float(_lspl[i]) for i  in i_resp])
\\-4.#            resp.append()
    hdr = self.vars + self.resps
    nrow = len(tempList)
    ncol = len(hdr)
    dtyp = zip(hdr, ['f8' for i in range(ncol)])
    self.data = np.array(tempList)
    self.data.dtype = dtyp
\\-4.#        print self.data[self.resps[0]]
    
    
        
        
    
    
</t>
<t tx="bin.20150912151924.1">def make_var_set( self, var):
    try:
        assert var in self.vars
        return set(self.data[var].flatten())
    except AssertionError:
        return None
    
</t>
<t tx="bin.20150912154225.1">def filtervariable(self, var, ovardic, tol = 0.001):
    def subfun((var,val)):
        return np.abs(self.data[var] - val) &lt; tol
    lst = map(subfun, ovardic.items())
    return self.data[var][reduce(lambda x, y: x &amp; y, lst)]
    
</t>
<t tx="bin.20150912203408.1">@pyqtSignature("")
def on_btnPlot_clicked():
    
</t>
<t tx="bin.20150912203711.1"></t>
<t tx="bin.20150912203711.10">@pyqtSignature("")
def on_action_Open_triggered(self):
    self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                r'D:\Workshop\Dakota\script')
    self.lblOut.setText("file Opened:" + self.fname)
    data = dakota_tabfile(self.fname)
     

@pyqtSignature("")
</t>
<t tx="bin.20150912203711.2">(uncached) bin.20150912113853.1
Diff...
  class Main(QtGui.QMainWindow, Ui_MainWindow):
      @others
+    
-         self.mplwid.axes.set_xlabel(self.cBoxXaxis.currentText)
-         self.mplwid.axes.set_ylabel(self.cBoxYaxis.currentText)   
     
  
      
  
  
</t>
<t tx="bin.20150912203711.3">class Main(QtGui.QMainWindow, Ui_MainWindow):
    @others
   
   

    


</t>
<t tx="bin.20150912203711.4">class Main(QtGui.QMainWindow, Ui_MainWindow):
    @others
        self.mplwid.axes.set_xlabel(self.cBoxXaxis.currentText)
        self.mplwid.axes.set_ylabel(self.cBoxYaxis.currentText)   
   

    


</t>
<t tx="bin.20150912203711.5">(uncached) bin.20150912122535.1
Diff...
  def __init__(self, ):
      super(Main, self).__init__()
      self.setupUi(self)
      
      x=[0,10,100]
      y=[3,4,5]
              
      #        self.mplwid.axes.set_xscale('log') # Nothing Happens 
      
  \\-4.#        self.mplwid.axes.set_visible(0)
  \\-4.#        ax1= self.mplwid.figure.add_subplot(211)
  \\-4.#        ax1.plot(x,y)
  \\-4.#        self.mplwid.figure.suptitle(r"$\alpha + \gamma = \rho$")
  \\-4.#        ax1.grid(1)
  \\-4.#        ax2= self.mplwid.figure.add_subplot(212)
  \\-4.#        
  \\-4.#        
  \\-4.#        ax2.plot(x,y)
  \\-4.#        
  \\-4.#        ax2.grid(1)
- 
+     self.mplwid.axes.set_xlabel('b')
+     self.mplwid.axes.set_title('GRAPH')
      #        self.mplwid.draw()
      
</t>
<t tx="bin.20150912203711.6">def __init__(self, ):
    super(Main, self).__init__()
    self.setupUi(self)
    
    x=[0,10,100]
    y=[3,4,5]
            
    #        self.mplwid.axes.set_xscale('log') # Nothing Happens 
    
\\-4.#        self.mplwid.axes.set_visible(0)
\\-4.#        ax1= self.mplwid.figure.add_subplot(211)
\\-4.#        ax1.plot(x,y)
\\-4.#        self.mplwid.figure.suptitle(r"$\alpha + \gamma = \rho$")
\\-4.#        ax1.grid(1)
\\-4.#        ax2= self.mplwid.figure.add_subplot(212)
\\-4.#        
\\-4.#        
\\-4.#        ax2.plot(x,y)
\\-4.#        
\\-4.#        ax2.grid(1)
    self.mplwid.axes.set_xlabel('b')
    self.mplwid.axes.set_title('GRAPH')
    #        self.mplwid.draw()
    
</t>
<t tx="bin.20150912203711.7">def __init__(self, ):
    super(Main, self).__init__()
    self.setupUi(self)
    
    x=[0,10,100]
    y=[3,4,5]
            
    #        self.mplwid.axes.set_xscale('log') # Nothing Happens 
    
\\-4.#        self.mplwid.axes.set_visible(0)
\\-4.#        ax1= self.mplwid.figure.add_subplot(211)
\\-4.#        ax1.plot(x,y)
\\-4.#        self.mplwid.figure.suptitle(r"$\alpha + \gamma = \rho$")
\\-4.#        ax1.grid(1)
\\-4.#        ax2= self.mplwid.figure.add_subplot(212)
\\-4.#        
\\-4.#        
\\-4.#        ax2.plot(x,y)
\\-4.#        
\\-4.#        ax2.grid(1)

    #        self.mplwid.draw()
    
</t>
<t tx="bin.20150912203711.8">(uncached) bin.20150912124601.1
Diff...
  @pyqtSignature("")
  def on_action_Open_triggered(self):
      self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                  r'D:\Workshop\Dakota\script')
      self.lblOut.setText("file Opened:" + self.fname)
      data = dakota_tabfile(self.fname)
       
+     
+     
  
- @pyqtSignature("")
</t>
<t tx="bin.20150912203711.9">@pyqtSignature("")
def on_action_Open_triggered(self):
    self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                r'D:\Workshop\Dakota\script')
    self.lblOut.setText("file Opened:" + self.fname)
    data = dakota_tabfile(self.fname)
     
    
    

</t>
</tnodes>
</leo_file>
