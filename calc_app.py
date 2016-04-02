from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

import calc_ui


class Calculator(QDialog, calc_ui.Ui_calc):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setFocus()

        #button actions handled here
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
        self.decimal.clicked.connect(lambda: self.dec_mode())

    #res to hold result of the operation, inp to get input value, op to determine operation to perform, var1 to hold previous input value, flag to determine whether the input value is going into decimal range, dec to old the string form of the float number
    res, inp , op, var1, flag, dec= 0, 0, "", 0, 0, ""



    def clear_all(self):
        #Clears all variables
        Calculator.inp, Calculator.res, Calculator.var1, Calculator.op = 0, 0, 0, ""
        self.calc_display.display(Calculator.res)


    def delete_num(self):
        #delets one numeal at a time from a number
        Calculator.res = Calculator.res//10
        self.calc_display.display(Calculator.res)


    def enter_num(self, num):
        #inputs numerals to the number on key press
        if Calculator.flag==0:
            Calculator.inp = Calculator.inp*10 + num
            self.calc_display.display(Calculator.inp)
        else:
            Calculator.dec += str(num)
            Calculator.inp = float(Calculator.dec)
            self.calc_display.display(Calculator.inp)


    def eval(self, op):
        #evaluates the result
        Calculator.flag = 0
        if Calculator.op!="":
            if Calculator.op=="+":
                Calculator.res = Calculator.var1 + Calculator.inp
            elif Calculator.op=="-":
                Calculator.res = Calculator.var1 - Calculator.inp
            elif Calculator.op=="*":
                Calculator.res = Calculator.var1 * Calculator.inp
            elif Calculator.op=="/":
                try:
                    Calculator.res = Calculator.var1 / Calculator.inp
                except ZeroDivisionError:
                    QMessageBox.information(self, "Error", "Cannot divide by zero")
                    self.clear_all()

        else:
            Calculator.res = Calculator.inp

        Calculator.op = op
        self.calc_display.display(Calculator.res)
        Calculator.var1 = Calculator.res
        Calculator.inp = 0


    def dec_mode(self):
        #sets flag to 1 to trigger decimal mode
        Calculator.flag = 1
        Calculator.dec = str(Calculator.inp)+"."






app = QApplication(sys.argv)
lets_calc = Calculator()
lets_calc.show()
app.exec_()

