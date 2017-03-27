from psychopy import visual, core

# Leave this alone
win = visual.Window ([1024,768], fullscr = False, units = 'pix')   # creates a window with the resolution of 1024x768


# Put the stimulus you want to test here
my_stim =  visual.ShapeStim(win, vertices = [[-30,20],[30,40],[30,0]], lineColor = 'red', fillColor = 'firebrick')


# Change the variable name of the .draw()
my_stim.draw()

# Leave this
win.flip()
core.wait(5) 
# This causes a hang of 5 secs so your stimulus doesnt just flash up 
# and you miss it (becasue by default it flips once which is only one screen refresh (so 16.6667ms))
# so I put this in so it would remain for 5 seconds (or thereabouts)