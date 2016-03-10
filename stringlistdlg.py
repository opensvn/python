#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class StringListDlg(QDialog):
    def __init__(self, name, items, parent=None):
        super(StringListDlg, self).__init__(parent)

        self.__items = items

        self.addBtn = QPushButton('&Add...')
        self.editBtn = QPushButton('&Edit...')
        self.removeBtn = QPushButton('&Remove...')
        self.upBtn = QPushButton('&Up')
        self.downBtn = QPushButton('&Down')
        self.sortBtn = QPushButton('&Sort')
        self.closeBtn = QPushButton('Close')

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.addBtn)
        vlayout.addWidget(self.editBtn)
        vlayout.addWidget(self.removeBtn)
        vlayout.addWidget(self.upBtn)
        vlayout.addWidget(self.downBtn)
        vlayout.addWidget(self.sortBtn)
        vlayout.addWidget(self.closeBtn)

        self.listWidget = QListWidget()
        self.listWidget.addItems(self.__items)

        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(vlayout)

        self.connect(self.addBtn, SIGNAL('clicked()'), self.addItem)
        self.connect(self.editBtn, SIGNAL('clicked()'), self.editItem)
        self.connect(self.removeBtn, SIGNAL('clicked()'), self.removeItem)
        self.connect(self.upBtn, SIGNAL('clicked()'), self.upItem)
        self.connect(self.downBtn, SIGNAL('clicked()'), self.downItem)
        self.connect(self.sortBtn, SIGNAL('clicked()'), self.listWidget.sortItems)
        self.connect(self.closeBtn, SIGNAL('clicked()'), self, SLOT('reject()'))
        self.connect(self, SIGNAL('changed'), self.refreshList)

        self.setLayout(layout)
        self.setWindowTitle('Edit Fruit List')

    def addItem(self):
        inputDialog = QInputDialog()
        item, ret = inputDialog.getText(self, 'Add Fruit', 'Add Fruit')
        if ret:
            self.__items.append(unicode(item))
            self.emit(SIGNAL('changed'))

    def editItem(self):
        inputDialog = QInputDialog()
        item, ret = inputDialog.getText(self, 'Edit Fruit', 'Edit Fruit')

    def removeItem(self):
        pass

    def upItem(self):
        pass

    def downItem(self):
        pass

    def getList(self):
        return self.__items

    def refreshList(self):
        self.listWidget.clear()
        self.listWidget.addItems(self.__items)

    stringlist = property(getList)

if __name__ == '__main__':
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
             "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
             "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi",
             "Lemon", "Nectarine", "Plum", "Raspberry", "Strawberry",
             "Orange"]
    app = QApplication(sys.argv)
    form = StringListDlg("Fruit", fruit)
    form.exec_()
    print "\n".join([unicode(x) for x in form.stringlist]) 