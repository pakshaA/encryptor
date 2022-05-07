from PyQt5 import QtCore, QtGui, QtWidgets
from Cesar import *


class Ui_Cesar(object):
    def setupUi(self, Cesar):
        Cesar.setObjectName("Cesar")
        Cesar.resize(440, 370)
        self.Input_Text = QtWidgets.QTextEdit(Cesar)
        self.Input_Text.setGeometry(QtCore.QRect(30, 10, 380, 100))
        self.Input_Text.setAccessibleDescription("")
        self.Input_Text.setObjectName("Input_Text")
        self.Key_2 = QtWidgets.QLabel(Cesar)
        self.Key_2.setGeometry(QtCore.QRect(30, 170, 70, 15))
        self.Key_2.setObjectName("Key_2")
        self.Key_value = QtWidgets.QLineEdit(Cesar)
        self.Key_value.setGeometry(QtCore.QRect(80, 170, 330, 20))
        self.Key_value.setObjectName("Key_value")
        self.Encrypt = QtWidgets.QPushButton(Cesar)
        self.Encrypt.setGeometry(QtCore.QRect(30, 220, 380, 25))
        self.Encrypt.setObjectName("Encrypt")
        self.Output_Text = QtWidgets.QTextBrowser(Cesar)
        self.Output_Text.setGeometry(QtCore.QRect(30, 260, 380, 100))
        self.Output_Text.setObjectName("Output_Text")
        self.comboBox = QtWidgets.QComboBox(Cesar)
        self.comboBox.setGeometry(QtCore.QRect(30, 130, 380, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Cesar)
        QtCore.QMetaObject.connectSlotsByName(Cesar)
        Cesar.setTabOrder(self.Input_Text, self.Encrypt)
        Cesar.setTabOrder(self.Encrypt, self.Output_Text)

        self.Encrypt.clicked.connect(self.btn_click)

    def retranslateUi(self, Cesar):
        _translate = QtCore.QCoreApplication.translate
        Cesar.setWindowTitle(_translate("Cesar", "Шифратор"))
        self.Input_Text.setWhatsThis(_translate("Cesar", "<html><head/><body><p><br/></p></body></html>"))
        self.Input_Text.setPlaceholderText(_translate("Cesar", "Введите текст"))
        self.Key_2.setText(_translate("Cesar", "Ключ:"))
        self.Encrypt.setText(_translate("Cesar", "Зашифровать/Дешифровать"))
        self.comboBox.setItemText(0, _translate("Cesar", "Шифрование"))
        self.comboBox.setItemText(1, _translate("Cesar", "Дешифрование"))

    def btn_click(self):
        res = get_caesar(self.Input_Text.toPlainText(), int(self.Key_value.text()), self.comboBox.currentIndex())
        self.Output_Text.setText(res)
