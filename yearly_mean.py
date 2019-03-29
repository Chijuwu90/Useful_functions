# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:27:48 2019

Calculate yearly mean value of a time series

@author: ChiJuWu
"""
import pandas
import numpy

def yearly_mean(time,value):
    # Format of input time : floating year
    ndays = len(value)
    temp = [0]*ndays
    for i in range(ndays):
        temp[i] = (numpy.int_(time[i]), value[i])
    # convert to dataframe   
    df = pandas.DataFrame(temp)   
    temp = df.groupby(df[0]).mean()
    # get columns from dataframe
    x = temp.index.values
    y = temp.values.reshape(len(x))
    return x, y