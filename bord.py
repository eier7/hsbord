#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
from yocto_api import *
from yocto_relay import *
from msvcrt import getch
from Tkinter import *

def die(msg):
    sys.exit(msg+' (check USB cable)')

# Setup the API to use local USB devices
errmsg=YRefParam()
if YAPI.RegisterHub("usb", errmsg)!= YAPI.SUCCESS:
    sys.exit("init error"+errmsg.value)

target="ANY"
if target=='ANY':
    # retreive any Relay then find its serial #
    relay = YRelay.FirstRelay()
    if relay is None : die('No module connected')
    m=relay.get_module()
    target = m.get_serialNumber()

relayone = YRelay.FindRelay(target + '.relay1')
relaytwo = YRelay.FindRelay(target + '.relay2')

if not(relayone.isOnline()):die('device not connected')
def movetable(direction, duration):
    duration = float(duration)
    if(direction == "up"):
        relayone.set_state(YRelay.STATE_B)
        time.sleep(duration)
        relayone.set_state(YRelay.STATE_A)
    elif(direction == "down"):
        relaytwo.set_state(YRelay.STATE_B)
        time.sleep(duration)
        relaytwo.set_state(YRelay.STATE_A)
        
def heltopp():
    movetable("up", 15)
def opp():
    movetable("up", 0.5)
def ned():
    movetable("down", 0.5)
def heltned():
    movetable("down", 15)
def normal():
    movetable("up", 15)
    time.sleep(1)
    movetable("down", 9.9)
#GUI
top = Tk()
top.title("Flytt Bordet")
top.wm_iconbitmap(bitmap = "table.ico")
topbutton = Button(top, text="Helt opp", command=heltopp)
topbutton.grid(row=0, column=1)
upbutton = Button(top, text="Opp", command=opp)
upbutton.grid(row=1, column=0)
downbutton = Button(top, text="Ned", command=ned)
downbutton.grid(row=1, column=2)
bottombutton = Button(top, text="Helt ned", command=heltned)
bottombutton.grid(row=2, column=1)
normalbutton = Button(top, text="Normal", command=normal)
normalbutton.grid(row=1, column=1)

top.mainloop()
