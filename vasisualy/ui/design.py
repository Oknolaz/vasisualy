# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt/vasisualy-design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 663)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"vasisualy/assets/icons/white icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(35, 28))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 480, 31))
        self.menuBar.setObjectName("menuBar")
        self.settingsMenu = QtWidgets.QMenu(self.menuBar)
        self.settingsMenu.setObjectName("settingsMenu")
        self.aboutMenu = QtWidgets.QMenu(self.menuBar)
        self.aboutMenu.setObjectName("aboutMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.settings = QtWidgets.QAction(MainWindow)
        self.settings.setObjectName("settings")
        self.about = QtWidgets.QAction(MainWindow)
        self.about.setObjectName("about")
        self.settingsMenu.addAction(self.settings)
        self.settingsMenu.addSeparator()
        self.aboutMenu.addAction(self.about)
        self.menuBar.addAction(self.settingsMenu.menuAction())
        self.menuBar.addAction(self.aboutMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vasisualy"))
        self.settingsMenu.setTitle(_translate("MainWindow", "Параметры"))
        self.aboutMenu.setTitle(_translate("MainWindow", "Справка"))
        self.settings.setText(_translate("MainWindow", "Настройки"))
        self.about.setText(_translate("MainWindow", "О программе"))
