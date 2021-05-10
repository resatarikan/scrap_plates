# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:06:10 2021

@author: Administrator
"""

def naz_add_char(ctn,tip,ns, keyword):
    for zz in range(65,91):
       print(ctn, True, keyword + chr(zz), tip) 

def naz(ctn,tip,ns, keyword):
    if ns > 0:
        for zz in range(65,91):
            print(ctn, True, keyword + chr(zz), tip) 
            naz(ctn,tip,ns-1, keyword+chr(zz))
        for ii in range(2):
            print(ctn, True, keyword +str(ii), tip)
            naz(ctn,tip,ns-1, keyword+str(ii))
        for kk in [" ", "-"]:
            naz(ctn,tip,ns-1, keyword+kk)
            


            
naz("be", 1, 1, "")
