#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Visualization class in  pyqtgraph 
"""

import pyqtgraph as pg

from Data import *


class Visualization:
    """docstring for Visualization"""

    def __init__(self):
               
        self.data = Data()

        self.plot = pg.PlotWidget()
        self.curve = self.plot.plot()
        self.curve1 = self.plot.plot()

        self.setConf()

    def setConf(self):
        # type: () -> None
        self.plot.setWindowTitle('pyqtgraph example: PlotSpeedTest')
        self.plot.setLabel('bottom', 'Time', units='s')
        self.plot.setLabel('left', 'Intencivity')
        self.plot.showGrid(x=True, y=True)
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(0)

    def update(self):
        t, x, y = self.data.getData()
        self.curve.setData(x=t, y=x, pen='red', name='x(t)')
        self.curve1.setData(x=t, y=y, pen='green', name='y(t)')
