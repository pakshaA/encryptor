

from PyQt5 import QtCore, QtGui, QtWidgets
from Cesar import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input_Text = QtWidgets.QTextEdit(self.centralwidget)
        self.Input_Text.setGeometry(QtCore.QRect(30, 10, 381, 101))
        self.Input_Text.setAccessibleDescription("")
        self.Input_Text.setObjectName("Input_Text")
        self.Cipher_selector = QtWidgets.QComboBox(self.centralwidget)
        self.Cipher_selector.setGeometry(QtCore.QRect(30, 130, 181, 21))
        self.Cipher_selector.setObjectName("Cipher_selector")
        self.Cipher_selector.addItem("")
        self.Cipher_selector.addItem("")
        self.Key_2 = QtWidgets.QLabel(self.centralwidget)
        self.Key_2.setGeometry(QtCore.QRect(30, 170, 71, 16))
        self.Key_2.setObjectName("Key_2")
        self.Key_value = QtWidgets.QLineEdit(self.centralwidget)
        self.Key_value.setGeometry(QtCore.QRect(70, 170, 341, 21))
        self.Key_value.setObjectName("Key_value")
        self.Encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.Encrypt.setGeometry(QtCore.QRect(140, 220, 151, 23))
        self.Encrypt.setObjectName("Encrypt")
        self.Output_Text = QtWidgets.QTextBrowser(self.centralwidget)
        self.Output_Text.setGeometry(QtCore.QRect(30, 260, 391, 131))
        self.Output_Text.setObjectName("Output_Text")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(230, 130, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Input_Text, self.Encrypt)
        MainWindow.setTabOrder(self.Encrypt, self.Output_Text)
        MainWindow.setTabOrder(self.Output_Text, self.Cipher_selector)
        MainWindow.setTabOrder(self.Cipher_selector, self.Key_value)

        self.Encrypt.clicked.connect(self.btn_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифратор"))
        self.Input_Text.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Input_Text.setPlaceholderText(_translate("MainWindow", "Введите текст"))
        self.Cipher_selector.setItemText(0, _translate("MainWindow", "Выберите метод шифрования"))
        self.Cipher_selector.setItemText(1, _translate("MainWindow", "Шифр Цезаря (Модернизированный)"))
        self.Key_2.setText(_translate("MainWindow", "Ключ:"))
        self.Encrypt.setText(_translate("MainWindow", "Зашифровать"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Выберите способ работы"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Шифрование"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Дешифрование"))

    def btn_click(self):
        if self.Cipher_selector.currentIndex() == 1:
            res = get_caesar(self.Input_Text.toPlainText(), int(self.Key_value.text()), self.comboBox.currentIndex())
            self.Output_Text.setText(res)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
