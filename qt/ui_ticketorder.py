# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticketorder.ui'
#
# Created: Fri Aug 21 15:26:51 2015
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

class Ui_TicketOrder(object):
    def setupUi(self, TicketOrder):
        TicketOrder.setObjectName(_fromUtf8("TicketOrder"))
        TicketOrder.resize(400, 209)
        self.verticalLayout_3 = QtGui.QVBoxLayout(TicketOrder)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(TicketOrder)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.customerLineEdit = QtGui.QLineEdit(TicketOrder)
        self.customerLineEdit.setObjectName(_fromUtf8("customerLineEdit"))
        self.horizontalLayout.addWidget(self.customerLineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(TicketOrder)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.dateTimeEdit = QtGui.QDateTimeEdit(TicketOrder)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 8, 22), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setMaximumDate(QtCore.QDate(2016, 8, 21))
        self.dateTimeEdit.setMinimumDate(QtCore.QDate(2015, 8, 22))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout.addWidget(self.dateTimeEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(TicketOrder)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.priceSpinBox = QtGui.QDoubleSpinBox(TicketOrder)
        self.priceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.priceSpinBox.setMaximum(5000.0)
        self.priceSpinBox.setObjectName(_fromUtf8("priceSpinBox"))
        self.gridLayout.addWidget(self.priceSpinBox, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(TicketOrder)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.quantitySpinBox = QtGui.QSpinBox(TicketOrder)
        self.quantitySpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.quantitySpinBox.setMaximum(50)
        self.quantitySpinBox.setObjectName(_fromUtf8("quantitySpinBox"))
        self.gridLayout.addWidget(self.quantitySpinBox, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(TicketOrder)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.amountLineEdit = QtGui.QLineEdit(TicketOrder)
        self.amountLineEdit.setObjectName(_fromUtf8("amountLineEdit"))
        self.gridLayout.addWidget(self.amountLineEdit, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(TicketOrder)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label.setBuddy(self.customerLineEdit)
        self.label_2.setBuddy(self.dateTimeEdit)
        self.label_3.setBuddy(self.priceSpinBox)
        self.label_4.setBuddy(self.quantitySpinBox)
        self.label_5.setBuddy(self.amountLineEdit)

        self.retranslateUi(TicketOrder)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TicketOrder.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TicketOrder.reject)
        QtCore.QMetaObject.connectSlotsByName(TicketOrder)
        TicketOrder.setTabOrder(self.customerLineEdit, self.dateTimeEdit)
        TicketOrder.setTabOrder(self.dateTimeEdit, self.priceSpinBox)
        TicketOrder.setTabOrder(self.priceSpinBox, self.quantitySpinBox)
        TicketOrder.setTabOrder(self.quantitySpinBox, self.buttonBox)
        TicketOrder.setTabOrder(self.buttonBox, self.amountLineEdit)

    def retranslateUi(self, TicketOrder):
        TicketOrder.setWindowTitle(_translate("TicketOrder", "Ticket Order", None))
        self.label.setText(_translate("TicketOrder", "Customer:", None))
        self.label_2.setText(_translate("TicketOrder", "When:", None))
        self.dateTimeEdit.setDisplayFormat(_translate("TicketOrder", "M/d/yy hh:mm ", None))
        self.label_3.setText(_translate("TicketOrder", "Price:", None))
        self.priceSpinBox.setPrefix(_translate("TicketOrder", "$ ", None))
        self.label_4.setText(_translate("TicketOrder", "Quantity:", None))
        self.label_5.setText(_translate("TicketOrder", "Amount:", None))

