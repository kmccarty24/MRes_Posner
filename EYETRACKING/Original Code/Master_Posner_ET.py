from psychopy import visual, event, core, data, gui 
from psychopy.iohub import (launchHubServer, EventConstants, EyeTrackerConstants, module_directory, 
                            getCurrentDateTimeString, ioHubExperimentRuntime)

info = {}
info['participant'] = '0'
info['fixFrames'] = 60 #frames
info['cueFrames'] = 12 #frames
info['probeFrames'] = 12 #frames
info['See Eyes?'] = ['Yes', "No"]
info['dateStr'] = data.getDateStr() #will create str of current date/time
dlg = gui.DlgFromDict(info) #dialog box
if not dlg.OK: #did they push ok?
    core.quit()


io = launchHubServer(iohub_config_name = 'iohub_config.yaml', experiment_code = info['particicpant'])


filename = "data/" + info['participant'] + "_" + info['dateStr'] #This is the file name in the data/ directory


#add trials to the experiment handler to store data
posnerExp = data.ExperimentHandler(
        name='Posner', version='1.5', #not needed, just handy
        extraInfo = info, #the info we created earlier
        dataFileName = filename, # using our string with data/name_date
        )

exp_conditions=data.importConditions('conditions.xlsx')
trials = data.TrialHandler(exp_conditions,1)

posnerExp.addLoop(trials) #there could be other loops (like practice loop)

# Inform the ioDataStore that the experiment is using a
# TrialHandler. The ioDataStore will create a table 
# which can be used to record the actual trial variable values (DV or IV)
# in the order run / collected.

io.createTrialHandlerRecordTable(trials) 
                         
# selected_eyetracker_name=args[0]
# Let's make some short-cuts to the devices we will be using in this experiment.
try:
    tracker=io.devices.tracker
except Exception:
    # No eye tracker config found in iohub_config.yaml
    from psychopy.iohub.util import MessageDialog
    md = MessageDialog(title="No Eye Tracker Configuration Found",
                       msg="Update the iohub_config.yaml file by "
                       "uncommenting\nthe appropriate eye tracker "
                       "config lines.\n\nPress OK to exit demo.",
                       showButtons=MessageDialog.OK_BUTTON,
                       dialogType=MessageDialog.ERROR_DIALOG,
                       allowCancel=False,
                       display_index=0)
    md.show()

display=io.devices.display
kb=io.devices.keyboard
mouse=io.devices.mouse            
            
# Start by running the eye tracker default setup procedure.
tracker.runSetupProcedure()

# Create a psychopy window, full screen resolution, full screen mode...
#
res=display.getPixelResolution()
win=visual.Window(res,monitor=display.getPsychopyMonitorName(),
                            units=display.getCoordinateType(),
                            fullscr=True,
                            allowGUI=False,
                            screen= display.getIndex() # default 0, if ,multi then any upto N-1
                            )

# Set the mouse visibility to False 
mouse.setSystemCursorVisibility(False)


#Configure Display Elements 

display_coord_type=display.getCoordinateType()

fixation = visual.Circle(win, size =  5, lineColor = 'white', fillColor = 'black')

respClock = core.Clock() #create the class clock.

probe = visual.ImageStim(win, size = 80, pos = [300, 0], image = None, mask = 'gauss', color = 'blue') 

cue = visual.ShapeStim(win, vertices = [[-30,-20],[-30,20],[30,0]], lineColor = 'red', fillColor = 'firebrick')

gaze_dot =visual.GratingStim(win,tex=None, mask="gauss", 
                             pos=(0,0 ),size=(66,66),color='green', 
                             units=display_coord_type)

instr = 'Press Enter or arrow keys nobber'
instruct = visual.TextStim(win, text = instr)


## -- ## Begin Experiment ##--##

# Draw Instructions / Inform ioHub Experiment Starting

instruct.draw()
flip_time=win.flip() # logs time between refreshes consecutivly from onset
io.sendMessageEvent(text="EXPERIMENT_START",sec_time=flip_time)

io.clearEvents('all') # to clear the buffer of events such as key presses etc
kb.waitForPresses(keys=' ') # similar to psychopys waitKeys func

# Send some information to the ioDataStore as experiment messages,
# including the experiment and session id's, the calculated pixels per
# degree, display resolution, etc.

io.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO START") 
io.sendMessageEvent(text="ioHub Experiment started {0}".format(getCurrentDateTimeString()))
io.sendMessageEvent(text="Experiment ID: {0}, Session ID: {1}".format(io.experimentID,io.experimentSessionID))
io.sendMessageEvent(text="Stimulus Screen ID: {0}, Size (pixels): {1}, CoordType: {2}".format(display.getIndex(),display.getPixelResolution(),display.getCoordinateType()))
io.sendMessageEvent(text="Calculated Pixels Per Degree: {0} x, {1} y".format(*display.getPixelsPerDegree()))        
io.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO END")

io.clearEvents('all')


## -- ## Start Trial Sequence ##--##

