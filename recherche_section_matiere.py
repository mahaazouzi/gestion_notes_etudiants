# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recherche_section_matiere.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 407)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 210, 231, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(41, 44, 49);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 140, 461, 81))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(-10, -70, 921, 831))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../12.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(560, 340, 141, 41))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(211, 207, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 40, 611, 81))
        self.label.setStyleSheet("font: 63 18pt \"Open Sans Semibold\";")
        self.label.setObjectName("label")
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Section :</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "AFFICHER"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" text-decoration: underline; color:#ffffff;\">RECHERCHE PAR SECTION D\'UNE MATIERE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())