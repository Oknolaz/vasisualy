from ..ui import about_window
from PyQt5 import QtWidgets

class ShowAboutWindow(QtWidgets.QWidget, about_window.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