t=0
for trialN in trials:
    resp=None #stops carry over
    rt=None #stops carry over
    probe.setPos([trialN['probeX'],0])
    cue.setOri(trialN['cueOri'])
    
    print trialN #prints the dictionary order its using

    io.sendMessageEvent(text="TRIAL%i_START" %(t),sec_time=flip_time)

    flip_time=win.flip() #So go to blank (in case there was something on the screen)

    trialN['session_id']=io.getSessionID() # Remember Kris, a trialN in trials 
    trialN['trial_id']=t+1                       # is merely a dictionary, hence you 
    trialN['TRIAL_START']=flip_time              # can add stuff to it

    #io.sendMessageEvent(text="TRIAL_START",sec_time=flip_time)
    io.clearEvents('all')
    
    # Turn the tracker on!
    tracker.setRecordingState(True)

   
        
    gpos = tracker.getLastGazePosition()
    

    # Draw Fixation Cross and log time in the datastore
    for frameN in range(info['fixFrames']):
        fixation.draw()#  in Python we need to 'draw' stimuli - goes to back buffer
        
        # If we have a gaze position from the tracker,
        # redraw the background image and then the
        # gaze_cursor at the current eye position.
        gpos = tracker.getLastGazePosition()
        if type(gpos) in [tuple,list]:
            gaze_dot.setPos([gpos[0], gpos[1]])
            gaze_dot.draw()
        
        if frameN == 0:
            flips = win.flip()
            io.sendMessageEvent("Fix_Onset TrialNo %i" %(t),sec_time=flips)
        else:
            win.flip() #Update the screen

    # Change Screen to Black and Hopefully their gaze should be in the centre
    flips = win.flip() # to black, gets rid of fix and logs time in flips

    # and log it with the latest gase position
    gpos = tracker.getLastGazePosition()

    io.sendMessageEvent("Fix_Offset TrialNo %i %.3f %.3f" %(t, gpos[0],gpos[1]),sec_time=flips)

    # Draw Cue and log it in the datastore 

    for frameN in range(info['cueFrames']):
        cue.draw()

        gpos = tracker.getLastGazePosition()
        if type(gpos) in [tuple,list]:
            gaze_dot.setPos([gpos[0], gpos[1]])
            gaze_dot.draw()

        if frameN == 0:
            flips = win.flip()
            io.sendMessageEvent("Cue_Onset TrialNo %i" %(t),sec_time=flips)
        elif frameN != 0 and frameN < (info['cueFrames']-1):
            win.flip()
        elif frameN == (info['cueFrames']-1):
            flips = win.flip()
            io.sendMessageEvent("Cue_Offset TrialNo %i %.3f %.3f" %(t, gpos[0],gpos[1]),sec_time=flips)
            #not happy with this as its technically not off the screen yet


    # Present probe

    win.callOnFlip(respClock.reset) #NB: reset not reset() as the callOnFlip function doesnt need extra () 
    io.clearEvents('all')
    
    iteration = 0

    keys = []
    
    while len(keys) == 0:

        gpos = tracker.getLastGazePosition()
        if type(gpos) in [tuple,list]:
            gaze_dot.setPos([gpos[0], gpos[1]])
            gaze_dot.draw()

        probe.draw()

        if iteration == 0:
            flips = win.flip()
            io.sendMessageEvent("Probe_Onset TrialNo %i %.3f %.3f" %(t, gpos[0],gpos[1]),sec_time=flips)
        else:
            win.flip()

        keys = kb.getKeys(keys = ['m','z','ESCAPE'])

        if len(keys) < 1:
            kb.clearEvents()
            iteration +=1
        elif 'm' in keys and trialN['probeX']== 300:
            rt = respClock.getTime()
            corr = 1
            print 'correct'
            break
        elif 'z' in keys and trialN['probeX']== -300:
            rt = respClock.getTime()
            corr = 1
            print 'correct'
            break
        elif 'ESCAPE' in keys:
            rt = respClock.getTime()
            trials.finished = True
            corr = 'Pressed Escape'
            core.quit()
            win.close()
        else:
            rt = respClock.getTime()
            print 'incorrect'
            corr = 0
            break

    trials.addData('rt', rt)
    trials.addData('key', keys[0])
    trials.addData('Correct?', corr)

    # So the trial has ended, send a message to the DataStore
    # with the trial end time and stop recording eye data.

    # Save the Experiment Condition Variable Data for this trial to the
    # ioDataStore.
    flips = win.flip()
    trialN['TRIAL_END']=flips
    io.sendMessageEvent(text = "TRIAL_END %d" %t,sec_time=flips)
    io.addRowToConditionVariableTable(trialN.values())
    io.clearEvents('all')

    # In this example, we have no use for any eye data between trials, so why save it.
    tracker.setRecordingState(False)

    #Clear Event Buffers
    io.clearEvents()

    posnerExp.nextEntry() #add this stuff to the file defined in the posnerExp (experiment handler)
    t+=1
    

# This logs to the ioStore that the experiment has ended
# Note, disconnecting the tracker does not mean experiment = finished hence this message
io.sendMessageEvent(text='EXPERIMENT_COMPLETE')

tracker.setConnectionState(False)
