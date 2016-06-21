#!/usr/bin/env python
import sys
import glob
import serial


from PyQt4 import QtGui, QtCore

def serial_ports():
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

class  Data(object):
    """docstring for  Data"""
    def __init__(self):
        super( Data, self).__init__()
        import serial
        if (serial_ports() != []):
            # rewrite later !!!!
            for port in serial_ports():
                self.device_port = serial.Serial(port , 38400)
            
        
          #  print 'Cant find Arduio'
        self.t_data = []
        self.x_data = []
        self.y_data = []
        #data = x_data, y_data



    def getData(self):
        try:
            line = self.device_port.readline()
            data = [float(val) for val in line.split()]
            if (len(data) == 3):
                self.t_data.append(data[0])
                self.x_data.append(data[1])
                self.y_data.append(data[2])
                return self.t_data, self.x_data, self.y_data
    
            if (len (self.y_data) >=999.0): 
                self.t_data = []
                self.y_data = []
                self.x_data = []

        except:
            print 'No Arduio'
        return  self.x_data, self.y_data
        #print self.x_data,self.y_data 
        #print t + '\t' + x + '\t'+ y
        print data
        
    def getFakeData(self):
        arc = 0.8
        R = np.arange(0,arc*np.pi, 0.01)
        x = 1.5*np.cos(R) + 2 + 0.1*np.random.rand(len(R))
        y = np.sin(R) + 1. + 0.1*np.random.rand(len(R))
#data = Data()


#def printData():
    #global data
    #print data.getData()
    #print x + '\t'+ y
#while True:
#    printData()
