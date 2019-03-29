# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:26:56 2019

Calculate smoothed series with given window 

@author: ChiJuWu
"""
import pandas 
import numpy

def smooth(y, window):
    n = len(y)
    y = pandas.DataFrame(y)
    y = y.rolling(window, center=True, min_periods=1).mean()
    y_smooth = y.values
    y_smooth = numpy.reshape(y_smooth, n)
    return y_smooth