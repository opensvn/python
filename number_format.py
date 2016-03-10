#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    self.format = dict(thousandsseparator=',',
        decimalmarker='.', decimalplaces=2,
        rednegatives=False)

    def setNumberFormat1(self):
        dialog = numberformatdlg1.NumberFormatDlg(self.format, self)
        if dialog.exec_():
            self.format = dialog.numberFormat()
            self.refreshTable()
