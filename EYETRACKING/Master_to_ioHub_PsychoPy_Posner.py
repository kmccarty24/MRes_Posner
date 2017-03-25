# -*- coding: utf-8 -*-

# PsychoPy 2 - Posner Cueing Task Example w/ Frame Timer
# Dr K McCarty
# Northumbria University
# February 2017

#Import the necessary modules from the Python storage bank
from psychopy import visual, core, data, gui, event

from psychopy.iohub import (launchHubServer, EventConstants, EyeTrackerConstants, module_directory, 
                            getCurrentDateTimeString, ioHubExperimentRuntime)


#Particicpant Info and Other Settings
info = {}
info['participant'] = '0'
info['dateStr'] = data.getDateStr() #will create str of current date/time
dlg = gui.DlgFromDict(info) #dialog box
if not dlg.OK: #did they push ok?
    core.quit()



###############----ioHub Start and Hardware----#############

io = launchHubServer(iohub_config_name = 'iohub_config.yaml', experiment_code = info['participant'])

#Declare our Hardware
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

mouse.setSystemCursorVisibility(False)

#Start by running the eye tracker default setup procedure.
#This should be done BEFORE the PsychoPy Window Appears 
tracker.runSetupProcedure()


###############----My Filename when saved----###############

filename = "data/" + info['participant'] + "_" + info['dateStr']

###############----Trial/Experiment Handler----###############

conditions = data.importConditions('conditions.xlsx') #basically imports your trials and assigns them to condition 

#add trialHandler
trials = data.TrialHandler(trialList=conditions, nReps=1) #default method is randomised, trials = trial handler function thats based on conditions as the trialList

#add trials to the experiment handler to store data
posnerExp = data.ExperimentHandler(name='Posner', version='2.0',
                                   extraInfo = info,
                                   dataFileName = filename)

posnerExp.addLoop(trials) #there could be other loops (like practice loop)

# Tell the ioHub we are using a PsychoPy TrialHandler so it can structure its contents
io.createTrialHandlerRecordTable(trials)

##############-----Windows, Stimuli and Conditions File Stuff----##############

#Window changes to be more dynamic
res = display.getPixelResolution() # Returns a Tuple
units = display.getCoordinateType()

win = visual.Window(res, monitor = display.getPsychopyMonitorName(),
                    fullscr = False, units = units, allowGUI = False, 
                    color = 'black', screen = display.getIndex())

#Rest of the nuts and bolts
fixation = visual.Circle(win, size = 5, lineColor = 'red', 
                         fillColor = 'red')

probe = visual.ImageStim(win, size = 80, pos = [300, 0], 
                         image = None, mask = 'raisedCos',
                         color = 'blue') 

cue = visual.ShapeStim(win, vertices = [[-30, 20], [30, 40], [30, 0]],
                       lineColor = 'red', fillColor = 'firebrick')

gaze_dot =visual.GratingStim(win, tex=None, mask="raisedCos", 
                             pos=(0, 0), size=(66, 66), color='green', 
                             units=units)

respClock = core.Clock()

instText = 'Press Left if the circle appears on the left, press right if it is on the right'


def showInstructions(text, txtCol = 'white', win = win):
    global flip_time

    io.clearEvents('all')

    instruct = visual.TextStim(win, text = text, color = 'white')
    instruct.draw()
    flip_time = win.flip() #this logs time between consecutive frame flips
    kb.waitForPresses(keys=' ')



###############----Trials----###############

#Display Instructions
showInstructions(text = instText)

#Tell ioHub we are starting
io.sendMessageEvent(text="EXPERIMENT_START", sec_time=flip_time)

#Pass some info to the ioHub regarding settings
io.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO START") 
io.sendMessageEvent(text="ioHub Experiment started {0}".format(getCurrentDateTimeString()))
io.sendMessageEvent(text="Experiment ID: {0}, Session ID: {1}".format(io.experimentID,io.experimentSessionID))
io.sendMessageEvent(text="Stimulus Screen ID: {0}, Size (pixels): {1}, CoordType: {2}".format(display.getIndex(),display.getPixelResolution(),display.getCoordinateType()))
io.sendMessageEvent(text="Calculated Pixels Per Degree: {0} x, {1} y".format(*display.getPixelsPerDegree()))        
io.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO END")

#Clear events before trail start
io.clearEvents('all')

