#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


import sys
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import gaugelib
import math
import myServer



if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')



win = tk.Tk()
win.attributes('-fullscreen', True)#change to win.attributes('-fullscreen', True) or to win.attributes('-zoomed', True)
#win.state('normal') #use this if running on windows
#a5 = PhotoImage(file="g1.png")
#win.tk.call('wm', 'iconphoto', win._w, a5)
win.title("Hardware Monitor Display Raspberry Pi Version 1.0")
win.geometry("1280x720+0+0")
win.resizable(width=False, height=False)
win.configure(bg='black',cursor='none')


    

    

    
    
def loop():
    
    try:
        cpu_load.set_value(myServer.cpu_load())
        cpu_temperature.set_value(myServer.cpu_temperature())  
        
        gpu_load.set_value(myServer.gpu_load())
        gpu_temperature.set_value(myServer.gpu_temperature())
        
        RAM_load.set_value(myServer.RAM_load())
        front_fan.set_value(myServer.front_fan())
        
        cpu_fan.set_value(myServer.cpu_fan())
        rear_fan.set_value(myServer.rear_fan())

        print(myServer.cpu_load())
        print(myServer.cpu_temperature())
        print(myServer.gpu_load())
        print(myServer.gpu_temperature())
        print(myServer.RAM_load())
        print(myServer.front_fan())
        print(myServer.cpu_fan())
        print(myServer.rear_fan())
    #print(myServer.cpu_data()))
    
    #print(myServer.gpu_data()))
    except:
       print("Exception error: Main.py loop()")
       
    win.after(10, loop)
    


cpu_load = gaugelib.DrawGauge4(
    win,
    max_value = 100.0,
    min_value= 0.0,
    size = 310,
    bg_col='black',
    unit = "CPU Load")
cpu_load.place(x=5,y=70)

cpu_temperature = gaugelib.DrawGauge4(
    win,
    max_value = 80.0,
    min_value= 40.0,
    size = 310,
    bg_col='black',
    unit = "CPU Temp")
cpu_temperature.place(x=320,y=70)

gpu_load = gaugelib.DrawGauge4(
    win,
    max_value = 100.0,
    min_value= 0.0,
    size = 310,
    bg_col='black',
    unit = "GPU Load")
gpu_load.place(x=635,y=70)

gpu_temperature = gaugelib.DrawGauge4(
    win,
    max_value = 80.0,
    min_value= 40.0,
    size = 310,
    bg_col='black',
    unit = "GPU Temp")
gpu_temperature.place(x=950,y=70)

RAM_load = gaugelib.DrawGauge4(
    win,
    max_value = 100.0,
    min_value= 0.0,
    size = 310,
    bg_col='black',
    unit = "RAM load")
RAM_load.place(x=5,y=420)

front_fan = gaugelib.DrawGauge4(
    win,
    max_value = 1600.0,
    min_value= 600.0,
    size = 310,
    bg_col='black',
    unit = "Front Fan")
front_fan.place(x=320,y=420)

cpu_fan = gaugelib.DrawGauge4(
    win,
    max_value = 2700.0,
    min_value= 1000.0,
    size = 310,
    bg_col='black',
    unit = "CPU Fan")
cpu_fan.place(x=635,y=420)

rear_fan = gaugelib.DrawGauge4(
    win,
    max_value = 1800.0,
    min_value= 500.0,
    size = 310,
    bg_col='black',
    unit = "Rear Fan")
rear_fan.place(x=955,y=420)


loop()







