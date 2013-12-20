#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from PyQt4 import QtCore, QtGui
from ui_WriteLog import *
from WriteCSVLogFromDBLog import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
class Ui(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.ui = Ui_Dialog()    
        self.ui.setupUi(self)
        self.connect(self.ui.pushMakeExcButton, QtCore.SIGNAL("clicked()"),
                     self.write_Log)
        self.connect(self.ui.pushSelLogButton, QtCore.SIGNAL("clicked()"),
                     self.sellogfile)
        self.connect(self.ui.pushSelExcButton, QtCore.SIGNAL("clicked()"),
                     self.selexcpath)
        self.ui.lineSetSqlEdit.setText('select * from bbstattable')
    def write_Log(self):
        StrLogPath     =   self.ui.lineSelLogEdit.text().__str__()
        StrExcNamePath =   self.ui.lineSelExcEdit.text().__str__() + '/' + self.ui.lineSetExcEdit.text().__str__()
        StrSelectSql   =   self.ui.lineSetSqlEdit.text().__str__()
        if not os.path.exists( StrLogPath ) :
            QtGui.QMessageBox.warning(None,
                                      'Warning',
                                      "No such LogDB Path!",
                                      QtGui.QMessageBox.Ok)
        elif not os.path.exists( self.ui.lineSelExcEdit.text().__str__() ):
            QtGui.QMessageBox.warning(None,
                                      'Warning',
                                      "No such Excel Path!",
                                      QtGui.QMessageBox.Ok) 
        elif not StrSelectSql == '': 
            QtGui.QMessageBox.warning(None,
                                      'Warning',
                                      "No such Excel Name!",
                                      QtGui.QMessageBox.Ok)
        else:
            stater = WriteLog( StrLogPath, StrExcNamePath, StrSelectSql )
            stater.process()
    def sellogfile(self):
        strtmp = QtGui.QFileDialog.getOpenFileName(None,'','e:/','*.nds')
        self.ui.lineSelLogEdit.setText(strtmp)
        qstrExcName = strtmp.mid( strtmp.lastIndexOf("/")+1, strtmp.lastIndexOf(".")-strtmp.lastIndexOf("/")-1 )
        self.ui.lineSetExcEdit.setText(qstrExcName)    
    def selexcpath(self):
        strtmp = QtGui.QFileDialog.getExistingDirectory(None,'','e:/',)
        self.ui.lineSelExcEdit.setText(strtmp)
    def closeEvent(self, event):
        event.accept()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Ui()
    window.setFixedSize( 500, 250)
    window.exec_()
    
    sys.exit(app.exec_())
    
    
    
    
    
    