#Begin Trial Sequence
t = 1
for thisTrial in trials: 

    #Reset resp and rt
    resp=None
    rt=None

    #Set up trial variables
    probe.pos = [thisTrial['probeX'], 0] 
    cue.ori = thisTrial['cueOri'] 
    print probe.pos, 'Probe'
    print cue.ori, 'Cue'

    #Clear window and log time (so its more accurate for the next message log)
    flips = win.flip()

    #Send a message to ioHub that the main trial is about to begin
    io.sendMessageEvent(text="TRIAL{}_START".format(t), sec_time=flips)

    #Log some experiment stuff to the trialHandler Dictionary for this trial
    thisTrial['session_id']=io.getSessionID()
    thisTrial['trial_id']=t + 1
    thisTrial['TRIAL_START']=flips

    #Clear Events
    io.clearEvents('all')

    #Turn the tracker on
    tracker.setRecordingState(True)

    #Get some gaze coordinates from it (should return a tuple of x,y coords)
    gpos = tracker.getLastGazePosition()

    #Display Fixation for 500ms
    for frameN in range(30): #500ms
        fixation.draw()

        gpos = tracker.getLastGazePosition()

        try:
            gaze_dot.pos = ([gpos[0], gpos[1]])
            gaze_dot.draw()
        except:
            pass

        if frameN == 0:
            flips = win.flip()
            io.sendMessageEvent(text ="Fix_Onset TrialNo {}".format(t), sec_time = flips)
        else:
            win.flip()

    #Log offset of fixation
    flips = win.flip() #(switches to blank)
    io.sendMessageEvent(text ="Fix_Offset TrialNo {}".format(t), sec_time = flips)


    # Display Cues for 200ms
    for frameN in range(12):
        cue.draw()

        gpos = tracker.getLastGazePosition()

        try:
            gaze_dot.pos = (gpos[0], gpos[1])
            gaze_dot.draw()
        except:
            pass

        if frameN == 0:
            flips = win.flip()
            io.sendMessageEvent(text ="Cue_Onset TrialNo {}".format(t), sec_time = flips)
        else:
            win.flip()

    #Log offset of cue
    flips = win.flip()
    io.sendMessageEvent(text ="Cue_Offset TrialNo {}".format(t), sec_time = flips)

    #Reset the clock on flip
    win.callOnFlip(respClock.reset) #NB: reset not reset() 

    #Clear Events 
    io.clearEvents('all')

    #Change the probe display to a while loop
    iteration = 0 #needed for the while to set onset message

    keys = []

    while len(keys) == 0:
        
        probe.draw()

        gpos = tracker.getLastGazePosition()

        try:
            gaze_dot.pos = (gpos[0], gpos[1])
            gaze_dot.draw()
        except:
            pass

        if iteration == 0:
            flips = win.flip()
            io.sendMessageEvent(text ="Probe_Onset TrialNo {0} Coords = {1}, {2}".format(t, gpos[0], gpos[1]), sec_time = flips)
            iteration +=1
        else:
            win.flip()

        keys = kb.getKeys(keys = ['m','z','ESCAPE'])

        if len(keys) == 0:
            pass
        elif 'm' in keys and thisTrial['probeX']== 300:
            rt = respClock.getTime()
            corr = 1
            print 'correct'
            break
        elif 'z' in keys and thisTrial['probeX']== -300:
            rt = respClock.getTime()
            corr = 1
            print 'correct'
            break
        elif 'ESCAPE' in keys:
            io.sendMessageEvent(text ="Pressed Escape TrialN {}".format(t), sec_time = flips)
            tracker.setRecordingState(False)
            tracker.setConnectionState(False)
            trials.finished = True
            win.close()
            core.quit()
            quit()
        else:
            rt = respClock.getTime()
            print 'incorrect'
            corr = 0
            break

    print keys
    #Add data
    trials.addData('rt', rt)
    trials.addData('key', keys[0].key)
    trials.addData('Correct', corr)

    #Log offset and trial end
    flips = win.flip()
    thisTrial['TRIAL_END'] = flips
    io.sendMessageEvent(text ="Probe_Offset TrialNo {}".format(t), sec_time = flips)
    print 'Trial ended'

    #Add the thisTrial dictionary to the ioHub file
    io.addRowToConditionVariableTable(thisTrial.values())

    #Clear events
    io.clearEvents('all')

    #We have no need to record eyes between trials so stop record
    tracker.setRecordingState(False)

    #Clear events
    io.clearEvents('all')
    
    #Set the Experiment Handler to the next row
    posnerExp.nextEntry()

    #Increment trial number
    t+=1


#Signal end of trials
io.sendMessageEvent(text ='EXPERIMENT_COMPLETE')

#Disconnect from the tracker
tracker.setConnectionState(False)

###############-----------------Ends-----------------------###############
