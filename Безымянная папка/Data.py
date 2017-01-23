from __future__ import print_function

import numpy as np


class Data(object):
    """
    docstring for  Data
    """

    def __init__(self):
        #  print 'Cant find Arduio'
        self.data_store = []

        self.x_data = []
        self.y_data = []
        self.t_data = []
        # data = x_data, y_data

    # def get_data(self):
    #     return self.x

    def calc_averege(self):
        spectrum = np.fft.fft(self.x_data)
        freq = np.fft.fftfreq(len(spectrum))
        # print (freq
        threshold = 0.5*np.max(np.abs(spectrum))
        mask= np.max(spectrum) > threshold
        peaks = (freq, np.abs(spectrum))
        return peaks

    def get_t_data(self):
        return self.t_data

    def get_x_data(self):
        return self.x_data

    def get_y_data(self):
        return self.y_data

    def set_data(self):
        pass

    def data_overflowed(self):
        self.data_store.extend([self.x_data, self.y_data])
        self.x_data = []
        self.y_data = []
