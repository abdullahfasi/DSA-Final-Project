# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messagingui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 559)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-95, -109, 1351, 171))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 0, 91, 61))
        self.label.setStyleSheet("image: url(:/newPrefix/homelinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.homelabel = QtWidgets.QLabel(Dialog)
        self.homelabel.setGeometry(QtCore.QRect(426, 2, 71, 61))
        self.homelabel.setStyleSheet("image: url(:/newPrefix/homepic.jpg);")
        self.homelabel.setText("")
        self.homelabel.setObjectName("homelabel")
        self.networklabel = QtWidgets.QLabel(Dialog)
        self.networklabel.setGeometry(QtCore.QRect(560, 0, 81, 61))
        self.networklabel.setStyleSheet("image: url(:/newPrefix/networkpic.jpg);")
        self.networklabel.setText("")
        self.networklabel.setObjectName("networklabel")
        self.messaginlabel = QtWidgets.QLabel(Dialog)
        self.messaginlabel.setGeometry(QtCore.QRect(700, 0, 81, 61))
        self.messaginlabel.setStyleSheet("image: url(:/newPrefix/messagepic.jpg);")
        self.messaginlabel.setText("")
        self.messaginlabel.setObjectName("messaginlabel")
        self.profilelabel = QtWidgets.QLabel(Dialog)
        self.profilelabel.setGeometry(QtCore.QRect(840, 0, 81, 61))
        self.profilelabel.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.profilelabel.setText("")
        self.profilelabel.setObjectName("profilelabel")
        self.friendstable = QtWidgets.QTableWidget(Dialog)
        self.friendstable.setGeometry(QtCore.QRect(140, 200, 211, 291))
        self.friendstable.setStyleSheet("")
        self.friendstable.setLineWidth(2)
        self.friendstable.setShowGrid(True)
        self.friendstable.setGridStyle(QtCore.Qt.DashDotLine)
        self.friendstable.setRowCount(1000)
        self.friendstable.setObjectName("friendstable")
        self.friendstable.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.friendstable.setHorizontalHeaderItem(0, item)
        self.friendstable.horizontalHeader().setDefaultSectionSize(160)
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(140, 80, 211, 121))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.searchbar = QtWidgets.QLineEdit(Dialog)
        self.searchbar.setGeometry(QtCore.QRect(160, 140, 171, 31))
        self.searchbar.setObjectName("searchbar")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 70, 571, 351))
        self.label_6.setStyleSheet("image: url(:/newPrefix/picformessageui.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.friendstable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Friends"))
        self.searchbar.setPlaceholderText(_translate("Dialog", " Search Messages"))
        self.pushButton.setText(_translate("Dialog", "Message Friends"))
import homelinkedin_rc
import homepic_rc
import logo_rc
import logolinkedin_rc
import messagepic_rc
import networkpic_rc
import picformessage_rc
import profilepic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
