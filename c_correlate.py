# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:22:54 2019

Calculate cross correlation with lags

@author: ChiJuWu
"""

def c_correlate(x, y, lag):
    nx = len(x)
    nlag = len(lag)    

    Xd = x - sum(x)/nx
    Yd = y - sum(y)/nx
    
    cross = [0]*nlag
    
    for k in range(nlag):
        if lag[k] >= 0:
            cross[k] = sum(Xd[0 : nx-lag[k]] * Yd[lag[k]:])
        else:
            cross[k] = sum(Yd[0 : nx+lag[k]] * Xd[-lag[k]:])

    cross = cross/(sum(Xd**2)*sum(Yd**2))**(1/2)
    return cross