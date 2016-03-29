# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calc.ui'
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

class Ui_calc(object):
    def setupUi(self, calc):
        calc.setObjectName(_fromUtf8("calc"))
        calc.resize(557, 452)
        calc.setSizeGripEnabled(True)
        calc.setModal(True)
        self.gridLayout = QtGui.QGridLayout(calc)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.value_0 = QtGui.QPushButton(calc)
        self.value_0.setObjectName(_fromUtf8("value_0"))
        self.gridLayout.addWidget(self.value_0, 5, 0, 1, 1)
        self.add = QtGui.QPushButton(calc)
        self.add.setObjectName(_fromUtf8("add"))
        self.gridLayout.addWidget(self.add, 1, 3, 1, 1)
        self.value_4 = QtGui.QPushButton(calc)
        self.value_4.setObjectName(_fromUtf8("value_4"))
        self.gridLayout.addWidget(self.value_4, 2, 0, 2, 1)
        self.sub = QtGui.QPushButton(calc)
        self.sub.setObjectName(_fromUtf8("sub"))
        self.gridLayout.addWidget(self.sub, 2, 3, 1, 1)
        self.value_2 = QtGui.QPushButton(calc)
        self.value_2.setObjectName(_fromUtf8("value_2"))
        self.gridLayout.addWidget(self.value_2, 1, 1, 1, 1)
        self.value_3 = QtGui.QPushButton(calc)
        self.value_3.setObjectName(_fromUtf8("value_3"))
        self.gridLayout.addWidget(self.value_3, 1, 2, 1, 1)
        self.value_9 = QtGui.QPushButton(calc)
        self.value_9.setObjectName(_fromUtf8("value_9"))
        self.gridLayout.addWidget(self.value_9, 4, 2, 1, 1)
        self.value_1 = QtGui.QPushButton(calc)
        self.value_1.setObjectName(_fromUtf8("value_1"))
        self.gridLayout.addWidget(self.value_1, 1, 0, 1, 1)
        self.value_7 = QtGui.QPushButton(calc)
        self.value_7.setObjectName(_fromUtf8("value_7"))
        self.gridLayout.addWidget(self.value_7, 4, 0, 1, 1)
        self.div = QtGui.QPushButton(calc)
        self.div.setObjectName(_fromUtf8("div"))
        self.gridLayout.addWidget(self.div, 4, 3, 1, 1)
        self.value_6 = QtGui.QPushButton(calc)
        self.value_6.setObjectName(_fromUtf8("value_6"))
        self.gridLayout.addWidget(self.value_6, 2, 2, 2, 1)
        self.value_5 = QtGui.QPushButton(calc)
        self.value_5.setObjectName(_fromUtf8("value_5"))
        self.gridLayout.addWidget(self.value_5, 2, 1, 2, 1)
        self.mul = QtGui.QPushButton(calc)
        self.mul.setObjectName(_fromUtf8("mul"))
        self.gridLayout.addWidget(self.mul, 3, 3, 1, 1)
        self.calc_display = QtGui.QLCDNumber(calc)
        self.calc_display.setFrameShape(QtGui.QFrame.StyledPanel)
        self.calc_display.setSmallDecimalPoint(True)
        self.calc_display.setProperty("value", 0.0)
        self.calc_display.setObjectName(_fromUtf8("calc_display"))
        self.gridLayout.addWidget(self.calc_display, 0, 0, 1, 4)
        self.value_8 = QtGui.QPushButton(calc)
        self.value_8.setObjectName(_fromUtf8("value_8"))
        self.gridLayout.addWidget(self.value_8, 4, 1, 1, 1)
        self.clear_p = QtGui.QPushButton(calc)
        self.clear_p.setObjectName(_fromUtf8("clear_p"))
        self.gridLayout.addWidget(self.clear_p, 5, 1, 1, 1)
        self.equals = QtGui.QPushButton(calc)
        self.equals.setObjectName(_fromUtf8("equals"))
        self.gridLayout.addWidget(self.equals, 5, 3, 1, 1)
        self.clear_a = QtGui.QPushButton(calc)
        self.clear_a.setObjectName(_fromUtf8("clear_a"))
        self.gridLayout.addWidget(self.clear_a, 5, 2, 1, 1)

        self.retranslateUi(calc)
        QtCore.QMetaObject.connectSlotsByName(calc)
        calc.setTabOrder(self.value_1, self.value_2)
        calc.setTabOrder(self.value_2, self.value_3)
        calc.setTabOrder(self.value_3, self.value_4)
        calc.setTabOrder(self.value_4, self.value_5)
        calc.setTabOrder(self.value_5, self.value_6)
        calc.setTabOrder(self.value_6, self.value_7)
        calc.setTabOrder(self.value_7, self.value_8)
        calc.setTabOrder(self.value_8, self.value_9)
        calc.setTabOrder(self.value_9, self.value_0)
        calc.setTabOrder(self.value_0, self.equals)
        calc.setTabOrder(self.equals, self.add)
        calc.setTabOrder(self.add, self.sub)
        calc.setTabOrder(self.sub, self.mul)
        calc.setTabOrder(self.mul, self.div)

    def retranslateUi(self, calc):
        calc.setWindowTitle(_translate("calc", "Dialog", None))
        self.value_0.setText(_translate("calc", "0", None))
        self.add.setText(_translate("calc", "+", None))
        self.value_4.setText(_translate("calc", "4", None))
        self.sub.setText(_translate("calc", "-", None))
        self.value_2.setText(_translate("calc", "2", None))
        self.value_3.setText(_translate("calc", "3", None))
        self.value_9.setText(_translate("calc", "9", None))
        self.value_1.setText(_translate("calc", "1", None))
        self.value_7.setText(_translate("calc", "7", None))
        self.div.setText(_translate("calc", "/", None))
        self.value_6.setText(_translate("calc", "6", None))
        self.value_5.setText(_translate("calc", "5", None))
        self.mul.setText(_translate("calc", "*", None))
        self.value_8.setText(_translate("calc", "8", None))
        self.clear_p.setText(_translate("calc", "C", None))
        self.equals.setText(_translate("calc", "=", None))
        self.clear_a.setText(_translate("calc", "AC", None))

