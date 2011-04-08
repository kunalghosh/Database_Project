# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_ui_files/delete.ui'
#
# Created: Thu Nov 19 06:56:03 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 413)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.usn_lineEdit = QtGui.QLineEdit(Dialog)
        self.usn_lineEdit.setObjectName("usn_lineEdit")
        self.gridLayout.addWidget(self.usn_lineEdit, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)
        self.name_lineEdit = QtGui.QLineEdit(Dialog)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)
        self.sem_lineEdit = QtGui.QLineEdit(Dialog)
        self.sem_lineEdit.setObjectName("sem_lineEdit")
        self.gridLayout.addWidget(self.sem_lineEdit, 2, 3, 1, 1)
        self.display_webView = QtWebKit.QWebView(Dialog)
        self.display_webView.setUrl(QtCore.QUrl("about:blank"))
        self.display_webView.setObjectName("display_webView")
        self.gridLayout.addWidget(self.display_webView, 3, 0, 1, 4)
        self.search_pushButton = QtGui.QPushButton(Dialog)
        self.search_pushButton.setObjectName("search_pushButton")
        self.gridLayout.addWidget(self.search_pushButton, 4, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(125, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Delete Student Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Search Student By USN:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Search Student By Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Search Student By Semester:", None, QtGui.QApplication.UnicodeUTF8))
        self.search_pushButton.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
