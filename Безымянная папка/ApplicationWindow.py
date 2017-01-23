#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

The main Application class, which provide connect interfaces in

"""
from __future__ import print_function
from __future__ import unicode_literals

from PyQt4 import QtGui, QtCore

import sys

# import Visualization
import pyqtgraph as pg
import SerialComm
import Data

progname = 'Stirling engine'
progversion = "0.1"


# from MyMplCanvas import *


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Menu and Window
        self.main_widget = QtGui.QWidget(self)
        self.help_menu = QtGui.QMenu('&Help', self)
        self.file_menu = QtGui.QMenu('&File', self)
        self.draw_window_menu

        self.plot = pg.PlotWidget()
        self.curve = self.plot.plot()
        self.curve1 = self.plot.plot()
        self.setconf()

        # Classes
        self.__dev = SerialComm.SerialComm()
        self.__data = Data.Data()
        self.timer = QtCore.QTimer()
        # Widgets

        layout = QtGui.QGridLayout(self.main_widget)
        self.__btn_start_stop = QtGui.QPushButton('Start')
        self.text = QtGui.QLineEdit()
        self.__cb = QtGui.QComboBox()
        self.__cb.addItem(self.__dev.find_ports()[-1])

        # self.graph = Visualization.Visualization()
        #
        layout.addWidget(self.__btn_start_stop, 0, 0)  # button goes in upper-left
        # layout.addWidget(self.text, 1, 0)   # text edit goes in middle-left
        layout.addWidget(self.__cb, 1, 0)  # list widget goes in bottom-left
        layout.addWidget(self.plot, 0, 2, 5, 1)  # plot goes on right side, spanning 3 rows

        # Signals & Slots

        # self.fillCombo()

        # self.connect(self.__cb, QtCore.SIGNAL('currentIndexChanged()'), self.change_current_plot)
        self.connect(self.__btn_start_stop, QtCore.SIGNAL('clicked()'), self.clicked_start_stop)
        self.connect(self.__dev, QtCore.SIGNAL('started()'), self.on_started)
        self.connect(self.__dev, QtCore.SIGNAL('finished()'), self.on_finished)

        # Signal& slot connection for Thread which reads data from Serial port
        self.connect(self.__dev,
                     QtCore.SIGNAL('run_signal(float,float)'),
                     self.on_change, QtCore.Qt.QueuedConnection)
        self.connect(self.__dev,
                     QtCore.SIGNAL('run_signal(float,float,float)'),
                     self.on_change, QtCore.Qt.QueuedConnection)

        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.re_plot)



        self.av_timer = QtCore.QTimer(self)
        self.av_timer.timeout.connect(self.get_averege)


    def on_change(self, a, b):

        self.__data.x_data.append(a)
        self.__data.y_data.append(b)
        if len(self.__data.x_data) > 250:
            self.__data.data_overflowed()

    def clicked_start_stop(self):
        """
        Slot Function for Start/Stop button
        :return:
        """
        index = self.__cb.currentIndex()
        # if len(self.__data.get_data()) > 1:
        #     self.__btn_clear.setDisabled(False)

        if not self.__dev.is_connected:
            self.__btn_start_stop.setText("Stop")
            self.__dev.connect()
            self.__dev.start()
        else:
            self.__btn_start_stop.setText("Start")
            self.__dev.disconnect()
            self.timer.stop()

    def on_started(self):
        """
        Slot Function for starting Thread.
        :return:
        """
        self.statusBar().showMessage("Connected and Started!", 2000)

        self.timer.start(10)
        self.av_timer.start(500)
        print("Timer started")

    def on_finished(self):
        """

        :return:
        """
        self.statusBar().showMessage("Finished!", 2000)
        self.timer.stop()
        self.av_timer.stop()

    # def clicked_clear_data(self):
    #     self.__data.pop()

    def re_plot(self):
        """

        :return:
        """
        try:

            x = self.__data.get_x_data()
            y = self.__data.get_y_data()
            # x, y = self.__data.get_data()
            # if len(x) >1000
            self.curve.setData(x=x, y=y, pen=None, symbol='s')
            # self.curve1.setData(x=t, y=y, pen='g', symbol='s', symbolPen='g')
            # self.curve.setData(self.__data.x_data, self.__data.y_data)
            # self.curve1.setData(self.__data[self.index].x_data, self.__data[self.index].y_data)

            # Calculate Something

            # maxdif = max(abs(x - y))
            # print(maxdif)
        except Exception as e:
            print(e)
            return 1, e

        return 0

    def get_averege(self):
        print ("Get Averege")
        # print (self.__data.calc_averege())
        pass
    def setconf(self):
        # type: () -> None
        self.plot.setWindowTitle('pyqtgraph example: PlotSpeedTest')
        self.plot.setLabel('bottom', 'Time', units='s')
        self.plot.setLabel('left', 'Intencivity')
        self.plot.showGrid(x=True, y=True)

    def fileQuit(self):
        self.close()

    def closeEvent(self):
        self.fileQuit()

    @property
    def draw_window_menu(self):
        """
        Modifications : Build all control tools in start window
        :type self:
        """
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")
        self.setWindowIcon(QtGui.QIcon('resources/icon/icon.png'))

        self.file_menu.addAction('&Quit', self.fileQuit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu, )

        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about, QtCore.Qt.CTRL + QtCore.Qt.Key_H)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        return self

    def about(self):
        QtGui.QMessageBox.about(self, "About", """Stirling_engine
Copyright 2016 Ivan Severin, 

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.""")


if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())
    # qApp.exec_()
