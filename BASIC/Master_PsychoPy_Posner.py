# -*- coding: utf-8 -*-

# PsychoPy 2 - Posner Cueing Task Example w/ Frame Timer
# Dr K McCarty
# Northumbria University
# February 2017

#Import the necessary modules from the Python storage bank
from psychopy import visual, core, data, gui, event 

#Create a dictionary called info with the following keys and values:
        # participant   -   '' (an empty string)
        # dateStr       -   data.getDateStr()

info = {}
info['participant'] = ''
info['dateStr'] = data.getDateStr() #will create str of current date/time
dlg = gui.DlgFromDict(info) #dialog box
if not dlg.OK: #did they push ok?
    core.quit()


###############----------------My Filename when saved----------------------###############

# Below, create a variable called filename that should start with "data/" and adds participant 
# code an underscore (_) and the date - use string addition for this 

filename = "data/" + info['participant'] + "_" + info['dateStr'] #This is the file name in the data/ directory


###############----------------Windows, Stimuli and Conditions File Stuff------------------------###############

# Create the following below
        # a window, call the variable win. set the resolution to 1024x768, fullscr = False
        # a fixation cross or circle, call this fixation, size 5, line and fill color white
        # a response clock, call this respClock
        # a probe, use an image stim, size 80, mask = gauss, make this whatever color you want
        # a cue, make this a shape stim. we will talk about vertices in developing the shape 


win = visual.Window((1024,768),fullscr = False, units = 'pix', waitBlanking=True, color = 'black')

fixation = visual.Circle(win, size =  5, lineColor = 'white', fillColor = 'black')

respClock = core.Clock() #create the class clock.

probe = visual.ImageStim(win, size = 80, pos = [300, 0], image = None, mask = 'raisedCos', color = 'blue') 

cue = visual.ShapeStim(win, vertices = [[-30,20],[30,40],[30,0]], lineColor = 'red', fillColor = 'firebrick')


###############-------------Trial/Experiment Handler---------------------------###############

# Create the following below:
        # conditions, using the data.importConditions function import your condition .XLS file

        # trials, initiate a trialHandler and pass the trialList argument to your conditions variable,
        #         set nReps to 5

        # posnerExp, an experiment handler, pass the extraInfo your dictionary from earlier
        #            and dataFileName to filename (your filename string)

        # finally, run the function expHander.addLoop(<your trial handler>)

conditions = data.importConditions('conditions.xlsx') #basically imports your trials and assigns them to condition 

#add trialHandler
trials = data.TrialHandler(trialList=conditions, nReps=5) #default method is randomised, trials = trial handler function thats based on conditions as the trialList

#add trials to the experiment handler to store data
posnerExp = data.ExperimentHandler(name='Posner', version='1.2',
                                   extraInfo = info,
                                   dataFileName = filename)

posnerExp.addLoop(trials) #there could be other loops (like practice loop)


###############----------------Trials-----------------------###############

# Instructions

instruct = 'Press Left if the circle appears on the left, press right if it is on the right'

instructions = visual.TextStim(win, text = instruct , color = 'white')

instructions.draw()
win.flip()
keys = event.waitKeys(keyList = ['space'])

# Start a For Loop to loop through your trial handler using the iterater name thisTrial

for thisTrial in trials: # trials is of course from the above trials (based on the data handler)

    # Set two variables resp and rt to None (dont forget the capital)
    resp=None #stops carry over
    rt=None #stops carry over

    # Set the orientation of the probe and cue, set these to whats currently in the trial handler (your iterator)
    probe.pos = [thisTrial['probeX'],0] #set the position of our probe based on the columns in trials
    cue.ori = thisTrial['cueOri'] # set the orientation of the cue (triangle. 0 positon is it facing right, 180 is flipped to left)
    print probe.pos, 'Probe'
    print cue.ori, 'Cue'

    ## Next, we want to display our fixation cross
    ## We should use a frame timer, assume your monitor is 60Hz and display for 500ms

    for frameN in range(30): #500ms
        fixation.draw()#  in Python we need to 'draw' stimuli - goes to back buffer
        win.flip() #Update the screen

    ## After fixation, we want to display our cue, again use the frame timer, 200ms this time

    for frameN in range(12): # 200ms 
        cue.draw()
        win.flip()

    ## Now for the critical bit, we want to display our probe

     # first use a function that calls a selected function when the frame flip - get it to reset the clock
    win.callOnFlip(respClock.reset) #NB: reset not reset() 

     # Now we need to clear the events buffer of any rogue key presses call event.clearEvents()
    event.clearEvents()

    # Now for the probe loop, this time we want to display the probe for 200ms but also monitor key presses
      # so, start your frame loop as usual
      # next, add in a function that checks the keyboard for presses and adds them to a list called resp (getKeys)
      # follwing this, we should check if a key was pressed, and if it was, store the resulting reaction to rt and 
      # break the loop

    for frameN in range(12):
        keys = event.getKeys(keyList = ['left','right','escape'])
        if len(keys)>0:
            resp = keys[0]
            rt=respClock.getTime()
            break
        probe.draw()
        win.flip()

    # We want the screen to go to black once a key is pressed so we should flip the buffer but not give any draw commands

    win.flip()

    # We should wait if participants have yet to make a response
    # Lets use logic to achieve this: if there isnt a response
      # Use the if to call a function that waits for a press
      # then collect the first response and assign it to resp 
      # then stop the rt timer and assign the result to rt

    if resp is None:
        keys = event.waitKeys(keyList=['left', 'right', 'escape']) 
        resp = keys[0] 
        rt=respClock.getTime()

    # To make our lives easier, we should work out if the participant was correct 
     # using what we know about the trial we should assign a variable corr with either 1 for correct or 0 for no

    if thisTrial['probeX']==300 and resp=='right': #resp is defined as the first indicie in the list keys
        corr = 1
    elif thisTrial['probeX']==-300 and resp == 'left':
        corr = 1
    elif resp=='escape':
        trials.finished = True
    else:
        corr = 0

    # We should really log some data in a file, lets use the trial handler to do this

    trials.addData('resp', resp)
    trials.addData('rt', rt)
    trials.addData('corr', corr)

    # Tell the experiment handler that this trial is now over and to begin the next trial

    posnerExp.nextEntry() #add this stuff to the file defined in the posnerExp (experiment handler)

###############-----------------Ends-----------------------###############

# Homework Challenges, 
# (better) Prizes will be provided on completion and certificates put on your student file

# It's a bit odd actually having a blank screen while you wait, it looks like a crash!
# stop this blanking from happening  

# I dont trust the psychopy data logger, write your own file of just the variables you want

# Make the timing settings for the presentation of the stimuli flexible on load using a GUI
# Dont forget to make sure its wholley divisible by the refresh rate
# Bonus: is there a way we can dynamically check what the refresh rate of the monitor is?

# When people have responded, show them their rt

# Create a new block that replicates the Friesen and Kingstone experiment you made in opensesame
# Now randomise the order of blocks on presentation (repeated measures)
