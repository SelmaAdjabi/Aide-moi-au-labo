# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QDialogLab(object):
    def setupUi(self, QDialogLab):
        QDialogLab.setObjectName("QDialogLab")
        QDialogLab.resize(637, 498)
        self.label = QtWidgets.QLabel(QDialogLab)
        self.label.setGeometry(QtCore.QRect(230, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(46, 52, 54)")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(QDialogLab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 631, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.fd = QtWidgets.QLineEdit(self.tab)
        self.fd.setGeometry(QtCore.QRect(90, 70, 161, 41))
        self.fd.setObjectName("fd")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.vi = QtWidgets.QLineEdit(self.tab)
        self.vi.setGeometry(QtCore.QRect(360, 70, 161, 41))
        self.vi.setObjectName("vi")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(370, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(370, 140, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.vf = QtWidgets.QLineEdit(self.tab)
        self.vf.setGeometry(QtCore.QRect(360, 180, 161, 41))
        self.vf.setText("")
        self.vf.setObjectName("vf")
        self.vd = QtWidgets.QLineEdit(self.tab)
        self.vd.setGeometry(QtCore.QRect(90, 180, 161, 41))
        self.vd.setObjectName("vd")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(100, 140, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(250, 260, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(300, 50, 20, 211))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.calculateButton = QtWidgets.QPushButton(self.tab)
        self.calculateButton.setGeometry(QtCore.QRect(230, 284, 151, 31))
        self.calculateButton.setObjectName("calculateButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(380, 20, 161, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(380, 80, 161, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalSlider_5 = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(380, 60, 160, 16))
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.horizontalSlider_6 = QtWidgets.QSlider(self.tab_2)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(380, 120, 160, 16))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(380, 160, 161, 41))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(380, 210, 161, 41))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 210, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(380, 260, 161, 41))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(20, 260, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.line_3 = QtWidgets.QFrame(self.tab_2)
        self.line_3.setGeometry(QtCore.QRect(30, 140, 561, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(20, 300, 561, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 320, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(380, 320, 161, 41))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_2 = QtWidgets.QLabel(QDialogLab)
        self.label_2.setGeometry(QtCore.QRect(590, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(136, 136, 136)")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(QDialogLab)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QDialogLab)

    def retranslateUi(self, QDialogLab):
        _translate = QtCore.QCoreApplication.translate
        QDialogLab.setWindowTitle(_translate("QDialogLab", "Dialog"))
        self.label.setText(_translate("QDialogLab", "AIDE MOI AU LABO"))
        self.label_4.setText(_translate("QDialogLab", "Facteur de dilution"))
        self.label_5.setText(_translate("QDialogLab", "Volume Initiale"))
        self.label_6.setText(_translate("QDialogLab", "Volume finale"))
        self.label_7.setText(_translate("QDialogLab", "Volume diluant"))
        self.calculateButton.setText(_translate("QDialogLab", "Calculer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("QDialogLab", "Facteur de dilution"))
        self.label_8.setText(_translate("QDialogLab", "Volume de chaque puit"))
        self.label_9.setText(_translate("QDialogLab", "Volume de l\'échantillon (ARN)"))
        self.label_10.setText(_translate("QDialogLab", "Volume de l\'enzyme"))
        self.label_11.setText(_translate("QDialogLab", "Volume de l\'amorce 1"))
        self.label_12.setText(_translate("QDialogLab", "Volume de l\'amorce 2"))
        self.label_13.setText(_translate("QDialogLab", "Volume de l\'eau"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("QDialogLab", "Calcul MIX PCR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("QDialogLab", "Convertisseur"))
        self.label_2.setText(_translate("QDialogLab", "A.S © "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QDialogLab = QtWidgets.QDialog()
    ui = Ui_QDialogLab()
    ui.setupUi(QDialogLab)
    QDialogLab.show()
    sys.exit(app.exec_())

