# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:38:33 2019

Find the index in an array which is closest to a number

@author: ChiJuWu
"""

import numpy

def closest(number, array, lower=None, upper=None):
    if lower == None and upper == None:
        idx = (numpy.abs(number-array)).argmin() 
    elif lower is not None:
        idx = numpy.where(array == array[array <= number].max())[0]
    elif upper is not None:
        idx = numpy.where(array == array[array >= number].min())[0]
    return idx