# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1050, 697)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.filterButton = QtGui.QPushButton(self.centralwidget)
        self.filterButton.setGeometry(QtCore.QRect(790, 20, 71, 27))
        self.filterButton.setObjectName(_fromUtf8("filterButton"))
        self.filterText = QtGui.QLineEdit(self.centralwidget)
        self.filterText.setGeometry(QtCore.QRect(30, 20, 641, 27))
        self.filterText.setObjectName(_fromUtf8("filterText"))
        self.filter_table = QtGui.QTableWidget(self.centralwidget)
        self.filter_table.setGeometry(QtCore.QRect(30, 60, 911, 241))
        self.filter_table.setObjectName(_fromUtf8("filter_table"))
        self.filter_table.setColumnCount(6)
        self.filter_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.filter_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.filter_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.filter_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.filter_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.filter_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.filter_table.setHorizontalHeaderItem(5, item)
        self.filter_table.horizontalHeader().setDefaultSectionSize(150)
        self.detail_widget = QtGui.QListWidget(self.centralwidget)
        self.detail_widget.setGeometry(QtCore.QRect(30, 310, 911, 170))
        self.detail_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.detail_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.detail_widget.setObjectName(_fromUtf8("detail_widget"))
        self.interface_2 = QtGui.QComboBox(self.centralwidget)
        self.interface_2.setGeometry(QtCore.QRect(690, 20, 85, 27))
        self.interface_2.setObjectName(_fromUtf8("interface_2"))
        self.hexdump_list = QtGui.QListWidget(self.centralwidget)
        self.hexdump_list.setGeometry(QtCore.QRect(30, 490, 911, 121))
        self.hexdump_list.setObjectName(_fromUtf8("hexdump_list"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 620, 68, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.running_info = QtGui.QLabel(self.centralwidget)
        self.running_info.setGeometry(QtCore.QRect(90, 620, 841, 17))
        self.running_info.setText(_fromUtf8(""))
        self.running_info.setObjectName(_fromUtf8("running_info"))
        self.haltButton = QtGui.QPushButton(self.centralwidget)
        self.haltButton.setGeometry(QtCore.QRect(870, 20, 71, 27))
        self.haltButton.setObjectName(_fromUtf8("haltButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.filterButton.setText(_translate("MainWindow", "filter", None))
        self.filter_table.setSortingEnabled(True)
        item = self.filter_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.filter_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source", None))
        item = self.filter_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination", None))
        item = self.filter_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protocol", None))
        item = self.filter_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Length", None))
        item = self.filter_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Info", None))
        self.label.setText(_translate("MainWindow", "Status:", None))
        self.haltButton.setText(_translate("MainWindow", "Halt", None))
