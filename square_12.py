#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win, lineColor="black",fillColor="red",size=[-50,100])
square_blue = visual.Rect(win,lineColor="black",fillColor="blue",size=[50,100])

for i in range(360):
        square_red.ori += 1
        square_red.draw()
        win.flip()
        core.wait(.0027)
        square_blue.ori += 1
        square_blue.draw()
        win.flip()
        core.wait(.0027)

win.close()
sys.exit()


