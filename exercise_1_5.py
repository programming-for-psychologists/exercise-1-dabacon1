# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win, lineColor="black",fillColor="red",size=[100,100])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
i = 1
while i <=6:  
    if (i % 2 != 0):
        square_blue.draw()
    else:
        square_red.draw()
    win.flip()
    core.wait(1)
    win.flip()
    core.wait(.5)
    i = i+1
win.close()
sys.exit()
