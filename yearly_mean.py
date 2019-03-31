# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:27:48 2019

Calculate yearly mean value of a time series

@author: ChiJuWu
"""
import pandas
import numpy

def yearly_mean(time, value):
    '''Calculating yearly mean value'''
    # Format of input time : floating year
    ndays = len(value)
    temp = [0]*ndays
    for i in range(ndays):
        temp[i] = (numpy.int_(time[i]), value[i])
    # convert to dataframe
    df = pandas.DataFrame(temp)
    temp = df.groupby(df[0]).mean()
    # get columns from dataframe
    yearly_time = temp.index.values
    yearly_value = temp.values.reshape(len(yearly_time))
    
    return yearly_time, yearly_value
