# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 109)
        Form.setMaximumSize(QtCore.QSize(400, 109))
        self.radioname = QtWidgets.QLabel(Form)
        self.radioname.setGeometry(QtCore.QRect(10, 10, 381, 41))
        self.radioname.setAlignment(QtCore.Qt.AlignCenter)
        self.radioname.setWordWrap(True)
        self.radioname.setObjectName("radioname")
        self.playpause = QtWidgets.QPushButton(Form)
        self.playpause.setGeometry(QtCore.QRect(100, 60, 201, 41))
        self.playpause.setObjectName("playpause")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vasisualy Radio Player"))
        self.radioname.setText(_translate("Form", "Радиостанция"))
        self.playpause.setText(_translate("Form", "Play"))
