import sys
import argparse

from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *


#import our crap
import PokerHandRanges as phr
import PokerDataTypes as  pdt

PROG_VERSION = "v0.0.2"

def printVersion(name):
    print(name + PROG_VERSION)

def printHelp(name):
    print(name + "-v | -h")
    print("-v: print version when starting the program")
    print("-h: show this message and exit()")
    exit(-1)

def minGtdOverlay(entryToPool, gtd):
    return round(gtd/entryToPool)

def calcBB(bs,sz):
    return sz / bs

def calcPotOdds(bet, pot):
    return (int((bet / (bet + bet + pot))*100))

def calcHandEquity(outs, isFlop):
    return (outs * 4) if isFlop else (outs * 2)

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("ppmh")
        lbl_ttl_bbc = QLabel("BBC Calc:", self)
        lbl_ttl_po = QLabel("PO Calc:", self)
        lbl_ttl_me = QLabel("ME Calc:", self)

        line_editSS = QLineEdit("10000", self)
        line_editBBS = QLineEdit("1000", self)
        label_bb = QLabel("10 BB", self)
        label_bb.setWordWrap(True)
        # adding action to the line edit when enter key is pressed
        line_editSS.returnPressed.connect(lambda: bbc_lbl_change())
        line_editBBS.returnPressed.connect(lambda: bbc_lbl_change())

        line_editBS = QLineEdit("50", self)
        line_editPS = QLineEdit("100", self)
        label_po = QLabel("33%", self)
        label_po.setWordWrap(True)
        # adding action to the line edit when enter key is pressed
        line_editSS.returnPressed.connect(lambda: po_lbl_change())
        line_editBS.returnPressed.connect(lambda: po_lbl_change())

        line_editGTD = QLineEdit("2000", self)
        line_editEntry = QLineEdit("100", self)
        label_to = QLabel("20", self)
        label_to.setWordWrap(True)
        # adding action to the line edit when enter key is pressed
        line_editGTD.returnPressed.connect(lambda: to_lbl_change())
        line_editEntry.returnPressed.connect(lambda: to_lbl_change())

        layout = QGridLayout()
        layout.addWidget(lbl_ttl_bbc, 0, 0)
        layout.addWidget(line_editSS, 0, 1)
        layout.addWidget(line_editBBS, 0, 2)
        layout.addWidget(label_bb, 0, 3)
        layout.addWidget(lbl_ttl_po, 1, 0)
        layout.addWidget(line_editBS, 1, 1)
        layout.addWidget(line_editPS, 1, 2)
        layout.addWidget(label_po, 1, 3)
        layout.addWidget(lbl_ttl_me, 2, 0)
        layout.addWidget(line_editGTD, 2, 1)
        layout.addWidget(line_editEntry, 2, 2)
        layout.addWidget(label_to, 2, 3)


        self.setLayout(layout)

        # method to do action
        def bbc_lbl_change():
            ss = int(line_editSS.text())
            bs = int(line_editBBS.text())
            bb = str(int(calcBB(bs,ss)))
            label_bb.setText(bb + " BB")

        def po_lbl_change():
            bs = int(line_editBS.text())
            ps = int(line_editPS.text())
            po = str(int(calcBB(bs,ss)))
            label_bb.setText(po + "%")

        def to_lbl_change():
            gtd = int(line_editGTD.text())
            entry = int(line_editEntry.text())
            needed = str(int(minGtdOverlay(entry,gtd)))
            label_to.setText(needed + " Entries")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-v":
            printVersion(sys.argv[0])
        else:
            printHelp(sys.argv[0])

    App = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(App.exec())

