from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import calc_ui


class Calculator(QDialog, calc_ui.Ui_calc):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setFocus()


        self.clear_a.clicked.connect(self.clear_all)
        self.clear_p.clicked.connect(self.delete_num)
        self.value_0.clicked.connect(lambda: self.enter_num(0))
        self.value_1.clicked.connect(lambda: self.enter_num(1))
        self.value_2.clicked.connect(lambda: self.enter_num(2))
        self.value_3.clicked.connect(lambda: self.enter_num(3))
        self.value_4.clicked.connect(lambda: self.enter_num(4))
        self.value_5.clicked.connect(lambda: self.enter_num(5))
        self.value_6.clicked.connect(lambda: self.enter_num(6))
        self.value_7.clicked.connect(lambda: self.enter_num(7))
        self.value_8.clicked.connect(lambda: self.enter_num(8))
        self.value_9.clicked.connect(lambda: self.enter_num(9))
        self.add.clicked.connect(lambda: self.eval("+"))
        self.sub.clicked.connect(lambda: self.eval("-"))
        self.mul.clicked.connect(lambda: self.eval("*"))
        self.div.clicked.connect(lambda: self.eval("/"))
        self.equals.clicked.connect(lambda: self.eval("="))


    res, inp , op, var1= 0, 0, "", 0



    def clear_all(self):
        Calculator.inp, Calculator.res, Calculator.var1, Calculator.op = 0, 0, 0, ""
        self.calc_display.display(Calculator.res)


    def delete_num(self):
        Calculator.res = Calculator.res//10
        self.calc_display.display(Calculator.res)


    def enter_num(self, num):
        Calculator.inp = Calculator.inp*10 + num
        self.calc_display.display(Calculator.inp)

    def eval(self, op):
        if Calculator.op!="":
            if Calculator.op=="+":
                Calculator.res = Calculator.var1 + Calculator.inp
            elif Calculator.op=="-":
                Calculator.res = Calculator.var1 - Calculator.inp
            elif Calculator.op=="*":
                Calculator.res = Calculator.var1 * Calculator.inp
            elif Calculator.op=="/":
                Calculator.res = Calculator.var1 / Calculator.inp

        else:
            Calculator.res = Calculator.inp

        Calculator.op = op
        self.calc_display.display(Calculator.res)
        Calculator.var1 = Calculator.res
        Calculator.inp = 0





app = QApplication(sys.argv)
lets_calc = Calculator()
lets_calc.show()
app.exec_()

