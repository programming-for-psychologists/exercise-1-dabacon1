#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win, lineColor="black",fillColor="red",size=[100,100])

square_red.size += [10,10]
square_red.draw()
win.flip()
core.wait(1)

win.close()
sys.exit()
