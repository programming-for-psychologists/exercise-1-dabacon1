# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
square_blue.draw()
win.flip()
core.wait(1.5) 
win.flip()
core.wait(1)
i = 1
while i <=3:
    win.flip()
    square_blue.draw()
    core.wait(.3)
    win.flip()
    i = i+1
    
win.close()
sys.exit()