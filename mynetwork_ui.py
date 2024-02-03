# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mynetwork.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1109, 575)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(-90, -90, 1361, 151))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, -5, 101, 71))
        self.label.setStyleSheet("image: url(:/newPrefix/homelinkedin.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 0, 71, 61))
        self.label_2.setStyleSheet("image: url(:/newPrefix/homepic.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(510, 0, 91, 61))
        self.label_3.setStyleSheet("image: url(:/newPrefix/networkpic.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(680, 0, 91, 61))
        self.label_4.setStyleSheet("image: url(:/newPrefix/messagepic.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(860, 0, 81, 61))
        self.label_5.setStyleSheet("image: url(:/newPrefix/profilepic.jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(210, 130, 661, 141))
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(210, 90, 661, 41))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(390, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_6.setObjectName("label_6")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_3.setGeometry(QtCore.QRect(210, 290, 661, 41))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(360, 290, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_7.setObjectName("label_7")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(210, 330, 661, 141))
        self.tableWidget_2.setRowCount(1000)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(303)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Pending Invitations"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Accept"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Ignore"))
        self.label_6.setText(_translate("Dialog", "                  Invitations"))
        self.label_7.setText(_translate("Dialog", "            Connect With People"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "People You May Know"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Connect"))
import homelinkedin_rc
import homepage_rc
import messagepic_rc
import networkpic_rc
import profilepic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
