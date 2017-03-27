# -*- coding: utf-8 -*-

# PsychoPy 2 - Posner Cueing Task Example w/ Frame Timer
# Dr K McCarty
# Northumbria University
# February 2017

#Import the necessary modules from the Python storage bank
from psychopy import visual, core, data, gui, event 

info = {}
info['participant'] = ''
info['dateStr'] = data.getDateStr() 
dlg = gui.DlgFromDict(info) 
if not dlg.OK: 
    core.quit()

###############----ioHub Start and Hardware----#############

#Declare our Hardware
# try:
#     tracker=io.devices.tracker
# except Exception:
#     # No eye tracker config found in iohub_config.yaml
#     from psychopy.iohub.util import MessageDialog
#     md = MessageDialog(title="No Eye Tracker Configuration Found",
#                        msg="Update the iohub_config.yaml file by "
#                        "uncommenting\nthe appropriate eye tracker "
#                        "config lines.\n\nPress OK to exit demo.",
#                        showButtons=MessageDialog.OK_BUTTON,
#                        dialogType=MessageDialog.ERROR_DIALOG,
#                        allowCancel=False,
#                        display_index=0)
#     md.show()


#Start by running the eye tracker default setup procedure.
#This should be done BEFORE the PsychoPy Window Appears 



###############----------------My Filename when saved----------------------###############

filename = "data/" + info['participant'] + "_" + info['dateStr']

###############----------------Windows, Stimuli and Conditions File Stuff------------------------###############

win = visual.Window((1024,768),
                    fullscr = False, 
                    units = 'pix', 
                    waitBlanking=True, 
                    color = 'black')

fixation = visual.Circle(win, size =  5, 
                         lineColor = 'white', 
                         fillColor = 'black')

respClock = core.Clock() #create the class clock.

probe = visual.ImageStim(win, size = 80, 
                         pos = [300, 0], 
                         image = None, 
                         mask = 'raisedCos', 
                         color = 'blue') 

cue = visual.ShapeStim(win, 
                       vertices = [[-30,20],[30,40],[30,0]], 
                       lineColor = 'red', 
                       fillColor = 'firebrick')


###############-------------Trial/Experiment Handler---------------------------###############

conditions = data.importConditions('conditions.xlsx')

#add trialHandler
trials = data.TrialHandler(trialList=conditions, nReps=5) 

#add trials to the experiment handler to store data
posnerExp = data.ExperimentHandler(name='Posner', version='1.2',
                                   extraInfo = info,
                                   dataFileName = filename)

posnerExp.addLoop(trials)


###############----------------Trials-----------------------###############

# Instructions

instruct = 'Press Left if the circle appears on the left, press right if it is on the right'

instructions = visual.TextStim(win, text = instruct , color = 'white')

instructions.draw()
win.flip()
keys = event.waitKeys(keyList = ['space'])

#Tell ioHub we are starting


#Pass some info to the ioHub regarding settings
# io.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO START") 
# io.sendMessageEvent(text="ioHub Experiment started {0}".format(getCurrentDateTimeString()))
# io.sendMessageEvent(text="Experiment ID: {0}, Session ID: {1}".format(io.experimentID,io.experimentSessionID))
# io.sendMessageEvent(text="Stimulus Screen ID: {0}, Size (pixels): {1}, CoordType: {2}".format(display.getIndex(), res, units))
# io.sendMessageEvent(text="Calculated Pixels Per Degree: {0} x, {1} y".format(*display.getPixelsPerDegree()))        
# io.sendMessageEvent(text="IO_HUB EXPERIMENT_INFO END")


for thisTrial in trials:

    resp=None
    rt=None

    probe.pos = [thisTrial['probeX'],0]
    cue.ori = thisTrial['cueOri']
    print probe.pos, 'Probe'
    print cue.ori, 'Cue'

    for frameN in range(30): #500ms
        fixation.draw()
        win.flip() 

    for frameN in range(12): # 200ms 
        cue.draw()
        win.flip()

    win.callOnFlip(respClock.reset)

    event.clearEvents()

    for frameN in range(12):
        keys = event.getKeys(keyList = ['left','right','escape'])
        if len(keys)>0:
            resp = keys[0]
            rt=respClock.getTime()
            break
        probe.draw()
        win.flip()

    win.flip()

    if resp is None:
        keys = event.waitKeys(keyList=['left', 'right', 'escape']) 
        resp = keys[0] 
        rt=respClock.getTime()

    if thisTrial['probeX']==300 and resp=='right':
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

    posnerExp.nextEntry()

###############-----------------Ends-----------------------###############
