# -*- coding: utf-8 -*-
"""
Spyder Editor

Convert IDL .sav file to Python .npz file

Wu 04. 04. 2019
"""

from scipy.io.idl import readsav as read_sav
import numpy 

def unpack(dictionary):
    '''unpack loaded dictionary from .sav file'''
    '''this function used in sav2npz'''
    dict_len = len(dictionary)
    keyword_str = ['']*dict_len
    value = []*dict_len
    
    # a list containing the name of variables
    keyword_str = [list(dictionary)[i] for i in range(dict_len)]
    value =  [list(dictionary.values())[i] for i in range(dict_len)]
    
    # convert numpy array into a list
    for i in range(dict_len):
        test = isinstance(value[i], numpy.ndarray)
        if test is True:
            value[i]= value[i].tolist()
    return keyword_str, value


def sav2npz(inputfile, outputfile):
    '''convert .sav to .npz'''
    # read IDL .sav file
    dictionary = read_sav(inputfile, python_dict=True, verbose=True)
    # unpack IDL .sav file
    keyword, val = unpack(dictionary)
    # create dynamic variables 
    dict_len = len(dictionary)
    for i in range(dict_len): 
        exec("%s = %s" % (keyword[i], val[i]))
    # save to the npz file with selected variables
    str_exec_save = "numpy.savez(outputfile,"    
    for i in range(dict_len):    
        str_exec_save += "%s = %s," % (keyword[i], keyword[i])
    str_exec_save += ")"
    exec(str_exec_save)


def load_sav2npz(npzfile): 
    '''load .npz file with its original names and values from sav2npz'''
    file_load = numpy.load(npzfile)
    files = file_load.files
    # loading them with their original names
    for i in range(len(files)):
        exec("%s = file_load['%s']" % (files[i], files[i]) )


