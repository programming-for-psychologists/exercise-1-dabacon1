#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:17:12 2018

@author: DAB
"""

# 1
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square_red.draw()
win.flip()
core.wait(.5) #pause for 500 ms (half a second)
win.close()
sys.exit()

# 2
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square_red.draw()
win.flip()
core.wait(1.5) #pause for 500 ms (half a second)
win.close()
sys.exit()

#3
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square.setFillColor('red')
square.draw()
win.flip()
core.wait(1) 
square.setFillColor('blue')
square.draw()
win.flip()
core.wait(1) 
win.close()
sys.exit()

#4
#see 3

#5
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
for cur_color in ['blue','red']*3:
    square.setFillColor(cur_color)
    square.draw()
    win.flip()
    core.wait(1.0)
    win.flip()
    core.wait(.05)
win.close()
sys.exit()

#6
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
square.draw()
win.flip()
core.wait(1)
square_red.setOri(45)
square_red.draw()
win.flip()
win.close()
sys.exit()

#7
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

increment = 6 #think about why this is 6
while True:
    square.draw()
    win.flip()
    #think about why there is no core.wait() here
    square.ori += increment #alternatively: square.setOri(square.ori + increment)
  
win.close()
sys.exit()

#8
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

increment = 6 #think about why this is 6
while True:
    square.draw()
    win.flip()
    #think about why there is no core.wait() here
    square.ori += increment #alternatively: square.setOri(square.ori + increment)
    if event.getKeys(['q']):
        break

win.close()
sys.exit()

#9
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

increment = 6 #think about why this is 6
while True:
    square.draw()
    win.flip()
    #think about why there is no core.wait() here
    square.ori += increment
    if event.getKeys(['s']):
        break
win.close()
sys.exit()

#10
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

while True:
    square.draw()
    win.flip()
    if event.waitKeys(keyList=['left']):
        print 'before change', square.size
        square.size[0] =[square.size[0]+10, square.size[1]]
        print 'after change', square.size
    elif event.waitKeys(keyList=['right']):
        square.size = [square.size[0]-10, square.size[1]]

win.close()
sys.exit()

#11
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])

while True:
    square.draw()
    win.flip()
    if event.waitKeys(keyList=['left']):
        print 'before change', square.size
        square.size[0] =[square.size[0]*1.1, square.size[1]]
        print 'after change', square.size
    elif event.waitKeys(keyList=['right']):
        square.size = [square.size[0]/1.1, square.size[1]]

win.close()
sys.exit()


#12
import time
import sys
from psychopy import visual,event,core

win = visual.Window([400,400],color="black", units="pix")
left_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos[-75,0])
right_square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos[75,0])

while True:
    left_square.draw()
    right_square.draw()
    left_square.ori += 6
    right_square.ori -= 6
    win.flip()
    
win.close()
sys.exit()

#12
#something fun, could google. 