from PyQt4 import QtCore, QtGui
from sympy import *
from functools import partial

equation = ""
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.display = QtGui.QTextEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(30, 10, 721, 31))
        self.display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.display.setObjectName(_fromUtf8("display"))
        self.one = QtGui.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(370, 290, 51, 51))
        self.one.setObjectName(_fromUtf8("one"))
        self.one.clicked.connect(partial(self.add_to_string, self.one))
        self.two = QtGui.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(420, 290, 51, 51))
        self.two.setObjectName(_fromUtf8("two"))
        self.two.clicked.connect(partial(self.add_to_string, self.two))
        self.three = QtGui.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(470, 290, 51, 51))
        self.three.setObjectName(_fromUtf8("three"))
        self.three.clicked.connect(partial(self.add_to_string, self.three))
        self.seven = QtGui.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(370, 390, 51, 51))
        self.seven.setObjectName(_fromUtf8("seven"))
        self.seven.clicked.connect(partial(self.add_to_string, self.seven))
        self.zero = QtGui.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(370, 440, 51, 51))
        self.zero.setAutoDefault(False)
        self.zero.setObjectName(_fromUtf8("zero"))
        self.zero.clicked.connect(partial(self.add_to_string, self.zero))
        self.nine = QtGui.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(470, 390, 51, 51))
        self.nine.setObjectName(_fromUtf8("nine"))
        self.nine.clicked.connect(partial(self.add_to_string, self.nine))
        self.eight = QtGui.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(420, 390, 51, 51))
        self.eight.setObjectName(_fromUtf8("eight"))
        self.eight.clicked.connect(partial(self.add_to_string, self.eight))
        self.six = QtGui.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(470, 340, 51, 51))
        self.six.setObjectName(_fromUtf8("six"))
        self.six.clicked.connect(partial(self.add_to_string, self.six))
        self.five = QtGui.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(420, 340, 51, 51))
        self.five.setObjectName(_fromUtf8("five"))
        self.five.clicked.connect(partial(self.add_to_string, self.five))
        self.four = QtGui.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(370, 340, 51, 51))
        self.four.setObjectName(_fromUtf8("four"))
        self.four.clicked.connect(partial(self.add_to_string, self.four))
        self.multipy = QtGui.QPushButton(self.centralwidget)
        self.multipy.setGeometry(QtCore.QRect(520, 390, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.multipy.setFont(font)
        self.multipy.setObjectName(_fromUtf8("multipy"))
        self.multipy.clicked.connect(
            partial(self.add_to_string, self.multipy))
        self.divide = QtGui.QPushButton(self.centralwidget)
        self.divide.setGeometry(QtCore.QRect(520, 440, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.divide.setFont(font)
        self.divide.setObjectName(_fromUtf8("divide"))
        self.divide.clicked.connect(partial(self.add_to_string, self.divide))
        self.add = QtGui.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(520, 290, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.add.setFont(font)
        self.add.setObjectName(_fromUtf8("add"))
        self.add.clicked.connect(partial(self.add_to_string, self.add))
        self.subtract = QtGui.QPushButton(self.centralwidget)
        self.subtract.setGeometry(QtCore.QRect(520, 340, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.subtract.setFont(font)
        self.subtract.setObjectName(_fromUtf8("subtract"))
        self.subtract.clicked.connect(
            partial(self.add_to_string, self.subtract))
        self.dot = QtGui.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(420, 440, 51, 51))
        self.dot.setAutoDefault(False)
        self.dot.setObjectName(_fromUtf8("dot"))
        self.dot.clicked.connect(partial(self.add_to_string, self.dot))
        self.equal = QtGui.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(470, 440, 51, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.equal.setPalette(palette)
        self.equal.setAutoFillBackground(True)
        self.equal.setAutoDefault(False)
        self.equal.setObjectName(_fromUtf8("equal"))
        self.equal.clicked.connect(self.evaluate)
        self.index = QtGui.QPushButton(self.centralwidget)
        self.index.setGeometry(QtCore.QRect(470, 240, 51, 51))
        self.index.setObjectName(_fromUtf8("index"))
        self.index.clicked.connect(partial(self.add_to_string, self.index))
        self.close_bracket = QtGui.QPushButton(self.centralwidget)
        self.close_bracket.setGeometry(QtCore.QRect(420, 240, 51, 51))
        self.close_bracket.setObjectName(_fromUtf8("close_bracket"))
        self.close_bracket.clicked.connect(
            partial(self.add_to_string, self.close_bracket))
        self.open_bracket = QtGui.QPushButton(self.centralwidget)
        self.open_bracket.setGeometry(QtCore.QRect(370, 240, 51, 51))
        self.open_bracket.setObjectName(_fromUtf8("open_bracket"))
        self.open_bracket.clicked.connect(
            partial(self.add_to_string, self.open_bracket))
        self.AC = QtGui.QPushButton(self.centralwidget)
        self.AC.setGeometry(QtCore.QRect(520, 240, 81, 51))
        self.AC.clicked.connect(self.clear_text)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.AC.setFont(font)
        self.AC.setObjectName(_fromUtf8("AC"))
        self.Sin = QtGui.QPushButton(self.centralwidget)
        self.Sin.setGeometry(QtCore.QRect(290, 240, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Sin.setFont(font)
        self.Sin.setObjectName(_fromUtf8("Sin"))
        self.Cos = QtGui.QPushButton(self.centralwidget)
        self.Cos.setGeometry(QtCore.QRect(290, 290, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cos.setFont(font)
        self.Cos.setObjectName(_fromUtf8("Cos"))
        self.Tan = QtGui.QPushButton(self.centralwidget)
        self.Tan.setGeometry(QtCore.QRect(290, 340, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Tan.setFont(font)
        self.Tan.setObjectName(_fromUtf8("Tan"))
        self.Root = QtGui.QPushButton(self.centralwidget)
        self.Root.setGeometry(QtCore.QRect(290, 390, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Root.setFont(font)
        self.Root.setObjectName(_fromUtf8("Root"))
        self.Pi_sym = QtGui.QPushButton(self.centralwidget)
        self.Pi_sym.setGeometry(QtCore.QRect(290, 440, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Pi_sym.setFont(font)
        self.Pi_sym.setObjectName(_fromUtf8("Pi_sym"))
        self.Cosec = QtGui.QPushButton(self.centralwidget)
        self.Cosec.setGeometry(QtCore.QRect(210, 240, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cosec.setFont(font)
        self.Cosec.setObjectName(_fromUtf8("Cosec"))
        self.Sec = QtGui.QPushButton(self.centralwidget)
        self.Sec.setGeometry(QtCore.QRect(210, 290, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Sec.setFont(font)
        self.Sec.setObjectName(_fromUtf8("Sec"))
        self.Cot = QtGui.QPushButton(self.centralwidget)
        self.Cot.setGeometry(QtCore.QRect(210, 340, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Cot.setFont(font)
        self.Cot.setObjectName(_fromUtf8("Cot"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.one.setText(_translate("MainWindow", "1", None))
        self.two.setText(_translate("MainWindow", "2", None))
        self.three.setText(_translate("MainWindow", "3", None))
        self.seven.setText(_translate("MainWindow", "7", None))
        self.zero.setText(_translate("MainWindow", "0", None))
        self.nine.setText(_translate("MainWindow", "9", None))
        self.eight.setText(_translate("MainWindow", "8", None))
        self.six.setText(_translate("MainWindow", "6", None))
        self.five.setText(_translate("MainWindow", "5", None))
        self.four.setText(_translate("MainWindow", "4", None))
        self.multipy.setText(_translate("MainWindow", "×", None))
        self.divide.setText(_translate("MainWindow", "÷", None))
        self.add.setText(_translate("MainWindow", "+", None))
        self.subtract.setText(_translate("MainWindow", "-", None))
        self.dot.setText(_translate("MainWindow", ".", None))
        self.equal.setText(_translate("MainWindow", "=", None))
        self.index.setText(_translate("MainWindow", "^", None))
        self.close_bracket.setText(_translate("MainWindow", ")", None))
        self.open_bracket.setText(_translate("MainWindow", "(", None))
        self.AC.setText(_translate("MainWindow", "AC", None))
        self.Sin.setText(_translate("MainWindow", "Sin", None))
        self.Cos.setText(_translate("MainWindow", "Cos", None))
        self.Tan.setText(_translate("MainWindow", "Tan", None))
        self.Root.setText(_translate("MainWindow", "√", None))
        self.Pi_sym.setText(_translate("MainWindow", "Pi", None))
        self.Cosec.setText(_translate("MainWindow", "Cosec", None))
        self.Sec.setText(_translate("MainWindow", "Sec", None))
        self.Cot.setText(_translate("MainWindow", "Cot", None))

    def add_to_string(self, button):
        global equation
        if str(button.text()) == "×":
            equation = equation + "*"
            self.display.setText(equation)
        elif str(button.text()) == "÷":
            equation = equation + "/"
            self.display.setText(equation)
        elif str(button.text()) == "^":
            equation = equation + "**"
            self.display.setText(equation)
        else:
            equation = equation + str(button.text())
            self.display.setText(equation)

    def clear_text(self):
        global equation
        equation = ""
        self.display.setText(equation)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())