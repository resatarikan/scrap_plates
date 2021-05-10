# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 20:52:34 2021

@author: Administrator
"""
import os



temp_path = "/mnt/disks/disk2/images/"



def countfiles(pathim):    
    for fol in os.listdir(pathim):
        try:
            print (fol,":", len(os.listdir(pathim+"/"+fol+"/")) )
        except:
            print(fol, "hata")


countfiles(temp_path)

