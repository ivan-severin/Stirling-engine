#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

"""

The main Application class, which provide connect inerfaces in 

"""

from __future__ import unicode_literals

progname = 'Stirling engine'
progversion = "0.1"
# from MyMplCanvas import *
from Visualization import *
from Arduino import *


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Menu and Window

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtGui.QWidget(self)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        # Widgets

        layout = QtGui.QGridLayout(self.main_widget)
        self.btn = QtGui.QPushButton('Start')
        self.text = QtGui.QLineEdit()
        self.combo = QtGui.QComboBox()
        self.graph = Visualization()

        layout.addWidget(self.btn, 0, 0)  # button goes in upper-left
        # layout.addWidget(self.text, 1, 0)   # text edit goes in middle-left
        layout.addWidget(self.combo, 1, 0)  # list widget goes in bottom-left
        layout.addWidget(self.graph.plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows

        # Signals & Slots


        listports = findPorts()
        for item in listports:
            self.combo.addItem(item)

        self.combo.currentIndexChanged.connect(lambda: self.combo.currentText())
        if listports:
            print (str(self.combo.currentText()))
            self.device = Arduino(Port=str(self.combo.currentText()), Boud=38400)
            self.device.connect()
            # if self.device.isConnected():
            self.statusBar().showMessage("Successfully connected to port %r." % self.device.port, 5000)
        else:
            self.device = Arduino()
            self.combo.addItem('No hardware')
            self.statusBar().showMessage("no hardware found", 5000)

        self.btn.clicked.connect(self.startReading)

    def startReading(self):
        if self.device.isConnected():
            self.device.sendData('r')
            # next wtrite this better !
            print(self.device.loadData())

    def stopReading(self):
        if self.device.isConnected():
            self.device.sendData('s')
            # next wtrite this better !
            print (self.device.loadData())

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QtGui.QMessageBox.about(self, "About",
                                """Stirling_engine
Copyright 2016 Ivan Severin, 

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
                                )


qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
# qApp.exec_()
