# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_ui_files/Update_details.ui'
#
# Created: Mon Nov  9 06:48:23 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 438)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.eligible_checkBox = QtGui.QCheckBox(Dialog)
        self.eligible_checkBox.setEnabled(False)
        self.eligible_checkBox.setObjectName("eligible_checkBox")
        self.gridLayout.addWidget(self.eligible_checkBox, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.usn_lineEdit = QtGui.QLineEdit(Dialog)
        self.usn_lineEdit.setEnabled(False)
        self.usn_lineEdit.setObjectName("usn_lineEdit")
        self.gridLayout.addWidget(self.usn_lineEdit, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.hasArrears_checkBox = QtGui.QCheckBox(Dialog)
        self.hasArrears_checkBox.setEnabled(False)
        self.hasArrears_checkBox.setObjectName("hasArrears_checkBox")
        self.gridLayout.addWidget(self.hasArrears_checkBox, 6, 1, 1, 1)
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.arrear1_lineEdit = QtGui.QLineEdit(Dialog)
        self.arrear1_lineEdit.setEnabled(False)
        self.arrear1_lineEdit.setObjectName("arrear1_lineEdit")
        self.gridLayout.addWidget(self.arrear1_lineEdit, 8, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
        self.arrear2_lineEdit = QtGui.QLineEdit(Dialog)
        self.arrear2_lineEdit.setEnabled(False)
        self.arrear2_lineEdit.setObjectName("arrear2_lineEdit")
        self.gridLayout.addWidget(self.arrear2_lineEdit, 9, 1, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)
        self.arrear3_lineEdit = QtGui.QLineEdit(Dialog)
        self.arrear3_lineEdit.setEnabled(False)
        self.arrear3_lineEdit.setObjectName("arrear3_lineEdit")
        self.gridLayout.addWidget(self.arrear3_lineEdit, 10, 1, 1, 1)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.arrear4_lineEdit = QtGui.QLineEdit(Dialog)
        self.arrear4_lineEdit.setEnabled(False)
        self.arrear4_lineEdit.setObjectName("arrear4_lineEdit")
        self.gridLayout.addWidget(self.arrear4_lineEdit, 11, 1, 1, 1)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.arrear5_lineEdit = QtGui.QLineEdit(Dialog)
        self.arrear5_lineEdit.setEnabled(False)
        self.arrear5_lineEdit.setObjectName("arrear5_lineEdit")
        self.gridLayout.addWidget(self.arrear5_lineEdit, 12, 1, 1, 1)
        self.update_pushButton = QtGui.QPushButton(Dialog)
        self.update_pushButton.setObjectName("update_pushButton")
        self.gridLayout.addWidget(self.update_pushButton, 13, 0, 1, 1)
        self.name_lineEdit = QtGui.QLineEdit(Dialog)
        self.name_lineEdit.setEnabled(False)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 3, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.usn_comboBox = QtGui.QComboBox(Dialog)
        self.usn_comboBox.setObjectName("usn_comboBox")
        self.gridLayout.addWidget(self.usn_comboBox, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.hasArrears_checkBox, QtCore.SIGNAL("clicked(bool)"), self.arrear1_lineEdit.setEnabled)
        QtCore.QObject.connect(self.hasArrears_checkBox, QtCore.SIGNAL("clicked(bool)"), self.arrear2_lineEdit.setEnabled)
        QtCore.QObject.connect(self.hasArrears_checkBox, QtCore.SIGNAL("clicked(bool)"), self.arrear3_lineEdit.setEnabled)
        QtCore.QObject.connect(self.hasArrears_checkBox, QtCore.SIGNAL("clicked(bool)"), self.arrear4_lineEdit.setEnabled)
        QtCore.QObject.connect(self.hasArrears_checkBox, QtCore.SIGNAL("clicked(bool)"), self.arrear5_lineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add a Student to Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Semester", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Eligible", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Usn", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Has Arrears ?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Serial No.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Arrear Subject Code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "2.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "3.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "4.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "5.", None, QtGui.QApplication.UnicodeUTF8))
        self.update_pushButton.setText(QtGui.QApplication.translate("Dialog", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))

