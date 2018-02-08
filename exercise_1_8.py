import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units="pix")
square_red = visual.Rect(win, lineColor="black",fillColor="red",size=[100,100])
square_red.draw()
win.flip()
core.wait(1)

for i in range(360):
        square_red.ori += 1
        square_red.draw()
        win.flip()
        core.wait(.0027)
event.getKeys(['s'])
win.close()
sys.exit()
