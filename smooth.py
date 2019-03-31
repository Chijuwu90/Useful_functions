# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:26:56 2019

Calculate smoothed series with given window 

@author: ChiJuWu
"""
import pandas 
import numpy

def smooth(data, window):
    '''Return the smoothed data with given window box'''
    n = len(data)
    data = pandas.DataFrame(data)
    data = data.rolling(window, center=True, min_periods=1).mean()
    data_smooth = data.values
    data_smooth = numpy.reshape(data_smooth, n)
    
    return data_smooth
