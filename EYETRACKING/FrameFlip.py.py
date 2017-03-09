from psychopy import core, visual

win = visual.Window([1024,768],fullscr = False, units = 'pix', waitBlanking=True) #Note the wait here!?
for i in range(500):
    
    flip_time=win.flip()
    print flip_time