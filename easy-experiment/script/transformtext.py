# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:19:40 2016

@author: Administrator
"""
from numpy import genfromtxt, savetxt
data = genfromtxt('../data/result_datasets.csv')
savetxt('../data/result_datasets.csv',data.T)
