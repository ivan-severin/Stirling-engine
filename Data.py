#!/usr/bin/env python
import sys
import glob
import serial

from PyQt4 import QtGui, QtCore

from Arduino import *


class Data(object):
    # docstring for  Data

    def __init__(self):
        super(Data, self).__init__()

        self.ard = Arduino(Port='/dev/ttyUSB0', Boud=38400, connState=1)
        # self.ard.connect()
        #  print 'Cant find Arduino'
        self.t_data = []
        self.x_data = []
        self.y_data = []
        # data = x_data, y_data

    @property
    def getData(self):
        line = self.ard.loadData()
        data = [float(val) for val in line.split()]
        if len(data) == 3:
            self.t_data.append(data[0])
            self.x_data.append(data[1])
            self.y_data.append(data[2])
            return self.t_data, self.x_data, self.y_data
        if len(self.y_data) >= 999.0:
            self.t_data = []
            self.y_data = []
            self.x_data = []
        print data

        #    print 'No Arduio'
        return self.x_data, self.y_data
        # print self.x_data,self.y_data
        # print t + '\t' + x + '\t'+ y

    def getFakeData(self):
        arc = 0.8
        R = np.arange(0, arc * np.pi, 0.01)
        x = 1.5 * np.cos(R) + 2 + 0.1 * np.random.rand(len(R))
        y = np.sin(R) + 1. + 0.1 * np.random.rand(len(R))


data = Data()


# def printData():
#   global data
#  data.ard.sendData('r')
# print data.getData()
# print x + '\t'+ y`
# while True:
#    printData()
