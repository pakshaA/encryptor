from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from asimmetric import *
from key_gen import *
import os
from ErrorWindow import *
import cryptography.fernet


class Ui_RSA(object):
    fname = ""
    curr_dir = ""

    def setupUi(self, RSA):
        RSA.setObjectName("RSA")
        RSA.resize(700, 700)
        self.Select_dir = QtWidgets.QPushButton(RSA)
        self.Select_dir.setGeometry(QtCore.QRect(280, 260, 390, 30))
        self.Select_dir.setObjectName("Select_dir")
        self.Method = QtWidgets.QComboBox(RSA)
        self.Method.setGeometry(QtCore.QRect(30, 30, 640, 30))
        self.Method.setObjectName("Method")
        self.Method.addItem("")
        self.Method.addItem("")
        self.start_txt = QtWidgets.QLabel(RSA)
        self.start_txt.setGeometry(30, 30, 650, 30)
        self.start_txt.setObjectName("start_txt")
        self.Open_dir_to_save = QtWidgets.QPushButton(RSA)
        self.Open_dir_to_save.setGeometry(QtCore.QRect(270, 480, 400, 30))
        self.Open_dir_to_save.setObjectName("Open_dir_to_save")
        self.Select_file = QtWidgets.QLabel(RSA)
        self.Select_file.setGeometry(QtCore.QRect(30, 240, 250, 70))
        self.Select_file.setObjectName("select_file")
        self.Keys_gen = QtWidgets.QPushButton(RSA)
        self.Keys_gen.setGeometry(QtCore.QRect(30, 110, 640, 30))
        self.Keys_gen.setObjectName("Keys_gen")
        self.Full_Start = QtWidgets.QPushButton(RSA)
        self.Full_Start.setGeometry(QtCore.QRect(30, 110, 640, 30))
        self.Full_Start.setObjectName("Full_Start")
        self.End = QtWidgets.QPushButton(RSA)
        self.End.setGeometry((QtCore.QRect(30, 560, 640, 30)))
        self.End.setObjectName("End")
        self.dir_to_keys = QtWidgets.QLabel(RSA)
        self.dir_to_keys.setGeometry(QtCore.QRect(30, 150, 650, 100))
        self.dir_to_keys.setObjectName("dir_to_keys")
        self.save_text = QtWidgets.QLabel(RSA)
        self.save_text.setGeometry(QtCore.QRect(30, 390, 640, 70))
        self.save_text.setObjectName("Save_text")
        self.Tip_to_open = QtWidgets.QLabel(RSA)
        self.Tip_to_open.setGeometry(QtCore.QRect(30, 480, 250, 50))
        self.Tip_to_open.setObjectName("Tip_to_open")
        self.Start = QtWidgets.QPushButton(RSA)
        self.Start.setGeometry(QtCore.QRect(30, 350, 640, 30))
        self.Start.setObjectName("Start")
        self.Select_dir_to_save = QtWidgets.QPushButton(RSA)
        self.Select_dir_to_save.setGeometry(30, 70, 640, 30)
        self.Select_dir_to_save.setObjectName("Select_dir_to_save")

        self.retranslateUi(RSA)
        QtCore.QMetaObject.connectSlotsByName(RSA)

        self.Start.clicked.connect(self.start_click)
        self.Keys_gen.clicked.connect(self.keys_gen)
        self.Select_dir.clicked.connect(self.select_dir)
        self.Open_dir_to_save.clicked.connect(self.open_file)
        self.Full_Start.clicked.connect(self.start)
        self.End.clicked.connect(self.end)
        self.Select_dir_to_save.clicked.connect(self.get_dirr)

    def retranslateUi(self, RSA):
        _translate = QtCore.QCoreApplication.translate
        RSA.setWindowTitle(_translate("RSA", "Шифратор"))
        self.Full_Start.setText(_translate("RSA", "Начать работу с выбранным методом"))
        self.End.setText(_translate("RSA", "Закончить работу с выбранным методом"))
        self.Method.setItemText(0, _translate("RSA", "Шифрование"))
        self.Method.setItemText(1, _translate("RSA", "Дешифрование"))
        self.Select_dir.setText(_translate("RSA", "Нaжмите, чтобы выбрать файл "))
        self.Open_dir_to_save.setText(_translate("RSA", "Открыть файл"))
        self.Keys_gen.setText(_translate("RSA", "Нажмите, чтобы сгенерировать пару ключей"))
        self.Tip_to_open.setText(_translate("RSA",
                                            "<html><head/><body><p>Нажмите на кнопку, чтобы"
                                            " </p><p> открыть полученный текст</p></body></html>"))
        self.Start.setText(_translate("RSA", "Начать работу"))
        self.Select_dir_to_save.setText(_translate("RSA", "Выберите, куда сохранять файлы"))

        self.Select_file.setVisible(False)
        self.Open_dir_to_save.setVisible(False)
        self.Keys_gen.setVisible(False)
        self.dir_to_keys.setVisible(False)
        self.save_text.setVisible(False)
        self.Tip_to_open.setVisible(False)
        self.Select_dir.setVisible(False)
        self.Start.setVisible(False)
        self.End.setVisible(False)
        self.start_txt.setVisible(False)

    def start(self):
        if self.Method.currentIndex() == 0:
            self.Keys_gen.setVisible(True)
            self.Select_dir.setVisible(True)
            self.Open_dir_to_save.setVisible(True)
            self.Select_file.setVisible(True)
            self.Start.setVisible(True)
            self.Tip_to_open.setVisible(True)
            self.Full_Start.setVisible(False)
            self.End.setVisible(True)
            self.Method.setVisible(False)
            self.start_txt.setVisible(True)
            self.start_txt.setText("Вы начали работу с шифрованием")

            self.Select_file.setText("Выберите файл,\n"
                                     "который требуется зашифровать")
        else:
            self.Select_dir.setVisible(True)
            self.Select_file.setVisible(True)
            self.Tip_to_open.setVisible(True)
            self.Full_Start.setVisible(False)
            self.End.setVisible(True)
            self.Start.setVisible(True)
            self.Open_dir_to_save.setVisible(True)
            self.start_txt.setText("Вы начали работу с дешифрованием")
            self.start_txt.setVisible(True)
            self.Method.setVisible(False)
            self.Select_file.setText("Выберите файл,\n"
                                     "который требуется дешифровать")

    def start_click(self):
        try:
            if self.Method.currentIndex() == 0:
                encrypt(self.fname[0], f"{self.curr_dir}/public.pem", self.curr_dir)

                self.save_text.setText("Файл с зашифрованным текстом сохранен в \n" + self.curr_dir +
                                       "/data_encrypted")
                self.save_text.setVisible(True)
            else:
                decrypt(self.fname[0], self.curr_dir + "/private.pem", self.curr_dir)
                self.save_text.setVisible(True)
                self.save_text.setText("Файл с дешифрованным текстом сохранен в\n" + self.curr_dir +
                                       "/data_decrypted")
        except FileNotFoundError:
            class ErrorWindow(QtWidgets.QWidget, Ui_ErrorWindow):
                def __init__(self, parent=None):
                    super(ErrorWindow, self).__init__(parent)
                    self.setupUi(self)

            def errwin(self):
                self.ErrorWindow = ErrorWindow()
                self.ErrorWindow.ErrorText.setText('Не сгенерированы ключи')
                self.ErrorWindow.show()

            errwin(self)
        except IndexError:
            class ErrorWindow(QtWidgets.QWidget, Ui_ErrorWindow):
                def __init__(self, parent=None):
                    super(ErrorWindow, self).__init__(parent)
                    self.setupUi(self)

            def errwin(self):
                self.ErrorWindow = ErrorWindow()
                self.ErrorWindow.ErrorText.setText('Не выбран файл')
                self.ErrorWindow.show()

            errwin(self)

        except cryptography.fernet.InvalidToken:

            class ErrorWindow(QtWidgets.QWidget, Ui_ErrorWindow):
                def __init__(self, parent=None):
                    super(ErrorWindow, self).__init__(parent)
                    self.setupUi(self)

            def errwin(self):
                self.ErrorWindow = ErrorWindow()
                self.ErrorWindow.ErrorText.setText('Не выбран файл')
                self.ErrorWindow.show()

            errwin(self)

    def keys_gen(self):
        try:
            if self.Method.currentIndex() == 0:
                key_gen(self.curr_dir)
                self.dir_to_keys.setText(
                    f"<html><head/><body><p>Ключи сгенерированы в</p><p> {self.curr_dir}"
                    "/private</p><p>"
                    "И " + f"{self.curr_dir}" + "/"
                                                "public</p></body></html>")
                self.dir_to_keys.setVisible(True)
        except PermissionError:
            class ErrorWindow(QtWidgets.QWidget, Ui_ErrorWindow):
                def __init__(self, parent=None):
                    super(ErrorWindow, self).__init__(parent)
                    self.setupUi(self)
            def errwin(self):
                self.ErrorWindow = ErrorWindow()
                self.ErrorWindow.ErrorText.setText('Не выбран путь сохранения файлов')
                self.ErrorWindow.show()

            errwin(self)

    def get_dirr(self):
        self.curr_dir = QFileDialog.getExistingDirectory(self, "Выбрать папку")

    def end(self):
        self.Select_file.setVisible(False)
        self.Open_dir_to_save.setVisible(False)
        self.Keys_gen.setVisible(False)
        self.dir_to_keys.setVisible(False)
        self.save_text.setVisible(False)
        self.Tip_to_open.setVisible(False)
        self.Select_dir.setVisible(False)
        self.Start.setVisible(False)
        self.End.setVisible(False)
        self.Full_Start.setVisible(True)
        self.Method.setVisible(True)
        self.start_txt.setVisible(False)

    def select_dir(self):
        self.fname = QFileDialog.getOpenFileName(None, 'Open file')

    def open_file(self):
        try:
            if self.Method.currentIndex() == 0:
                [file_name, file_ext] = self.fname[0].split('.')
                file_name=file_name + "_encrypted."+file_ext
                os.system(file_name.replace("/", "\\"))
            if self.Method.currentIndex() == 1:
                [file_name, file_ext] = self.fname[0].split('.')
                file_name=file_name + "_decrypted."+file_ext
                file_name=file_name.replace("_encrypted", '')
                os.system(file_name.replace("/", "\\"))
        except IndexError:
            class ErrorWindow(QtWidgets.QWidget, Ui_ErrorWindow):
                def __init__(self, parent=None):
                    super(ErrorWindow, self).__init__(parent)
                    self.setupUi(self)

            def errwin(self):
                self.ErrorWindow = ErrorWindow()
                self.ErrorWindow.ErrorText.setText('Нечего открывать')
                self.ErrorWindow.show()

            errwin(self)