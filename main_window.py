# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search_request = QtWidgets.QTextEdit(self.centralwidget)
        self.search_request.setGeometry(QtCore.QRect(20, 60, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.search_request.setFont(font)
        self.search_request.setObjectName("search_request")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.agents_count = QtWidgets.QSpinBox(self.centralwidget)
        self.agents_count.setGeometry(QtCore.QRect(340, 110, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.agents_count.setFont(font)
        self.agents_count.setMinimum(1)
        self.agents_count.setMaximum(20)
        self.agents_count.setObjectName("agents_count")
        self.agents_list = QtWidgets.QListWidget(self.centralwidget)
        self.agents_list.setGeometry(QtCore.QRect(20, 200, 221, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.agents_list.setFont(font)
        self.agents_list.setObjectName("agents_list")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 170, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.start_search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_search_btn.setGeometry(QtCore.QRect(380, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.start_search_btn.setFont(font)
        self.start_search_btn.setObjectName("start_search_btn")
        self.search_results = QtWidgets.QTextBrowser(self.centralwidget)
        self.search_results.setGeometry(QtCore.QRect(330, 210, 341, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.search_results.setFont(font)
        self.search_results.setObjectName("search_results")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Агентный поиск в сети Интернет"))
        self.label.setText(_translate("MainWindow", "Введите запрос для поиска в Интернете"))
        self.search_request.setPlaceholderText(_translate("MainWindow", "Введите запрос"))
        self.label_2.setText(_translate("MainWindow", "Введите количество агентов"))
        self.label_3.setText(_translate("MainWindow", "Список агентов"))
        self.label_4.setText(_translate("MainWindow", "Результаты поиска агента"))
        self.start_search_btn.setText(_translate("MainWindow", "Начать поиск"))
