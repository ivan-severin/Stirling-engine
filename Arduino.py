#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

"""



"""

import serial


def findPorts():
    import sys
    import glob
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class Arduino():
    def __init__(self, Port='/dev/ttyUSB0', Boud=9600, connState=0):
        # type: (self, basestring, int) -> None
        """

        :rtype: object
        """
        self.parent = self
        self.port = Port
        self.boud = Boud
        self.connState = connState
        self.timeount = 1
        self.ser = None
        self.connect()

    def connect(self):
        # noinspection PyBroadException
        try:
            self.ser = serial.Serial(self.port, self.boud, timeout=0.0001)
            # self.ser.open()
            self.connState = 1
            print("Successfully connected to port %r." % self.port)
            return [1, 'connected']
        except:
            self.connState = 0
            print('no hardware found')
            return [0, 'no hardware found']

    def disconnect(self):
        if self.connState == 1:
            self.ser.close()

    def isConnected(self):
        # Is the computer connected with the Serial Port?
        try:
            return self.connState
        except:
            return False

    def loadData(self):
        buffer = self.ser.readline()
        if buffer != '':
            try:
                print(buffer)
            except Exception as e:
                pass

    def sendData(self, command):
        try:
            self.ser.write(command)
        except Exception as e:
            print('Error sending message "%s" to Arduino:\n%s' % (command, e))



            # ard=Arduino(Boud=38400)
            # while True:
            #    if ard.connState:
            #        ard.loadData()
            #    else:
            #        print "Arduino not found"
            #       break
