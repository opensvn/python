#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_ticketorder

class TicketOrderDlg(QDialog, ui_ticketorder.Ui_TicketOrder):
    def __init__(self, parent=None):
        super(TicketOrderDlg, self).__init__(parent)
        self.setupUi(self)
        self.updateUi()
        self.__amount = 0.00

    def updateUi(self):
        enable = not self.customerLineEdit.text().isEmpty()
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)

    @pyqtSignature("QString")
    def on_customerLineEdit_textEdited(self, text):
        self.updateUi()

    @pyqtSignature('double')
    def on_priceSpinBox_valueChanged(self, value):
        self.calc()

    def calc(self):
        self.__amount = self.priceSpinBox.value() * self.quantitySpinBox.value()
        self.amountLineEdit.setText(self.__amount)

def main():
    from sys import argv
    app = QApplication(argv)
    form = TicketOrderDlg()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()