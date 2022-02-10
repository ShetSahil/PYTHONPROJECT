# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys,lg
import mysql.connector

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1141, 850)
        Form.setStyleSheet("QPushButton#pushButton{\n"
"    background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,2555,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(255,107,107,255);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color:rgba(255,107,107,255);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 40, 861, 701))
        self.label.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(107, 175, 164, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(440, 60, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 230, 191, 31))
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 310, 191, 22))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 390, 191, 22))
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 470, 191, 22))
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 550, 191, 22))
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(480, 170, 381, 161))
        self.lineEdit_6.setStyleSheet("QLineEdit {\n"
" border: 2px solid gray;\n"
" border-radius: 10px;\n"
" background-color:rgba(0,0,0,0);\n"
" \n"
" border-bottom-color:rgba(46,82,101,200);\n"
" color:rgb(0,0,0);\n"
" padding-bottom:7px;\n"
"\n"
"}")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_6.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 390, 191, 22))
        self.lineEdit_7.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 470, 191, 22))
        self.lineEdit_8.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(690, 620, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,2555,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(255,107,107,255);\n"
"    background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color:rgba(255,107,107,255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(700, 360, 241, 211))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#090909;\">SIGN UP</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "ADHAAR CARD NUMBER"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "FULL NAME"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "EMAIL-ID"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "USERNAME"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "MOBILE NUMBER"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "ADDRESS"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "PASSWORD"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "CONFIRM PASSWORD"))
        self.pushButton.setText(_translate("Form", "SIGN UP"))
        self.label_3.setWhatsThis(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/hand.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/hand.png\"/></p></body></html>"))
        self.pushButton.clicked.connect(self.signup)
    def signup(self): 
        uid = self.lineEdit.text()
        fname = self.lineEdit_2.text()
        Email = self.lineEdit_3.text()
        un = self.lineEdit_4.text()
        mobile = self.lineEdit_5.text()
        add = self.lineEdit_6.text()
        pwd = self.lineEdit_7.text() 
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbms"
        )
        
        mycursor = mydb.cursor()

        sql = "INSERT INTO acc (` Uid`,`full_name`,`E_mail`,`username`,`mobile_no`,`add`,`pwd`) VALUES (%s, %s,%s, %s,%s, %s,%s)"
        val = (uid, fname,Email,un,mobile,add,pwd)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.") 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
