#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b11),
    on February 12, 2019, at 15:24
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
expName = 'face_task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jscof\\OneDrive\\Desktop\\psychopy_experiment\\face_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instruct_text = visual.TextStim(win=win, name='instruct_text',
    text="Welcome to your experiment!\n\nYou will be asked to complete a facial emotion recognition task.\n\nPress 'c' to continue...",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct2"
instruct2Clock = core.Clock()
instruct2_text = visual.TextStim(win=win, name='instruct2_text',
    text="This is a facial emotion recognition task.\n\nThis task will require you to look at a blurry image of a face. The blurry image will slowly come into focus and you will be asked to press a button when you detect which emotion is displayed by the face. The face will disappear when you press the button. You will then be asked to select which emotion was displayed by the face from a list of emotions.\n\nPress 'c' to continue...",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruct3"
instruct3Clock = core.Clock()
instruct3_text = visual.TextStim(win=win, name='instruct3_text',
    text="You are about to begin the task.\n\nOn the following screen, when you detect which emotion is displayed by the face, please press 'SPACE BAR'. Once you press 'SPACE BAR', the face will disappear and you will be asked to select which emotion was displayed.\n\nTo respond, please press the numeric key associated with the correct responses: 1 = Fear, 2 = Anger, 3 = Happy, 4 = Sad, 5 = Disgust, 6 = Surprise, 7 = Neutral\n\nPress 'SPACE BAR' when you are ready to begin...",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trials"
trialsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="Press 'SPACE BAR' when you recognize the emotion displayed...",
    font='Arial',
    pos=(0, -0.75), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "expression"
expressionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Which emotion ws displayed?\n\n1. Fear\n2. Anger\n3. Happiness\n4. Sadness\n5. Disgust\n6. Surprise\n7. Neutral\n\nPress a number to continue...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Thank you for participating!\n\nYou are now finished.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruct_key = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [instruct_text, instruct_key]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_text* updates
    if t >= 0.0 and instruct_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_text.tStart = t
        instruct_text.frameNStart = frameN  # exact frame index
        instruct_text.setAutoDraw(True)
    
    # *instruct_key* updates
    if t >= 0.0 and instruct_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct_key.tStart = t
        instruct_key.frameNStart = frameN  # exact frame index
        instruct_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instruct_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['c'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instruct_key.keys = theseKeys[-1]  # just the last key pressed
            instruct_key.rt = instruct_key.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruct_key.keys in ['', [], None]:  # No response was made
    instruct_key.keys=None
thisExp.addData('instruct_key.keys',instruct_key.keys)
if instruct_key.keys != None:  # we had a response
    thisExp.addData('instruct_key.rt', instruct_key.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct2"-------
t = 0
instruct2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruct2_key = event.BuilderKeyResponse()
# keep track of which components have finished
instruct2Components = [instruct2_text, instruct2_key]
for thisComponent in instruct2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct2"-------
while continueRoutine:
    # get current time
    t = instruct2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct2_text* updates
    if t >= 0.0 and instruct2_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct2_text.tStart = t
        instruct2_text.frameNStart = frameN  # exact frame index
        instruct2_text.setAutoDraw(True)
    
    # *instruct2_key* updates
    if t >= 0.0 and instruct2_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct2_key.tStart = t
        instruct2_key.frameNStart = frameN  # exact frame index
        instruct2_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct2_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instruct2_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['c'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instruct2_key.keys = theseKeys[-1]  # just the last key pressed
            instruct2_key.rt = instruct2_key.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct2"-------
for thisComponent in instruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruct2_key.keys in ['', [], None]:  # No response was made
    instruct2_key.keys=None
thisExp.addData('instruct2_key.keys',instruct2_key.keys)
if instruct2_key.keys != None:  # we had a response
    thisExp.addData('instruct2_key.rt', instruct2_key.rt)
thisExp.nextEntry()
# the Routine "instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct3"-------
t = 0
instruct3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruct3_key = event.BuilderKeyResponse()
# keep track of which components have finished
instruct3Components = [instruct3_text, instruct3_key]
for thisComponent in instruct3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct3"-------
while continueRoutine:
    # get current time
    t = instruct3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct3_text* updates
    if t >= 0.0 and instruct3_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct3_text.tStart = t
        instruct3_text.frameNStart = frameN  # exact frame index
        instruct3_text.setAutoDraw(True)
    
    # *instruct3_key* updates
    if t >= 0.0 and instruct3_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct3_key.tStart = t
        instruct3_key.frameNStart = frameN  # exact frame index
        instruct3_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct3_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instruct3_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instruct3_key.keys = theseKeys[-1]  # just the last key pressed
            instruct3_key.rt = instruct3_key.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct3"-------
for thisComponent in instruct3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruct3_key.keys in ['', [], None]:  # No response was made
    instruct3_key.keys=None
thisExp.addData('instruct3_key.keys',instruct3_key.keys)
if instruct3_key.keys != None:  # we had a response
    thisExp.addData('instruct3_key.rt', instruct3_key.rt)
thisExp.nextEntry()
# the Routine "instruct3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim_list.csv'),
    seed=None, name='trials_loop')
thisExp.addLoop(trials_loop)  # add the loop to the experiment
thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
if thisTrials_loop != None:
    for paramName in thisTrials_loop:
        exec('{} = thisTrials_loop[paramName]'.format(paramName))

for thisTrials_loop in trials_loop:
    currentLoop = trials_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop:
            exec('{} = thisTrials_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trials"-------
    t = 0
    trialsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    movie = visual.MovieStim3(
        win=win, name='movie',
        noAudio = True,
        filename=vid,
        ori=0, pos=(0, 0), opacity=1,
        size=1500,
        depth=0.0,
        )
    movie_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialsComponents = [movie, movie_key, text_2]
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trials"-------
    while continueRoutine:
        # get current time
        t = trialsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie* updates
        if t >= 0.0 and movie.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie.tStart = t
            movie.frameNStart = frameN  # exact frame index
            movie.setAutoDraw(True)
        
        # *movie_key* updates
        if t >= 0.0 and movie_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie_key.tStart = t
            movie_key.frameNStart = frameN  # exact frame index
            movie_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(movie_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if movie_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                movie_key.keys = theseKeys[-1]  # just the last key pressed
                movie_key.rt = movie_key.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials"-------
    for thisComponent in trialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if movie_key.keys in ['', [], None]:  # No response was made
        movie_key.keys=None
    trials_loop.addData('movie_key.keys',movie_key.keys)
    if movie_key.keys != None:  # we had a response
        trials_loop.addData('movie_key.rt', movie_key.rt)
    # the Routine "trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "expression"-------
    t = 0
    expressionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    expressionComponents = [text, text_key]
    for thisComponent in expressionComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "expression"-------
    while continueRoutine:
        # get current time
        t = expressionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *text_key* updates
        if t >= 0.0 and text_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_key.tStart = t
            text_key.frameNStart = frameN  # exact frame index
            text_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(text_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if text_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5', '6'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                text_key.keys = theseKeys[-1]  # just the last key pressed
                text_key.rt = text_key.clock.getTime()
                # was this 'correct'?
                if (text_key.keys == str(corr)) or (text_key.keys == corr):
                    text_key.corr = 1
                else:
                    text_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expressionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "expression"-------
    for thisComponent in expressionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if text_key.keys in ['', [], None]:  # No response was made
        text_key.keys=None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           text_key.corr = 1;  # correct non-response
        else:
           text_key.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_loop (TrialHandler)
    trials_loop.addData('text_key.keys',text_key.keys)
    trials_loop.addData('text_key.corr', text_key.corr)
    if text_key.keys != None:  # we had a response
        trials_loop.addData('text_key.rt', text_key.rt)
    # the Routine "expression" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_loop'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_text]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if end_text.status == STARTED and t >= frameRemains:
        end_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
