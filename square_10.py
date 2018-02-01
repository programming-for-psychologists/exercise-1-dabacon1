#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win, lineColor="black",fillColor="red",size=[100,100])
square_red.draw()
event.getKeys(['right', 'left'])
square_red.size += [10,10]
win.flip()
core.wait(10)
win.close()
sys.exit()
