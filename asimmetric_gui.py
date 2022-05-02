
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from asimmetric import *
from key_gen import *
import os


class Ui_MainWindow(object):
    fname = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Select_dir = QtWidgets.QPushButton(self.centralwidget)
        self.Select_dir.setGeometry(QtCore.QRect(240, 140, 251, 31))
        self.Select_dir.setObjectName("Select_dir")
        self.Method = QtWidgets.QComboBox(self.centralwidget)
        self.Method.setGeometry(QtCore.QRect(39, 20, 101, 22))
        self.Method.setObjectName("Method")
        self.Method.addItem("")
        self.Method.addItem("")
        self.Open_dir_to_save = QtWidgets.QPushButton(self.centralwidget)
        self.Open_dir_to_save.setGeometry(QtCore.QRect(290, 300, 111, 23))
        self.Open_dir_to_save.setObjectName("Open_dir_to_save")
        self.Select_file_encr = QtWidgets.QLabel(self.centralwidget)
        self.Select_file_encr.setGeometry(QtCore.QRect(40, 110, 191, 71))
        self.Select_file_encr.setObjectName("select_file")
        self.Select_file_decr = QtWidgets.QLabel(self.centralwidget)
        self.Select_file_decr.setGeometry(QtCore.QRect(40, 110, 191, 71))
        self.Select_file_decr.setObjectName("Select_file")
        self.Keys_gen = QtWidgets.QPushButton(self.centralwidget)
        self.Keys_gen.setGeometry(QtCore.QRect(160, 20, 281, 21))
        self.Keys_gen.setObjectName("Keys_gen")
        self.Full_Start = QtWidgets.QPushButton(self.centralwidget)
        self.Full_Start.setGeometry(QtCore.QRect(40, 70, 451, 23))
        self.Full_Start.setObjectName("Full_Start")
        self.End = QtWidgets.QPushButton(self.centralwidget)
        self.End.setGeometry((QtCore.QRect(44, 370, 451, 23)))
        self.End.setObjectName("End")
        self.dir_to_keys = QtWidgets.QLabel(self.centralwidget)
        self.dir_to_keys.setGeometry(QtCore.QRect(90, 50, 411, 71))
        self.dir_to_keys.setObjectName("dir_to_keys")
        self.Save_text_encr = QtWidgets.QLabel(self.centralwidget)
        self.Save_text_encr.setGeometry(QtCore.QRect(40, 220, 451, 61))
        self.Save_text_encr.setObjectName("Save_text")
        self.Save_text_decr = QtWidgets.QLabel(self.centralwidget)
        self.Save_text_decr.setGeometry(QtCore.QRect(40, 220, 451, 61))
        self.Save_text_decr.setObjectName("Save_text")
        self.Tip_to_open = QtWidgets.QLabel(self.centralwidget)
        self.Tip_to_open.setGeometry(QtCore.QRect(40, 280, 241, 61))
        self.Tip_to_open.setObjectName("Tip_to_open")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(70, 180, 121, 23))
        self.Start.setObjectName("Start")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Start.clicked.connect(self.start_click)
        self.Keys_gen.clicked.connect(self.keys_gen)
        self.Select_dir.clicked.connect(self.select_dir)
        self.Open_dir_to_save.clicked.connect(self.open_file)
        self.Full_Start.clicked.connect(self.start)
        self.End.clicked.connect(self.end)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Full_Start.setText(_translate("MainWindow", "Начать работу с выбранным методом"))
        self.End.setText(_translate("MainWindow", "Закончить работу с выбранным методом"))
        self.Method.setItemText(0, _translate("MainWindow", "Шифрование"))
        self.Method.setItemText(1, _translate("MainWindow", "Дешифрование"))
        self.Select_dir.setText(_translate("MainWindow", "Нaжмите, чтобы выбрать файл "))
        self.Open_dir_to_save.setText(_translate("MainWindow", "Открыть файл"))
        self.Select_file_encr.setText(_translate("MainWindow", "Выберите файл,\n"
                                                          "который требуется зашифровать"))
        self.Select_file_decr.setText(_translate("MainWindow", "Выберите файл,\n"
                                                          "который требуется дешифровать"))

        self.Keys_gen.setText(_translate("MainWindow", "Нажмите, чтобы сгенерировать пару ключей"))
        self.dir_to_keys.setText(_translate("MainWindow",
                                            "<html><head/><body><p>Ключи сгенерированы в C:\\Users\\paksh\\PycharmProjects\\encryptor\\private</p><p>и C:\\Users\\paksh\\PycharmProjects\\encrypto\\public</p></body></html>"))

        self.Save_text_encr.setText(_translate("MainWindow", "Файл с зашифрованным текстом сохранен в\n"
                                                        " C:Users\\paksh\\PycharmProjects\\test_with_text\\data_encrypted"))
        self.Save_text_decr.setText(_translate("MainWindow", "Файл с дешифрованным текстом сохранен в\n"
                                                        " C:Users\\paksh\\PycharmProjects\\encryptor\\data_encrypted_decrypted"))
        self.Tip_to_open.setText(_translate("MainWindow",
                                            "<html><head/><body><p>Нажмите на кнопку, </p><p>чтобы открыть полученный текст</p></body></html>"))
        self.Start.setText(_translate("MainWindow", "Начать работу"))

        self.Select_file_encr.setVisible(False)
        self.Open_dir_to_save.setVisible(False)
        self.Select_file_decr.setVisible(False)
        self.Keys_gen.setVisible(False)
        self.dir_to_keys.setVisible(False)
        self.Save_text_encr.setVisible(False)
        self.Save_text_decr.setVisible(False)
        self.Tip_to_open.setVisible(False)
        self.Select_dir.setVisible(False)
        self.Start.setVisible(False)
        self.End.setVisible(False)

    def start(self):
        if self.Method.currentIndex() == 0:
            self.Keys_gen.setVisible(True)
            self.Select_dir.setVisible(True)
            self.Open_dir_to_save.setVisible(True)
            self.Select_file_encr.setVisible(True)
            self.Start.setVisible(True)
            self.Tip_to_open.setVisible(True)
            self.Full_Start.setVisible(False)
            self.End.setVisible(True)
        else:
            self.Select_dir.setVisible(True)
            self.Select_file_decr.setVisible(True)
            self.Tip_to_open.setVisible(True)
            self.Full_Start.setVisible(False)
            self.End.setVisible(True)
            self.Start.setVisible(True)
            self.Save_text_decr.setVisible(True)
            self.Open_dir_to_save.setVisible(True)

    def start_click(self):
        if self.Method.currentIndex() == 0:
            encrypt(self.fname[0], "public.pem")
            self.Save_text_encr.setVisible(True)
        else:
            decrypt(self.fname[0], "private.pem")
            self.Save_text_decr.setVisible(True)

    def keys_gen(self):
        if self.Method.currentIndex() == 0:
            key_gen()
            self.dir_to_keys.setVisible(True)

    def end(self):
        self.Select_file_encr.setVisible(False)
        self.Open_dir_to_save.setVisible(False)
        self.Select_file_decr.setVisible(False)
        self.Keys_gen.setVisible(False)
        self.dir_to_keys.setVisible(False)
        self.Save_text_encr.setVisible(False)
        self.Save_text_decr.setVisible(False)
        self.Tip_to_open.setVisible(False)
        self.Select_dir.setVisible(False)
        self.Start.setVisible(False)
        self.End.setVisible(False)
        self.Full_Start.setVisible(True)

    def select_dir(self):
     self.fname = QFileDialog.getOpenFileName(None, 'Open file', 'C:\\Users\\paksh\\PycharmProjects\\encryptor\\',
                                                "Text files (*.txt)")
    def open_file(self):
        if self.Method.currentIndex() == 0:
            os.system("C:\\Users\\paksh\\PycharmProjects\\encryptor\\data_encrypted.txt")
        if self.Method.currentIndex() == 1:
            os.system("C:\\Users\\paksh\\PycharmProjects\\encryptor\\data_encrypted_decrypted.txt")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
