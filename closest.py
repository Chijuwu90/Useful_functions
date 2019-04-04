# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:38:33 2019

Find the index in an array which is closest to a number

@author: ChiJuWu
"""

import numpy

def closest(number, array, lower=False, upper=False):
    if lower:
        idx = numpy.where(array == array[array <= number].max())[0]
    elif upper:
        idx = numpy.where(array == array[array >= number].min())[0]
    else:
        idx = (numpy.abs(number-array)).argmin() 
    return idx
