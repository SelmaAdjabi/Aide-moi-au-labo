#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import gui  # import du fichier gui.py généré par pyuic5
import time


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = gui.Ui_QDialogLab()
        self.ui.setupUi(self)

        self.ui.calculateButton.clicked.connect(self.handleCalculate)

    def handleCalculate(self):
        fd = self.ui.fd.text()
        vi = self.ui.vi.text()
        vf = self.ui.vf.text()

        if fd == "" and vi == "" and vf == "":
            msgBox = QMessageBox()
            msgBox.setText("Il faut remplir au moins deux valeurs !")
            msgBox.exec()
        else:
            fd = float(fd)
            vf = float(vf)
            vi = vf / fd
            vd = vf - vi
            self.ui.vi.setText(str(vi))
            self.ui.vd.setText(str(vd))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())