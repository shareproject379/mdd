# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BasicInfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class BasicInfoUiDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(275, 253)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        Dialog.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 180, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.leRsrp = QtWidgets.QLineEdit(Dialog)
        self.leRsrp.setGeometry(QtCore.QRect(100, 30, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.leRsrp.setFont(font)
        self.leRsrp.setObjectName("leRsrp")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 47, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 47, 16))
        self.label_2.setObjectName("label_2")
        self.leRsrq = QtWidgets.QLineEdit(Dialog)
        self.leRsrq.setGeometry(QtCore.QRect(100, 60, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.leRsrq.setFont(font)
        self.leRsrq.setObjectName("leRsrq")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 47, 16))
        self.label_3.setObjectName("label_3")
        self.leSinr = QtWidgets.QLineEdit(Dialog)
        self.leSinr.setGeometry(QtCore.QRect(100, 90, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.leSinr.setFont(font)
        self.leSinr.setObjectName("leSinr")
        self.leIemi = QtWidgets.QLineEdit(Dialog)
        self.leIemi.setGeometry(QtCore.QRect(100, 120, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.leIemi.setFont(font)
        self.leIemi.setObjectName("leIemi")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 47, 16))
        self.label_4.setObjectName("label_4")
        self.leIccid = QtWidgets.QLineEdit(Dialog)
        self.leIccid.setGeometry(QtCore.QRect(100, 150, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.leIccid.setFont(font)
        self.leIccid.setObjectName("leIccid")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 47, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.leRsrp.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "نمایش اطلاعات"))
        self.label.setText(_translate("Dialog", "RSRP:"))
        self.label_2.setText(_translate("Dialog", "RSRQ:"))
        self.label_3.setText(_translate("Dialog", "SINR:"))
        self.label_4.setText(_translate("Dialog", "IMEI:"))
        self.label_5.setText(_translate("Dialog", "ICCID:"))
