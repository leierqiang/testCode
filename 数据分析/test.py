# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 20:07:23 2019

@author: Leq
"""
from pandas import Series
#
s = Series(['a', True, 1], index=['first', 'secont', 'third'])

print(s[1])
