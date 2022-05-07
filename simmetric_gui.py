from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from simmetric import *
import os


class Ui_simmetric(object):
    fname = ""

    def setupUi(self, simmetric):
        simmetric.setObjectName("Simmetric")
        simmetric.resize(700, 700)
        self.Selector = QtWidgets.QComboBox(simmetric)
        self.Selector.setGeometry(QtCore.QRect(30, 30, 650, 30))
        self.Selector.setObjectName("Selector")
        self.Selector.addItem("")
        self.Selector.addItem("")
        self.Start = QtWidgets.QPushButton(simmetric)
        self.Start.setGeometry(QtCore.QRect(30, 360, 650, 30))
        self.Start.setObjectName("Start")
        self.Full_start = QtWidgets.QPushButton(simmetric)
        self.Full_start.setGeometry(QtCore.QRect(30, 70, 650, 30))
        self.Full_start.setObjectName("Full_start")
        self.start_txt = QtWidgets.QLabel(simmetric)
        self.start_txt.setGeometry(30, 30, 650, 30)
        self.start_txt.setObjectName("start_txt")
        self.Key_gen = QtWidgets.QPushButton(simmetric)
        self.Key_gen.setGeometry(QtCore.QRect(30, 70, 650, 30))
        self.Key_gen.setObjectName("Key_gen")
        self.dir_to_key = QtWidgets.QLabel(simmetric)
        self.dir_to_key.setGeometry(QtCore.QRect(30, 100, 650, 100))
        self.dir_to_key.setObjectName("dir_to_key")
        self.Tip_for_open_file = QtWidgets.QLabel(simmetric)
        self.Tip_for_open_file.setGeometry(QtCore.QRect(30, 220, 250, 40))
        self.Tip_for_open_file.setObjectName("Tip_for_open_file")
        self.Tip_for_open_decr = QtWidgets.QLabel(simmetric)
        self.Tip_for_open_decr.setGeometry(QtCore.QRect(30, 220, 250, 40))
        self.Tip_for_open_decr.setObjectName("Tip_for_open_decr")
        self.open_file_btn = QtWidgets.QPushButton(simmetric)
        self.open_file_btn.setGeometry(QtCore.QRect(230, 225, 450, 30))
        self.open_file_btn.setObjectName("open_file_btn")
        self.encr_save_text = QtWidgets.QLabel(simmetric)
        self.encr_save_text.setGeometry(QtCore.QRect(30, 280, 650, 60))
        self.encr_save_text.setObjectName("encr_save_text")
        self.Tip_toOpen_saved = QtWidgets.QLabel(simmetric)
        self.Tip_toOpen_saved.setGeometry(QtCore.QRect(30, 420, 200, 50))
        self.Tip_toOpen_saved.setObjectName("Tip_toOpen_saved")
        self.Open_Saved_File = QtWidgets.QPushButton(simmetric)
        self.Open_Saved_File.setGeometry(QtCore.QRect(240, 420, 440, 30))
        self.Open_Saved_File.setObjectName("Open_Saved_File")
        self.Full_end = QtWidgets.QPushButton(simmetric)
        self.Full_end.setGeometry(QtCore.QRect(30, 500, 650, 30))
        self.Full_end.setObjectName("Full_end")

        self.retranslateUi(simmetric)
        QtCore.QMetaObject.connectSlotsByName(simmetric)

        self.Full_start.clicked.connect(self.full_start)
        self.Key_gen.clicked.connect(self.key_gen)
        self.open_file_btn.clicked.connect(self.select_dir)
        self.Start.clicked.connect(self.start_click)
        self.Open_Saved_File.clicked.connect(self.open_file)
        self.Full_end.clicked.connect(self.end)

    def retranslateUi(self, simmetric):
        _translate = QtCore.QCoreApplication.translate
        simmetric.setWindowTitle(_translate("simmetric", "Шифратор"))
        self.Selector.setItemText(0, _translate("simmetric", "Шифрование"))
        self.Selector.setItemText(1, _translate("simmetric", "Дешифрование"))
        self.Full_start.setText(_translate("simmetric", "Начать работу с выбранным методом"))
        self.start_txt.setText(_translate("simmetric", "Вы начали работу с шифрованием"))
        self.Start.setText(_translate("simmetric", "Начать работу"))
        self.Key_gen.setText(_translate("simmetric", "Нажмите, чтобы сгенерировать ключ"))
        self.dir_to_key.setText(_translate("simmetric", "<html><head/><body><p>Ключ успешно сохранен в</p><p> "
                                                        "C:\\Users\\paksh\\PycharmProjects\\encryptor\\"
                                                        "for_simmetric\\simmetric_key и</p><p> "
                                                        "C:\\Users\\paksh\\PycharmProjects\\encryptor"
                                                        "\\for_simmetric\\simmetric_key.txt</p></body></html>"))
        self.Tip_for_open_file.setText(_translate("simmetric", "Выберите файл, который \n"
                                                               "требуется зашифровать"))
        self.open_file_btn.setText(_translate("simmetric", "Нажмите, чтобы выбрать файл"))
        self.encr_save_text.setText(_translate("simmetric", "Зашифрованный текст сохранен в\n"
                                                             "C:\\Users\\paksh\\PycharmProjects\\encryptor\\"
                                                             "for_simmetric\\data_encrypted.txt"))
        self.Tip_toOpen_saved.setText(_translate("simmetric", "Нажмите, чтобы открыть\n"
                                                               "полученный файл"))
        self.Open_Saved_File.setText(_translate("simmetric", "Открыть файл"))
        self.Full_end.setText(_translate("simmetric", "Закончить работу с выбранным методом"))

        self.Key_gen.setVisible(False)
        self.dir_to_key.setVisible(False)
        self.Tip_for_open_file.setVisible(False)
        self.open_file_btn.setVisible(False)
        self.encr_save_text.setVisible(False)
        self.Tip_toOpen_saved.setVisible(False)
        self.Open_Saved_File.setVisible(False)
        self.Full_end.setVisible(False)
        self.Start.setVisible(False)
        self.start_txt.setVisible(False)

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
            self.start_txt.setVisible(True)
            self.Selector.setVisible(False)
        else:
            self.Full_start.setVisible(False)
            self.open_file_btn.setVisible(True)
            self.Start.setVisible(True)
            self.Tip_toOpen_saved.setVisible(True)
            self.Open_Saved_File.setVisible(True)
            self.Full_end.setVisible(True)
            self.start_txt.setVisible(True)
            self.Selector.setVisible(False)
            self.Tip_for_open_file.setVisible(True)
            self.start_txt.setText("Вы начали работу с дешифрованием")
            self.Tip_for_open_file.setText("Выберите файл, который \n"
                                           "требуется дешифровать")
            self.encr_save_text.setText("<html><head/><body><p>Дешифрованный текст сохранен в</p><p>"
                                                            "C:\\\\Users\\\\paksh\\\\PycharmProjects\\\\encryptor"
                                                            "\\\\for_simmetric\\\\data_decrypted.txt</p></body></html>")

    def key_gen(self):
        write_key()
        self.dir_to_key.setVisible(True)

    def start_click(self):
        if self.Selector.currentIndex() == 0:
            encrypt(self.fname[0])
            self.encr_save_text.setVisible(True)
        else:
            decrypt(self.fname[0])
            self.encr_save_text.setVisible(True)

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
        self.Tip_toOpen_saved.setVisible(False)
        self.Open_Saved_File.setVisible(False)
        self.Full_end.setVisible(False)
        self.Start.setVisible(False)
        self.Full_start.setVisible(True)
        self.start_txt.setVisible(False)
        self.Selector.setVisible(True)

