
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(611, 900)
        Form.setStyleSheet("")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 150, 231, 31))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(301, 16777215))
        self.lineEdit_2.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 410, 231, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(51, 55, 64);\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 460, 231, 31))
        self.lineEdit_5.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 690, 71, 31))
        self.lineEdit_4.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 740, 141, 41))
        self.pushButton.setStyleSheet("background-color: rgb(154, 136, 153);\n"
"background-color: rgb(181, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(-20, -30, 661, 1091))
        self.label_12.setStyleSheet("border-left-color: rgb(255, 85, 127);\n"
"border-right-color: rgb(182, 255, 142);")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../12.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 30, 381, 51))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 460, 221, 21))
        self.label_2.setObjectName("label_2")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(40, 410, 221, 31))
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 520, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 560, 121, 31))
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(70, 610, 511, 61))
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 250, 231, 31))
        self.comboBox_2.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 250, 81, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 200, 231, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(51, 55, 64);\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 150, 221, 21))
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(90, 200, 61, 31))
        self.label_14.setObjectName("label_14")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 300, 121, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(230, 300, 231, 31))
        self.lineEdit_7.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(90, 350, 81, 31))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 350, 241, 31))
        self.comboBox.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 520, 231, 31))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(301, 16777215))
        self.lineEdit_8.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setDragEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(230, 560, 251, 31))
        self.lineEdit_9.setStyleSheet("border-color: rgb(253, 253, 253);\n"
"background-color: rgb(51, 55, 64);")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_12.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_4.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_13.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_10.raise_()
        self.comboBox_2.raise_()
        self.label_4.raise_()
        self.lineEdit_6.raise_()
        self.label_6.raise_()
        self.label_14.raise_()
        self.label_7.raise_()
        self.lineEdit_7.raise_()
        self.label_8.raise_()
        self.comboBox.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "AJOUTER"))
        self.label.setText(_translate("Form", "AJOUT NOTE"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">CODE MATIERE:</span></p></body></html>"))
        self.label_13.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">NUM D\'INSCRIPTION:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Note DS:</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Note EX:</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">voulez vous ajouter une autre note?(1pour OUI |0 pour NON</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "CPI 1"))
        self.comboBox_2.setItemText(1, _translate("Form", "CPI 2"))
        self.comboBox_2.setItemText(2, _translate("Form", "L1 INFO"))
        self.comboBox_2.setItemText(3, _translate("Form", "L1 TIC"))
        self.comboBox_2.setItemText(4, _translate("Form", "L1 EEA"))
        self.comboBox_2.setItemText(5, _translate("Form", "L1 MATH"))
        self.comboBox_2.setItemText(6, _translate("Form", "L2 INFO "))
        self.comboBox_2.setItemText(7, _translate("Form", "L2 TIC"))
        self.comboBox_2.setItemText(8, _translate("Form", "L2 EEA"))
        self.comboBox_2.setItemText(9, _translate("Form", "L2 MATH"))
        self.comboBox_2.setItemText(10, _translate("Form", "L3 INFO"))
        self.comboBox_2.setItemText(11, _translate("Form", "L3 TIC"))
        self.comboBox_2.setItemText(12, _translate("Form", "L3 EEA"))
        self.comboBox_2.setItemText(13, _translate("Form", "ING 1"))
        self.comboBox_2.setItemText(14, _translate("Form", "ING2"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">section:</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">CODE NOTE:</span></p></body></html>"))
        self.label_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nom:</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">coefficient:</span></p><p><br/></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">semestre:</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "1"))
        self.comboBox.setItemText(1, _translate("Form", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
