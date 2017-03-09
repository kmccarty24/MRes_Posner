# -*- coding: utf-8 -*-

# PsychoPy 2 - Posner Cueing Task Example w/ Frame Timer
# Dr K McCarty
# Northumbria University
# February 2017

#Import the necessary modules from the Python storage bank

#Create a dictionary called info with the following keys and values:
        # participant   -   '' (an empty string)
        # fixFrames     -   30
        # cueFrames     -   12
        # probeFrames   -   12
        # dateStr       -   data.getDateStr()

info = {}
info['participant'] = ''
info['fixFrames'] = 30 #frames
info['cueFrames'] = 12 #frames
info['probeFrames'] = 12 #frames
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


win = visual.Window([1024,768],fullscr = False, units = 'pix', waitBlanking=True)

fixation = visual.Circle(win, size =  5, lineColor = 'white', fillColor = 'black')

respClock = core.Clock() #create the class clock.

probe = visual.ImageStim(win, size = 80, pos = [300, 0], image = None, mask = 'gauss', color = 'blue') 

cue = visual.ShapeStim(win, vertices = [[-30,-20],[-30,20],[30,0]], lineColor = 'red', fillColor = 'firebrick')


###############-------------Trial/Experiment Handler---------------------------###############

# Create the following below
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
posnerExp = data.ExperimentHandler(
        name='Posner', version='1.2', #not needed, just handy
        extraInfo = info, #the info we created earlier
        dataFileName = filename, # using our string with data/name_date
        )
posnerExp.addLoop(trials) #there could be other loops (like practice loop)


###############----------------Trials-----------------------###############

# Instructions

# Start a For Loop to loop through your trial handler using the iterater name thisTrial

    # Set two variables resp and rt to None (dont forget the capital)
    # Set the orientation of the probe and cue, set these to whats currently in the trial handler (your iterator)

    ## Next, we want to display our fixation cross
    ## We should use a frame timer, assume your monitor is 60Hz and display for 500ms

    ## After fixation, we want to display our cue, again use the grame timer, 200ms this time

    ## Next up, present the cue 

    ## Now for the critical bit, we want to display our probe



for thisTrial in trials: # trials is of course from the above trials (based on the data handler
    #Set Trails up based on our conditions
    resp=None #stops carry over
    rt=None #stops carry over
    probe.setPos([thisTrial['probeX'],0]) #set the position of our probe based on the columns in trials
    cue.setOri(thisTrial['cueOri']) # set the orientation of the cue (triangle. 0 positon is it facing right, 180 is flipped to left)
    
    
    #Present fixation cross
    for frameN in range(30): #500ms
        fixation.draw()#  in Python we need to 'draw' stimuli - goes to back buffer
        win.flip() #Update the screen

    #Present cue 
    for frameN in range(12): # 200ms 
        cue.draw()
        win.flip()

    #Present probe
    win.callOnFlip(respClock.reset) #NB: reset not reset() 
    event.clearEvents()
    for frameN in range(12):
        keys = event.getKeys(keyList = ['left','right','escape'])
        if len(keys)>0:
            resp = keys[0]
            rt=respClock.getTime()
            break #out of the checking loop
        probe.draw()
        win.flip()
    win.flip() #so after the last frame it flips again to nothing


    #check for responses but only if one hasnt been made
    if resp is None:
        keys = event.waitKeys(keyList=['left', 'right', 'escape']) 
        resp = keys[0] #take the first response as its an indicie in a list its the first that was logged in zero
        rt=respClock.getTime() #collects the time from the clock
        #wait keys will clear the previous ones and wait until allowed key  is pressed
    
    
    #now is it right??
    if thisTrial['probeX']==300 and resp=='right': #resp is defined as the first indicie in the list keys
        corr = 1
    elif thisTrial['probeX']==-300 and resp == 'left':
        corr = 1
    elif resp=='escape':
        trials.finished = True
    else:
        corr = 0

    trials.addData('resp', resp)
    trials.addData('rt', rt)
    trials.addData('corr', corr)

    posnerExp.nextEntry() #add this stuff to the file defined in the posnerExp (experiment handler)

###############-----------------Ends-----------------------###############
