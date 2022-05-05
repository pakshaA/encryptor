from PyQt5 import QtCore, QtGui, QtWidgets
from Cesar_gui import Ui_Cesar
from asimmetric_gui import Ui_RSA


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(420, 200)
        self.simmetric = QtWidgets.QPushButton(main_window)
        self.simmetric.setGeometry(QtCore.QRect(40, 50, 341, 30))
        self.simmetric.setObjectName("simmetric")
        self.asimmetric = QtWidgets.QPushButton(main_window)
        self.asimmetric.setGeometry(QtCore.QRect(40, 90, 341, 30))
        self.asimmetric.setObjectName("asimmetric")
        self.pushButton_3 = QtWidgets.QPushButton(main_window)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 130, 341, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(main_window)
        self.label.setGeometry(QtCore.QRect(40, 20, 361, 30))
        self.label.setObjectName("label")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Шифратор"))
        self.simmetric.setText(_translate("main_window", "Симметричное шифрование (Шифр Цезаря)"))
        self.asimmetric.setText(_translate("main_window", "Ассиметричное шифрование (RSA)"))
        self.pushButton_3.setText(_translate("main_window", "PushButton"))
        self.label.setText(_translate("main_window", "<html><head/><body><p>Выберите алгоритм, с которым будете работать:</p><p><br/></p></body></html>"))


class Main(QtWidgets.QWidget, Ui_main_window):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.simmetric.clicked.connect(self.simmetric_start)
        self.asimmetric.clicked.connect(self.asimmetric_start)

    def simmetric_start(self):
        self.Cesar = Cesar()
        self.Cesar.show()


    def asimmetric_start(self):
        self.RSA = RSA()
        self.RSA.show()

class Cesar(QtWidgets.QWidget, Ui_Cesar):
    def __init__(self, parent=None):
        super(Cesar, self).__init__(parent)
        self.setupUi(self)


class RSA(QtWidgets.QWidget, Ui_RSA):
    def __init__(self, parent=None):
        super(RSA, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
