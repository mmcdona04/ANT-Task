#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b12),
    on December 10, 2018, at 14:30
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.0b12'
expName = 'ANT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
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
    originPath='C:\\Users\\lpzdb\\pavloviaDemos\\ANT\\ANT.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "PracInstruc"
PracInstrucClock = core.Clock()
pracText1 = visual.TextStim(win=win, name='pracText1',
    text='Welcome to this experiment.\n\nIn this task, you will be presented with a central arrow surrounded by arrows or blocks. The central arrow will point left or right.\n\nSometimes the flanking arrows will be pointing in the same direction as the central arrow, and sometimes the flanking arrows will point in the oppoiste direction to the central arrow.\n\neg. >>>>> or >><>>\n\nYour task is to respond to the direction of the central arrow.\n\nIf the central arrow points to the right, press the right arrow key and if the arrow points to the left, press the left arrow key.\n\nPress the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracInstruct2"
PracInstruct2Clock = core.Clock()
practInst2 = visual.TextStim(win=win, name='practInst2',
    text='In this task, you must respond to the direction of the centre arrow using the arrow keys.\n\nFirst, a fixation cross will appear in the centre of the screen. The fixation is sometimes followed by blocks on the screen, which may or may not\ncue the location of the target stimulus. If the blocks appear after the fixation, it means that the target will appear shortly.\n\nIf the blocks appears either above OR below the fixation cross, the target will shortly appear in that cued location.\n\nFirst there will be a practice trial, where you will recieve feedback and reaction times for each correct response.\n\nPlace your index fingers on the left and right keys ready to start, and press the spacebar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixDuration  = .4
image = visual.ImageStim(
    win=win, name='image',units='height', 
    image='stim/fix.png', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cues = visual.ImageStim(
    win=win, name='cues',units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target = visual.ImageStim(
    win=win, name='target',units='height', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fixationshort = visual.ImageStim(
    win=win, name='fixationshort',units='height', 
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
    text='That is the end of the practice trials.\n\nThe main trials will now begin. There will be 3 blocks of trials, with a rest period between each one. \n\nThe main trials involve the same instructions as before, however, you will not receive feedback on your responses.\n\nPress the spacebar to continue.',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixDuration  = .4
image = visual.ImageStim(
    win=win, name='image',units='height', 
    image='stim/fix.png', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
cues = visual.ImageStim(
    win=win, name='cues',units='height', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
target = visual.ImageStim(
    win=win, name='target',units='height', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
fixationshort = visual.ImageStim(
    win=win, name='fixationshort',units='height', 
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

# Initialize components for Routine "End"
EndClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='That is the end of the main trial. \n\nThank you for taking part in this experiment.\n\nPress any key to exit.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "PracInstruc"-------
t = 0
PracInstrucClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
pracResp1 = event.BuilderKeyResponse()
# keep track of which components have finished
PracInstrucComponents = [pracText1, pracResp1]
for thisComponent in PracInstrucComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PracInstruc"-------
while continueRoutine:
    # get current time
    t = PracInstrucClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pracText1* updates
    if t >= 0.0 and pracText1.status == NOT_STARTED:
        # keep track of start time/frame for later
        pracText1.tStart = t
        pracText1.frameNStart = frameN  # exact frame index
        pracText1.setAutoDraw(True)
    
    # *pracResp1* updates
    if t >= 0.0 and pracResp1.status == NOT_STARTED:
        # keep track of start time/frame for later
        pracResp1.tStart = t
        pracResp1.frameNStart = frameN  # exact frame index
        pracResp1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if pracResp1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracInstrucComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracInstruc"-------
for thisComponent in PracInstrucComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "PracInstruc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracInstruct2"-------
t = 0
PracInstruct2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
practResp2 = event.BuilderKeyResponse()
# keep track of which components have finished
PracInstruct2Components = [practInst2, practResp2]
for thisComponent in PracInstruct2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PracInstruct2"-------
while continueRoutine:
    # get current time
    t = PracInstruct2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practInst2* updates
    if t >= 0.0 and practInst2.status == NOT_STARTED:
        # keep track of start time/frame for later
        practInst2.tStart = t
        practInst2.frameNStart = frameN  # exact frame index
        practInst2.setAutoDraw(True)
    
    # *practResp2* updates
    if t >= 0.0 and practResp2.status == NOT_STARTED:
        # keep track of start time/frame for later
        practResp2.tStart = t
        practResp2.frameNStart = frameN  # exact frame index
        practResp2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if practResp2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracInstruct2"-------
for thisComponent in PracInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
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
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    durations = np.arange(.4, .6, .05)  # Create durations 
    shuffle(durations)  # Randomize durations 
    fixDuration  = durations[0] # Take one of the randomized durations
    # keep track of which components have finished
    fixationComponents = [image]
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + fixDuration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData("fixFuration", fixDuration)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.200000)
    # update component parameters for each repeat
    cues.setImage(cue)
    target.setOri(targOrientation)
    target.setImage(tar)
    resp = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [cues, target, resp, fixationshort]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cues* updates
        if t >= 0 and cues.status == NOT_STARTED:
            # keep track of start time/frame for later
            cues.tStart = t
            cues.frameNStart = frameN  # exact frame index
            cues.setAutoDraw(True)
        frameRemains = 0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cues.status == STARTED and t >= frameRemains:
            cues.setAutoDraw(False)
        
        # *target* updates
        if t >= .5 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t
            target.frameNStart = frameN  # exact frame index
            target.setAutoDraw(True)
        frameRemains = .5 + 1.7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if target.status == STARTED and t >= frameRemains:
            target.setAutoDraw(False)
        
        # *resp* updates
        if t >= .5 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = .5 + 1.7- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp.status == STARTED and t >= frameRemains:
            resp.status = STOPPED
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if resp.keys == []:  # then this was the first keypress
                    resp.keys = theseKeys[0]  # just the first key pressed
                    resp.rt = resp.clock.getTime()
                    # was this 'correct'?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # *fixationshort* updates
        if t >= 0.0 and fixationshort.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixationshort.tStart = t
            fixationshort.frameNStart = frameN  # exact frame index
            fixationshort.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixationshort.status == STARTED and t >= frameRemains:
            fixationshort.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
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
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
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
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'pracLoop'


# ------Prepare to start Routine "MainInstruc"-------
t = 0
MainInstrucClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instResp = event.BuilderKeyResponse()
# keep track of which components have finished
MainInstrucComponents = [mainInst, instResp]
for thisComponent in MainInstrucComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "MainInstruc"-------
while continueRoutine:
    # get current time
    t = MainInstrucClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mainInst* updates
    if t >= 0.0 and mainInst.status == NOT_STARTED:
        # keep track of start time/frame for later
        mainInst.tStart = t
        mainInst.frameNStart = frameN  # exact frame index
        mainInst.setAutoDraw(True)
    
    # *instResp* updates
    if t >= 0.0 and instResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instResp.tStart = t
        instResp.frameNStart = frameN  # exact frame index
        instResp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instResp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instResp.keys = theseKeys[-1]  # just the last key pressed
            instResp.rt = instResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MainInstrucComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MainInstruc"-------
for thisComponent in MainInstrucComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instResp.keys in ['', [], None]:  # No response was made
    instResp.keys=None
thisExp.addData('instResp.keys',instResp.keys)
if instResp.keys != None:  # we had a response
    thisExp.addData('instResp.rt', instResp.rt)
thisExp.nextEntry()
# the Routine "MainInstruc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blockLoop = data.TrialHandler(nReps=3, method='random', 
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
        t = 0
        fixationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        durations = np.arange(.4, .6, .05)  # Create durations 
        shuffle(durations)  # Randomize durations 
        fixDuration  = durations[0] # Take one of the randomized durations
        # keep track of which components have finished
        fixationComponents = [image]
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "fixation"-------
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.0 + fixDuration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData("fixFuration", fixDuration)
        # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.200000)
        # update component parameters for each repeat
        cues.setImage(cue)
        target.setOri(targOrientation)
        target.setImage(tar)
        resp = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [cues, target, resp, fixationshort]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cues* updates
            if t >= 0 and cues.status == NOT_STARTED:
                # keep track of start time/frame for later
                cues.tStart = t
                cues.frameNStart = frameN  # exact frame index
                cues.setAutoDraw(True)
            frameRemains = 0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cues.status == STARTED and t >= frameRemains:
                cues.setAutoDraw(False)
            
            # *target* updates
            if t >= .5 and target.status == NOT_STARTED:
                # keep track of start time/frame for later
                target.tStart = t
                target.frameNStart = frameN  # exact frame index
                target.setAutoDraw(True)
            frameRemains = .5 + 1.7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if target.status == STARTED and t >= frameRemains:
                target.setAutoDraw(False)
            
            # *resp* updates
            if t >= .5 and resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp.tStart = t
                resp.frameNStart = frameN  # exact frame index
                resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = .5 + 1.7- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp.status == STARTED and t >= frameRemains:
                resp.status = STOPPED
            if resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if resp.keys == []:  # then this was the first keypress
                        resp.keys = theseKeys[0]  # just the first key pressed
                        resp.rt = resp.clock.getTime()
                        # was this 'correct'?
                        if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                            resp.corr = 1
                        else:
                            resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *fixationshort* updates
            if t >= 0.0 and fixationshort.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixationshort.tStart = t
                fixationshort.frameNStart = frameN  # exact frame index
                fixationshort.setAutoDraw(True)
            frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixationshort.status == STARTED and t >= frameRemains:
                fixationshort.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys=None
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
        thisExp.nextEntry()
        
    # completed 2 repeats of 'mainLoop'
    
    
    # ------Prepare to start Routine "Rest"-------
    t = 0
    RestClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    restResp = event.BuilderKeyResponse()
    # keep track of which components have finished
    RestComponents = [rest, restResp]
    for thisComponent in RestComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Rest"-------
    while continueRoutine:
        # get current time
        t = RestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest* updates
        if t >= 0.0 and rest.status == NOT_STARTED:
            # keep track of start time/frame for later
            rest.tStart = t
            rest.frameNStart = frameN  # exact frame index
            rest.setAutoDraw(True)
        
        # *restResp* updates
        if t >= 0.0 and restResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            restResp.tStart = t
            restResp.frameNStart = frameN  # exact frame index
            restResp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if restResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rest"-------
    for thisComponent in RestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'blockLoop'


# ------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
endKey = event.BuilderKeyResponse()
# keep track of which components have finished
EndComponents = [endText, endKey]
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if t >= 0.0 and endText.status == NOT_STARTED:
        # keep track of start time/frame for later
        endText.tStart = t
        endText.frameNStart = frameN  # exact frame index
        endText.setAutoDraw(True)
    
    # *endKey* updates
    if t >= 0.0 and endKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        endKey.tStart = t
        endKey.frameNStart = frameN  # exact frame index
        endKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if endKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
