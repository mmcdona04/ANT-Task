#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 09, 2020, at 15:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'ANT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\cantb\\Desktop\\the-attention-network-task-master\\the-attention-network-task-master\\ANT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "PracInstruc"
PracInstrucClock = core.Clock()
pracText1 = visual.TextStim(win=win, name='pracText1',
    text='Welcome to this experiment.\n\nIn this task, you will be presented with a central arrow surrounded by arrows or blocks. The central arrow will point left or right.\n\nSometimes the flanking arrows will be pointing in the same direction as the central arrow, and sometimes the flanking arrows will point in the oppoiste direction to the central arrow.\n\neg. >>>>> or >><>>\n\nYour task is to respond to the direction of the central arrow.\n\nIf the central arrow points to the right, press the right arrow key and if the arrow points to the left, press the left arrow key.\n\nPress the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pracResp1 = keyboard.Keyboard()

# Initialize components for Routine "PracInstruct2"
PracInstruct2Clock = core.Clock()
practInst2 = visual.TextStim(win=win, name='practInst2',
    text='In this task, you must respond to the direction of the centre arrow using the arrow keys.\n\nFirst, a fixation cross will appear in the centre of the screen. The fixation is sometimes followed by blocks on the screen, which may or may not\ncue the location of the target stimulus. If the blocks appear after the fixation, it means that the target will appear shortly.\n\nIf the blocks appears either above OR below the fixation cross, the target will shortly appear in that cued location.\n\nFirst there will be a practice trial, where you will recieve feedback and reaction times for each correct response.\n\nPlace your index fingers on the left and right keys ready to start, and press the spacebar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
practResp2 = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixDuration  = .4
image = visual.ImageStim(
    win=win,
    name='image', units='height', 
    image='stim/fix.png', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cues = visual.ImageStim(
    win=win,
    name='cues', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target = visual.ImageStim(
    win=win,
    name='target', units='height', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
resp = keyboard.Keyboard()
fixationshort = visual.ImageStim(
    win=win,
    name='fixationshort', units='height', 
    image='stim/fix.png', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MainInstruc"
MainInstrucClock = core.Clock()
mainInst = visual.TextStim(win=win, name='mainInst',
    text='That is the end of the practice trials.\n\nThe main trials will now begin. There will be 2 blocks of trials, with a rest period between each one. \n\nThe main trials involve the same instructions as before, however, you will not receive feedback on your responses.\n\nPress the spacebar to continue.',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instResp = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixDuration  = .4
image = visual.ImageStim(
    win=win,
    name='image', units='height', 
    image='stim/fix.png', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cues = visual.ImageStim(
    win=win,
    name='cues', units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target = visual.ImageStim(
    win=win,
    name='target', units='height', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
resp = keyboard.Keyboard()
fixationshort = visual.ImageStim(
    win=win,
    name='fixationshort', units='height', 
    image='stim/fix.png', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "Rest"
RestClock = core.Clock()
rest = visual.TextStim(win=win, name='rest',
    text='You have completed a block of main trials.\n\nHave a short rest as required, and press the space bar to continue to the next block of trials when you are ready.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
restResp = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='That is the end of the main trial. \n\nThank you for taking part in this experiment.\n\nPress any key to exit.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endKey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "PracInstruc"-------
continueRoutine = True
# update component parameters for each repeat
pracResp1.keys = []
pracResp1.rt = []
_pracResp1_allKeys = []
# keep track of which components have finished
PracInstrucComponents = [pracText1, pracResp1]
for thisComponent in PracInstrucComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracInstrucClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracInstruc"-------
while continueRoutine:
    # get current time
    t = PracInstrucClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracInstrucClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pracText1* updates
    if pracText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracText1.frameNStart = frameN  # exact frame index
        pracText1.tStart = t  # local t and not account for scr refresh
        pracText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracText1, 'tStartRefresh')  # time at next scr refresh
        pracText1.setAutoDraw(True)
    
    # *pracResp1* updates
    waitOnFlip = False
    if pracResp1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pracResp1.frameNStart = frameN  # exact frame index
        pracResp1.tStart = t  # local t and not account for scr refresh
        pracResp1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pracResp1, 'tStartRefresh')  # time at next scr refresh
        pracResp1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(pracResp1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(pracResp1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if pracResp1.status == STARTED and not waitOnFlip:
        theseKeys = pracResp1.getKeys(keyList=['space'], waitRelease=False)
        _pracResp1_allKeys.extend(theseKeys)
        if len(_pracResp1_allKeys):
            pracResp1.keys = _pracResp1_allKeys[-1].name  # just the last key pressed
            pracResp1.rt = _pracResp1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracInstrucComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracInstruc"-------
for thisComponent in PracInstrucComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('pracText1.started', pracText1.tStartRefresh)
thisExp.addData('pracText1.stopped', pracText1.tStopRefresh)
# the Routine "PracInstruc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracInstruct2"-------
continueRoutine = True
# update component parameters for each repeat
practResp2.keys = []
practResp2.rt = []
_practResp2_allKeys = []
# keep track of which components have finished
PracInstruct2Components = [practInst2, practResp2]
for thisComponent in PracInstruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracInstruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracInstruct2"-------
while continueRoutine:
    # get current time
    t = PracInstruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracInstruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practInst2* updates
    if practInst2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practInst2.frameNStart = frameN  # exact frame index
        practInst2.tStart = t  # local t and not account for scr refresh
        practInst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practInst2, 'tStartRefresh')  # time at next scr refresh
        practInst2.setAutoDraw(True)
    
    # *practResp2* updates
    waitOnFlip = False
    if practResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practResp2.frameNStart = frameN  # exact frame index
        practResp2.tStart = t  # local t and not account for scr refresh
        practResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practResp2, 'tStartRefresh')  # time at next scr refresh
        practResp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practResp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practResp2.status == STARTED and not waitOnFlip:
        theseKeys = practResp2.getKeys(keyList=['space'], waitRelease=False)
        _practResp2_allKeys.extend(theseKeys)
        if len(_practResp2_allKeys):
            practResp2.keys = _practResp2_allKeys[-1].name  # just the last key pressed
            practResp2.rt = _practResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracInstruct2"-------
for thisComponent in PracInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practInst2.started', practInst2.tStartRefresh)
thisExp.addData('practInst2.stopped', practInst2.tStopRefresh)
# the Routine "PracInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond.xlsx', selection='0:24'),
    seed=None, name='pracLoop')
thisExp.addLoop(pracLoop)  # add the loop to the experiment
thisPracLoop = pracLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracLoop.rgb)
if thisPracLoop != None:
    for paramName in thisPracLoop:
        exec('{} = thisPracLoop[paramName]'.format(paramName))

for thisPracLoop in pracLoop:
    currentLoop = pracLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracLoop.rgb)
    if thisPracLoop != None:
        for paramName in thisPracLoop:
            exec('{} = thisPracLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    durations = np.arange(.4, .6, .05)  # Create durations 
    shuffle(durations)  # Randomize durations 
    fixDuration  = durations[0] # Take one of the randomized durations
    # keep track of which components have finished
    fixationComponents = [image]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + fixDuration-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("fixFuration", fixDuration)
    pracLoop.addData('image.started', image.tStartRefresh)
    pracLoop.addData('image.stopped', image.tStopRefresh)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    cues.setImage(cue)
    target.setOri(targOrientation)
    target.setImage(tar)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [cues, target, resp, fixationshort]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cues* updates
        if cues.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            cues.frameNStart = frameN  # exact frame index
            cues.tStart = t  # local t and not account for scr refresh
            cues.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cues, 'tStartRefresh')  # time at next scr refresh
            cues.setAutoDraw(True)
        if cues.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cues.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                cues.tStop = t  # not accounting for scr refresh
                cues.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cues, 'tStopRefresh')  # time at next scr refresh
                cues.setAutoDraw(False)
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                resp.status = FINISHED
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[0].name  # just the first key pressed
                resp.rt = _resp_allKeys[0].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fixationshort* updates
        if fixationshort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationshort.frameNStart = frameN  # exact frame index
            fixationshort.tStart = t  # local t and not account for scr refresh
            fixationshort.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationshort, 'tStartRefresh')  # time at next scr refresh
            fixationshort.setAutoDraw(True)
        if fixationshort.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationshort.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fixationshort.tStop = t  # not accounting for scr refresh
                fixationshort.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationshort, 'tStopRefresh')  # time at next scr refresh
                fixationshort.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pracLoop.addData('cues.started', cues.tStartRefresh)
    pracLoop.addData('cues.stopped', cues.tStopRefresh)
    pracLoop.addData('target.started', target.tStartRefresh)
    pracLoop.addData('target.stopped', target.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for pracLoop (TrialHandler)
    pracLoop.addData('resp.keys',resp.keys)
    pracLoop.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        pracLoop.addData('resp.rt', resp.rt)
    pracLoop.addData('resp.started', resp.tStartRefresh)
    pracLoop.addData('resp.stopped', resp.tStopRefresh)
    pracLoop.addData('fixationshort.started', fixationshort.tStartRefresh)
    pracLoop.addData('fixationshort.stopped', fixationshort.tStopRefresh)
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    msg = ''
    
    if resp.corr:
        msg = "Correct! Your RT is : {}".format(round(resp.rt, 2))
    elif not resp.corr:
        msg = "Incorrect!"
        
    text.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pracLoop.addData('text.started', text.tStartRefresh)
    pracLoop.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'pracLoop'


# ------Prepare to start Routine "MainInstruc"-------
continueRoutine = True
# update component parameters for each repeat
instResp.keys = []
instResp.rt = []
_instResp_allKeys = []
# keep track of which components have finished
MainInstrucComponents = [mainInst, instResp]
for thisComponent in MainInstrucComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MainInstrucClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MainInstruc"-------
while continueRoutine:
    # get current time
    t = MainInstrucClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MainInstrucClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mainInst* updates
    if mainInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mainInst.frameNStart = frameN  # exact frame index
        mainInst.tStart = t  # local t and not account for scr refresh
        mainInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mainInst, 'tStartRefresh')  # time at next scr refresh
        mainInst.setAutoDraw(True)
    
    # *instResp* updates
    waitOnFlip = False
    if instResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instResp.frameNStart = frameN  # exact frame index
        instResp.tStart = t  # local t and not account for scr refresh
        instResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instResp, 'tStartRefresh')  # time at next scr refresh
        instResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instResp.status == STARTED and not waitOnFlip:
        theseKeys = instResp.getKeys(keyList=['space'], waitRelease=False)
        _instResp_allKeys.extend(theseKeys)
        if len(_instResp_allKeys):
            instResp.keys = _instResp_allKeys[-1].name  # just the last key pressed
            instResp.rt = _instResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstrucComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MainInstruc"-------
for thisComponent in MainInstrucComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('mainInst.started', mainInst.tStartRefresh)
thisExp.addData('mainInst.stopped', mainInst.tStopRefresh)
# check responses
if instResp.keys in ['', [], None]:  # No response was made
    instResp.keys = None
thisExp.addData('instResp.keys',instResp.keys)
if instResp.keys != None:  # we had a response
    thisExp.addData('instResp.rt', instResp.rt)
thisExp.addData('instResp.started', instResp.tStartRefresh)
thisExp.addData('instResp.stopped', instResp.tStopRefresh)
thisExp.nextEntry()
# the Routine "MainInstruc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blockLoop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blockLoop')
thisExp.addLoop(blockLoop)  # add the loop to the experiment
thisBlockLoop = blockLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
if thisBlockLoop != None:
    for paramName in thisBlockLoop:
        exec('{} = thisBlockLoop[paramName]'.format(paramName))

for thisBlockLoop in blockLoop:
    currentLoop = blockLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            exec('{} = thisBlockLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    mainLoop = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('cond.xlsx'),
        seed=None, name='mainLoop')
    thisExp.addLoop(mainLoop)  # add the loop to the experiment
    thisMainLoop = mainLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            exec('{} = thisMainLoop[paramName]'.format(paramName))
    
    for thisMainLoop in mainLoop:
        currentLoop = mainLoop
        # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
        if thisMainLoop != None:
            for paramName in thisMainLoop:
                exec('{} = thisMainLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        durations = np.arange(.4, .6, .05)  # Create durations 
        shuffle(durations)  # Randomize durations 
        fixDuration  = durations[0] # Take one of the randomized durations
        # keep track of which components have finished
        fixationComponents = [image]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + fixDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("fixFuration", fixDuration)
        mainLoop.addData('image.started', image.tStartRefresh)
        mainLoop.addData('image.stopped', image.tStopRefresh)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        cues.setImage(cue)
        target.setOri(targOrientation)
        target.setImage(tar)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        # keep track of which components have finished
        trialComponents = [cues, target, resp, fixationshort]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cues* updates
            if cues.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                cues.frameNStart = frameN  # exact frame index
                cues.tStart = t  # local t and not account for scr refresh
                cues.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cues, 'tStartRefresh')  # time at next scr refresh
                cues.setAutoDraw(True)
            if cues.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cues.tStartRefresh + .1-frameTolerance:
                    # keep track of stop time/frame for later
                    cues.tStop = t  # not accounting for scr refresh
                    cues.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(cues, 'tStopRefresh')  # time at next scr refresh
                    cues.setAutoDraw(False)
            
            # *target* updates
            if target.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                target.frameNStart = frameN  # exact frame index
                target.tStart = t  # local t and not account for scr refresh
                target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
                target.setAutoDraw(True)
            if target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    target.tStop = t  # not accounting for scr refresh
                    target.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                    target.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[0].name  # just the first key pressed
                    resp.rt = _resp_allKeys[0].rt
                    # was this correct?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *fixationshort* updates
            if fixationshort.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationshort.frameNStart = frameN  # exact frame index
                fixationshort.tStart = t  # local t and not account for scr refresh
                fixationshort.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationshort, 'tStartRefresh')  # time at next scr refresh
                fixationshort.setAutoDraw(True)
            if fixationshort.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationshort.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationshort.tStop = t  # not accounting for scr refresh
                    fixationshort.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixationshort, 'tStopRefresh')  # time at next scr refresh
                    fixationshort.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        mainLoop.addData('cues.started', cues.tStartRefresh)
        mainLoop.addData('cues.stopped', cues.tStopRefresh)
        mainLoop.addData('target.started', target.tStartRefresh)
        mainLoop.addData('target.stopped', target.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for mainLoop (TrialHandler)
        mainLoop.addData('resp.keys',resp.keys)
        mainLoop.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            mainLoop.addData('resp.rt', resp.rt)
        mainLoop.addData('resp.started', resp.tStartRefresh)
        mainLoop.addData('resp.stopped', resp.tStopRefresh)
        mainLoop.addData('fixationshort.started', fixationshort.tStartRefresh)
        mainLoop.addData('fixationshort.stopped', fixationshort.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 2 repeats of 'mainLoop'
    
    
    # ------Prepare to start Routine "Rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    restResp.keys = []
    restResp.rt = []
    _restResp_allKeys = []
    # keep track of which components have finished
    RestComponents = [rest, restResp]
    for thisComponent in RestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Rest"-------
    while continueRoutine:
        # get current time
        t = RestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest* updates
        if rest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest.frameNStart = frameN  # exact frame index
            rest.tStart = t  # local t and not account for scr refresh
            rest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest, 'tStartRefresh')  # time at next scr refresh
            rest.setAutoDraw(True)
        
        # *restResp* updates
        waitOnFlip = False
        if restResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            restResp.frameNStart = frameN  # exact frame index
            restResp.tStart = t  # local t and not account for scr refresh
            restResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(restResp, 'tStartRefresh')  # time at next scr refresh
            restResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(restResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(restResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if restResp.status == STARTED and not waitOnFlip:
            theseKeys = restResp.getKeys(keyList=['space'], waitRelease=False)
            _restResp_allKeys.extend(theseKeys)
            if len(_restResp_allKeys):
                restResp.keys = _restResp_allKeys[-1].name  # just the last key pressed
                restResp.rt = _restResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rest"-------
    for thisComponent in RestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('rest.started', rest.tStartRefresh)
    blockLoop.addData('rest.stopped', rest.tStopRefresh)
    # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'blockLoop'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
endKey.keys = []
endKey.rt = []
_endKey_allKeys = []
# keep track of which components have finished
EndComponents = [endText, endKey]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    
    # *endKey* updates
    waitOnFlip = False
    if endKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endKey.frameNStart = frameN  # exact frame index
        endKey.tStart = t  # local t and not account for scr refresh
        endKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endKey, 'tStartRefresh')  # time at next scr refresh
        endKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endKey.status == STARTED and not waitOnFlip:
        theseKeys = endKey.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _endKey_allKeys.extend(theseKeys)
        if len(_endKey_allKeys):
            endKey.keys = _endKey_allKeys[-1].name  # just the last key pressed
            endKey.rt = _endKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
