# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Users\xianghe.zhao\workspace\test\src\SelectSql.ui'
#
# Created: Fri Dec 20 14:15:22 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(506, 259)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 221, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 121, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineSelLogEdit = QtGui.QLineEdit(Dialog)
        self.lineSelLogEdit.setGeometry(QtCore.QRect(20, 40, 381, 20))
        self.lineSelLogEdit.setReadOnly(True)
        self.lineSelLogEdit.setObjectName(_fromUtf8("lineSelLogEdit"))
        self.lineSelExcEdit = QtGui.QLineEdit(Dialog)
        self.lineSelExcEdit.setGeometry(QtCore.QRect(20, 90, 381, 20))
        self.lineSelExcEdit.setReadOnly(True)
        self.lineSelExcEdit.setObjectName(_fromUtf8("lineSelExcEdit"))
        self.lineSetExcEdit = QtGui.QLineEdit(Dialog)
        self.lineSetExcEdit.setGeometry(QtCore.QRect(20, 140, 181, 20))
        self.lineSetExcEdit.setObjectName(_fromUtf8("lineSetExcEdit"))
        self.lineSetSqlEdit = QtGui.QLineEdit(Dialog)
        self.lineSetSqlEdit.setGeometry(QtCore.QRect(20, 190, 471, 20))
        self.lineSetSqlEdit.setObjectName(_fromUtf8("lineSetSqlEdit"))
        self.pushSelLogButton = QtGui.QPushButton(Dialog)
        self.pushSelLogButton.setGeometry(QtCore.QRect(420, 40, 75, 23))
        self.pushSelLogButton.setObjectName(_fromUtf8("pushSelLogButton"))
        self.pushSelExcButton = QtGui.QPushButton(Dialog)
        self.pushSelExcButton.setGeometry(QtCore.QRect(420, 90, 75, 23))
        self.pushSelExcButton.setObjectName(_fromUtf8("pushSelExcButton"))
        self.pushMakeExcButton = QtGui.QPushButton(Dialog)
        self.pushMakeExcButton.setGeometry(QtCore.QRect(170, 220, 141, 23))
        self.pushMakeExcButton.setObjectName(_fromUtf8("pushMakeExcButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "WriteCSVLog", None))
        self.label.setText(_translate("Dialog", "选择日志文件", None))
        self.label_2.setText(_translate("Dialog", "选择生成Exc路径", None))
        self.label_3.setText(_translate("Dialog", "设置生成Exc文件名", None))
        self.label_4.setText(_translate("Dialog", "设置 Select SQL", None))
        self.pushSelLogButton.setText(_translate("Dialog", "...", None))
        self.pushSelExcButton.setText(_translate("Dialog", "...", None))
        self.pushMakeExcButton.setText(_translate("Dialog", "生成EXC文件", None))

