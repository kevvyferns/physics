#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:24:46 2018

@author: kevinfernandes
"""

import numpy as np
import matplotlib.pyplot as plt
import json as js
import time as tm
import datetime as dtm
import os as os
import sys as ss

"""- - - - - - - File related and IO functions - - - - - - -"""
def check_Dir(name, __path__):
    try:
        if not os.path.exists(__path__ + name):
            make_Dir(0, __path__, name)
            print ('File: {} created...'.format(name))
        else:
            print ('File: {} already exists...\nMoving on...'.format(name))
    except:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        pass
    return __path__ + name + '/'
    
def make_Dir(val, _path_, _name__):
    try:
        os.makedirs(_path_ + _name__)
    except:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        pass
    
def open_from_JSON(_path_, fname):
    try:
        with open(_path_ + fname) as f_:
            Data = js.load(f_)
    except:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        pass
    return Data

def save_to_JSON(filename, Data):
    try:
        with open(filename, 'w') as f:
            js.dump(Data, f, indent = 4, sort_keys = True)
        print ('Data saved in:\n\t{}'.format(filename))
    except:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        pass
    
"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""

"""- - - - - - - - Data management functions - - - - - - - -"""
def make_Stats(inList):
    try:
        List = np.array(inList)
        ave = np.average(List)
        std = np.std(List)
        mx = max(List)
        mn = min(List)
        out = {'Average' : ave, 'S.Dev' : std, 'Maximum' : mx, 'Minimum' : mn, 'Absolute Range' : np.ptp(List)}
    except:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        pass
    return out

"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""

"""- - - - - - - - Plotting related functions  - - - - - - -"""
def make_Fig(name, size = [12.5, 10]):
    try:
        # TODO: write function here
        print ('Nothing to see here...')
    except:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        pass
            
"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""

"""- - - - - - - - - - - - - Main  - - - - - - - - - - - - -"""
if __name__ == '__main__':
    pass