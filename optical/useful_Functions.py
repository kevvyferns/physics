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
    except Exception as ckDirExec:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        print (ckDirExec)
        pass
    return __path__ + name + '/'
    
def make_Dir(val, _path_, _name__):
    try:
        os.makedirs(_path_ + _name__)
    except Exception as mkDirExec:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        print (mkDirExec)
        pass
    
def open_from_JSON(_path_, fname):
    try:
        with open(_path_ + fname) as f_:
            Data = js.load(f_)
    except Exception as opnJsnExec:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        print (opnJsnExec)
        pass
    return Data

def save_to_JSON(filename, Data):
    try:
        with open(filename, 'w') as f:
            js.dump(Data, f, indent = 4, sort_keys = True)
        print ('Data saved in:\n\t{}'.format(filename))
    except Exception as savJsnExec:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        print (savJsnExec)
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
    except Exception as statExc:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        print (statExc)
        pass
    return out

"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""

"""- - - - - - - - Plotting related functions  - - - - - - -"""
def make_Fig(name, size = [12.5, 10]):
    try:
        # TODO: write function here
        print ('Nothing to see here...')
    except Exception as figExec:
        print ('Error in "{}" function'.format(ss._getframe().f_code.co_name))
        print (figExec)
        pass
            
"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""

"""- - - - - - - - - - - - - Main  - - - - - - - - - - - - -"""
if __name__ == '__main__':
    pass