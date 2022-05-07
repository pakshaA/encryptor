from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from simmetric import *
import os


class Ui_simmetric(object):
    fname = ""

    def setupUi(self, simmetric):
        simmetric.setObjectName("Simmetric")
        simmetric.resize(700, 500)
        self.Selector = QtWidgets.QComboBox(simmetric)
        self.Selector.setGeometry(QtCore.QRect(30, 30, 100, 25))
        self.Selector.setObjectName("Selector")
        self.Selector.addItem("")
        self.Selector.addItem("")
        self.Start = QtWidgets.QPushButton(simmetric)
        self.Start.setGeometry(QtCore.QRect(30, 220, 650, 30))
        self.Start.setObjectName("Start")
        self.Full_start = QtWidgets.QPushButton(simmetric)
        self.Full_start.setGeometry(QtCore.QRect(30, 70, 650, 30))
        self.Full_start.setObjectName("Full_start")
        self.Key_gen = QtWidgets.QPushButton(simmetric)
        self.Key_gen.setGeometry(QtCore.QRect(180, 30, 500, 25))
        self.Key_gen.setObjectName("Key_gen")
        self.dir_to_key = QtWidgets.QLabel(simmetric)
        self.dir_to_key.setGeometry(QtCore.QRect(30, 60, 650, 100))
        self.dir_to_key.setObjectName("dir_to_key")
        self.Tip_for_open_file = QtWidgets.QLabel(simmetric)
        self.Tip_for_open_file.setGeometry(QtCore.QRect(30, 160, 250, 40))
        self.Tip_for_open_file.setObjectName("Tip_for_open_file")
        self.Tip_for_open_decr = QtWidgets.QLabel(simmetric)
        self.Tip_for_open_decr.setGeometry(QtCore.QRect(30, 160, 250, 30))
        self.Tip_for_open_decr.setObjectName("Tip_for_open_decr")
        self.open_file_btn = QtWidgets.QPushButton(simmetric)
        self.open_file_btn.setGeometry(QtCore.QRect(230, 165, 450, 30))
        self.open_file_btn.setObjectName("open_file_btn")
        self.encr_save_text = QtWidgets.QLabel(simmetric)
        self.encr_save_text.setGeometry(QtCore.QRect(30, 265, 650, 60))
        self.encr_save_text.setObjectName("encr_save_text")
        self.decr_text_save = QtWidgets.QLabel(simmetric)
        self.decr_text_save.setGeometry(QtCore.QRect(30, 265, 650, 60))
        self.decr_text_save.setObjectName("decr_text_save")
        self.Tip_toOpen_saved = QtWidgets.QLabel(simmetric)
        self.Tip_toOpen_saved.setGeometry(QtCore.QRect(30, 340, 200, 50))
        self.Tip_toOpen_saved.setObjectName("Tip_toOpen_saved")
        self.Open_Saved_File = QtWidgets.QPushButton(simmetric)
        self.Open_Saved_File.setGeometry(QtCore.QRect(240, 340, 440, 30))
        self.Open_Saved_File.setObjectName("Open_Saved_File")
        self.Full_end = QtWidgets.QPushButton(simmetric)
        self.Full_end.setGeometry(QtCore.QRect(30, 405, 650, 25))
        self.Full_end.setObjectName("Full_end")

        self.retranslateUi(simmetric)
        QtCore.QMetaObject.connectSlotsByName(simmetric)

        self.Full_start.clicked.connect(self.full_start)
        self.Key_gen.clicked.connect(self.key_gen)
        self.open_file_btn.clicked.connect(self.select_dir)
        self.Start.clicked.connect(self.start_click)
        self.Open_Saved_File.clicked.connect(self.open_file)
        self.Full_end.clicked.connect(self.end)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифратор"))
        self.Selector.setItemText(0, _translate("MainWindow", "Шифрование"))
        self.Selector.setItemText(1, _translate("MainWindow", "Дешифрование"))
        self.Full_start.setText(_translate("MainWindow", "Начать работу с выбранным методом"))
        self.Start.setText(_translate("MainWindow", "Начать работу"))
        self.Key_gen.setText(_translate("MainWindow", "Нажмите, чтобы сгенерировать ключ"))
        self.dir_to_key.setText(_translate("MainWindow", "<html><head/><body><p>Ключ успешно сохранен в</p><p> "
                                                         "C:\\Users\\paksh\\PycharmProjects\\encryptor\\"
                                                         "for_simmetric\\simmetric_key и</p><p> "
                                                         "C:\\Users\\paksh\\PycharmProjects\\encryptor"
                                                         "\\for_simmetric\\simmetric_key.txt</p></body></html>"))
        self.Tip_for_open_file.setText(_translate("MainWindow", "Выберите файл, который \n"
                                                                "требуется зашифровать"))
        self.Tip_for_open_decr.setText(_translate("MainWindow", "Выберите файл, который \n"
                                                                "требуется дешифровать"))
        self.open_file_btn.setText(_translate("MainWindow", "Нажмите, чтобы выбрать файл"))
        self.encr_save_text.setText(_translate("MainWindow", "Зашифрованный текст сохранен в\n"
                                                             "C:\\Users\\paksh\\PycharmProjects\\encryptor\\"
                                                             "for_simmetric\\data_encrypted.txt"))
        self.decr_text_save.setText(_translate("MainWindow", "<html><head/><body><p>Дешифрованный текст сохранен в</p><p>"
                                                             "C:\\\\Users\\\\paksh\\\\PycharmProjects\\\\encryptor"
                                                             "\\\\for_simmetric\\\\data_decrypted.txt</p></body></html>"))
        self.Tip_toOpen_saved.setText(_translate("MainWindow", "Нажмите, чтобы открыть\n"
                                                               "полученный файл"))
        self.Open_Saved_File.setText(_translate("MainWindow", "Открыть файл"))
        self.Full_end.setText(_translate("MainWindow", "Закончить работу с выбранным методом"))

        self.Key_gen.setVisible(False)
        self.dir_to_key.setVisible(False)
        self.Tip_for_open_file.setVisible(False)
        self.Tip_for_open_decr.setVisible(False)
        self.open_file_btn.setVisible(False)
        self.encr_save_text.setVisible(False)
        self.decr_text_save.setVisible(False)
        self.Tip_toOpen_saved.setVisible(False)
        self.Open_Saved_File.setVisible(False)
        self.Full_end.setVisible(False)
        self.Start.setVisible(False)

    def full_start(self):
        if self.Selector.currentIndex() == 0:
            self.Full_start.setVisible(False)
            self.Key_gen.setVisible(True)
            self.Tip_for_open_file.setVisible(True)
            self.open_file_btn.setVisible(True)
            self.Start.setVisible(True)
            self.Tip_toOpen_saved.setVisible(True)
            self.Open_Saved_File.setVisible(True)
            self.Full_end.setVisible(True)
        else:
            self.Full_start.setVisible(False)
            self.Tip_for_open_decr.setVisible(True)
            self.open_file_btn.setVisible(True)
            self.Start.setVisible(True)
            self.Tip_toOpen_saved.setVisible(True)
            self.Open_Saved_File.setVisible(True)
            self.Full_end.setVisible(True)

    def key_gen(self):
        write_key()
        self.dir_to_key.setVisible(True)

    def start_click(self):
        if self.Selector.currentIndex() == 0:
            encrypt(self.fname[0])
            self.encr_save_text.setVisible(True)
        else:
            decrypt(self.fname[0])
            self.decr_text_save.setVisible(True)

    def select_dir(self):
     self.fname = QFileDialog.getOpenFileName(None, 'Open file', 'C:\\Users\\paksh\\PycharmProjects\\encryptor\\'
                                                                 'for_simmetric\\', "Text files (*.txt)")

    def open_file(self):
        if self.Selector.currentIndex() == 0:
            os.system("C:\\Users\\paksh\\PycharmProjects\\encryptor\\for_simmetric\\data_encrypted.txt")
        if self.Selector.currentIndex() == 1:
            os.system("C:\\Users\\paksh\\PycharmProjects\\encryptor\\for_simmetric"
                      "\\data_decrypted.txt")

    def end(self):
        self.Key_gen.setVisible(False)
        self.dir_to_key.setVisible(False)
        self.Tip_for_open_file.setVisible(False)
        self.Tip_for_open_decr.setVisible(False)
        self.open_file_btn.setVisible(False)
        self.encr_save_text.setVisible(False)
        self.decr_text_save.setVisible(False)
        self.Tip_toOpen_saved.setVisible(False)
        self.Open_Saved_File.setVisible(False)
        self.Full_end.setVisible(False)
        self.Start.setVisible(False)
        self.Full_start.setVisible(True)

