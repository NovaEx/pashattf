# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 2, 1, 1, 1)
        self.selectListFiles = QtWidgets.QPushButton(self.centralwidget)
        self.selectListFiles.setObjectName("selectListFiles")
        self.gridLayout.addWidget(self.selectListFiles, 0, 0, 1, 1)
        self.selectTTF = QtWidgets.QPushButton(self.centralwidget)
        self.selectTTF.setObjectName("selectTTF")
        self.gridLayout.addWidget(self.selectTTF, 1, 0, 1, 1)
        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setObjectName("done")
        self.gridLayout.addWidget(self.done, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectListFiles.setText(_translate("MainWindow", "Список файлов"))
        self.selectTTF.setText(_translate("MainWindow", "Выбрать TTF"))
        self.done.setText(_translate("MainWindow", "Done"))
