# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ticketorderdlg.ui'
#
# Created: Fri Oct 30 09:34:02 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_TicketOrderDlg(object):
    def setupUi(self, TicketOrderDlg):
        TicketOrderDlg.setObjectName(_fromUtf8("TicketOrderDlg"))
        TicketOrderDlg.resize(325, 262)
        self.gridLayout_2 = QtGui.QGridLayout(TicketOrderDlg)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(TicketOrderDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.customerLineEdit = QtGui.QLineEdit(TicketOrderDlg)
        self.customerLineEdit.setObjectName(_fromUtf8("customerLineEdit"))
        self.gridLayout_2.addWidget(self.customerLineEdit, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(TicketOrderDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(TicketOrderDlg)
        self.dateTimeEdit.setMaximumDate(QtCore.QDate(2016, 10, 30))
        self.dateTimeEdit.setMinimumDate(QtCore.QDate(2015, 10, 31))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout_2.addWidget(self.dateTimeEdit, 1, 1, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(TicketOrderDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.priceSpinBox = QtGui.QDoubleSpinBox(TicketOrderDlg)
        self.priceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.priceSpinBox.setMaximum(5000.0)
        self.priceSpinBox.setObjectName(_fromUtf8("priceSpinBox"))
        self.gridLayout.addWidget(self.priceSpinBox, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(TicketOrderDlg)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.quantitySpinBox = QtGui.QSpinBox(TicketOrderDlg)
        self.quantitySpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.quantitySpinBox.setMinimum(1)
        self.quantitySpinBox.setMaximum(50)
        self.quantitySpinBox.setObjectName(_fromUtf8("quantitySpinBox"))
        self.gridLayout.addWidget(self.quantitySpinBox, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(TicketOrderDlg)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.amountLineEdit = QtGui.QLineEdit(TicketOrderDlg)
        self.amountLineEdit.setObjectName(_fromUtf8("amountLineEdit"))
        self.gridLayout.addWidget(self.amountLineEdit, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 74, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TicketOrderDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 3, 2, 1, 1)
        self.label.setBuddy(self.customerLineEdit)
        self.label_2.setBuddy(self.dateTimeEdit)
        self.label_3.setBuddy(self.priceSpinBox)
        self.label_4.setBuddy(self.quantitySpinBox)
        self.label_5.setBuddy(self.amountLineEdit)

        self.retranslateUi(TicketOrderDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TicketOrderDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TicketOrderDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(TicketOrderDlg)

    def retranslateUi(self, TicketOrderDlg):
        TicketOrderDlg.setWindowTitle(_translate("TicketOrderDlg", "Ticket Order", None))
        self.label.setText(_translate("TicketOrderDlg", "&Customer:", None))
        self.label_2.setText(_translate("TicketOrderDlg", "&When:", None))
        self.label_3.setText(_translate("TicketOrderDlg", "&Price:", None))
        self.priceSpinBox.setPrefix(_translate("TicketOrderDlg", "$ ", None))
        self.label_4.setText(_translate("TicketOrderDlg", "&Quantity:", None))
        self.label_5.setText(_translate("TicketOrderDlg", "Amount:", None))

