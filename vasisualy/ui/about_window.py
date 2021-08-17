# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt/about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 312)
        Dialog.setMinimumSize(QtCore.QSize(400, 312))
        Dialog.setMaximumSize(QtCore.QSize(400, 312))
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(120, 10, 171, 121))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(f"vasisualy/ui/vas.png"))
        self.image.setObjectName("image")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(20, 120, 361, 41))
        self.name.setTextFormat(QtCore.Qt.MarkdownText)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setWordWrap(True)
        self.name.setObjectName("name")
        self.version = QtWidgets.QLabel(Dialog)
        self.version.setGeometry(QtCore.QRect(30, 170, 351, 22))
        self.version.setTextFormat(QtCore.Qt.MarkdownText)
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName("version")
        self.link = QtWidgets.QLabel(Dialog)
        self.link.setGeometry(QtCore.QRect(20, 200, 361, 22))
        self.link.setTextFormat(QtCore.Qt.MarkdownText)
        self.link.setAlignment(QtCore.Qt.AlignCenter)
        self.link.setOpenExternalLinks(True)
        self.link.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.link.setObjectName("link")
        self.license = QtWidgets.QLabel(Dialog)
        self.license.setGeometry(QtCore.QRect(20, 240, 361, 61))
        self.license.setTextFormat(QtCore.Qt.MarkdownText)
        self.license.setAlignment(QtCore.Qt.AlignCenter)
        self.license.setWordWrap(True)
        self.license.setOpenExternalLinks(True)
        self.license.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.license.setObjectName("license")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "О программе"))
        self.name.setText(_translate("Dialog", "**Vasisualy - свободный русскоязычный голосовой ассистент.**"))
        self.version.setText(_translate("Dialog", "0.8.0"))
        self.link.setText(_translate("Dialog", "https://github.com/Oknolaz/vasisualy"))
        self.license.setText(_translate("Dialog", "Это приложение распространяется без каких-либо гарантий.\n"
"Подробнее в [GNU General Public License 3.0](https://gnu.org/licenses/gpl-3.0.en.html)."))
