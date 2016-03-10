#!/usr/bin/evn python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_ticketorderdlg

class TicketOrderDlg(QDialog,
    ui_ticketorderdlg.Ui_TicketOrderDlg):
    def __init__(self, parent=None):
        super(TicketOrderDlg, self).__init__(parent)
        self.setupUi(self)
        self.updateUi()
        self.quantity = self.quantitySpinBox.value()
        self.price = self.priceSpinBox.value()
        self.datetime = self.dateTimeEdit.dateTime().toPyDateTime()

    def result(self):
        return self.customer, self.datetime, self.price, self.quantity

    def updateUi(self):
        enable = not self.customerLineEdit.text().isEmpty()
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)

    @pyqtSignature('QString')
    def on_customerLineEdit_textEdited(self):
        self.customer = unicode(self.customerLineEdit.text())
        self.updateUi()

    @pyqtSignature('int')
    def on_quantitySpinBox_valueChanged(self):
        self.quantity = self.quantitySpinBox.value()
        self.amount = self.quantity * self.price
        self.amountLineEdit.setText(str(self.amount))

    @pyqtSignature('double')
    def on_priceSpinBox_valueChanged(self):
        self.price = self.priceSpinBox.value()
        self.amount = self.quantity * self.price
        self.amountLineEdit.setText(str(self.amount))

def main():
    import sys
    app = QApplication(sys.argv)
    form = TicketOrderDlg()
    form.show()
    app.exec_()
    print form.result()

if __name__ == '__main__':
    main()