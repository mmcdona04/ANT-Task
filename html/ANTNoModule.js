/************ 
 * Ant Test *
 ************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'ANT';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(PracInstrucRoutineBegin);
flowScheduler.add(PracInstrucRoutineEachFrame);
flowScheduler.add(PracInstrucRoutineEnd);
flowScheduler.add(PracInstruct2RoutineBegin);
flowScheduler.add(PracInstruct2RoutineEachFrame);
flowScheduler.add(PracInstruct2RoutineEnd);
const pracLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(pracLoopLoopBegin, pracLoopLoopScheduler);
flowScheduler.add(pracLoopLoopScheduler);
flowScheduler.add(pracLoopLoopEnd);
flowScheduler.add(MainInstrucRoutineBegin);
flowScheduler.add(MainInstrucRoutineEachFrame);
flowScheduler.add(MainInstrucRoutineEnd);
const blockLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blockLoopLoopBegin, blockLoopLoopScheduler);
flowScheduler.add(blockLoopLoopScheduler);
flowScheduler.add(blockLoopLoopEnd);
flowScheduler.add(EndRoutineBegin);
flowScheduler.add(EndRoutineEachFrame);
flowScheduler.add(EndRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.1.3';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var PracInstrucClock;
var pracText1;
var PracInstruct2Clock;
var practInst2;
var fixationClock;
var image;
var trialClock;
var cues;
var target;
var fixationshort;
var feedbackClock;
var text;
var MainInstrucClock;
var mainInst;
var RestClock;
var rest;
var EndClock;
var endText;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "PracInstruc"
  PracInstrucClock = new util.Clock();
  pracText1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'pracText1',
    text: 'Welcome to this experiment.\n\nIn this task, you will be presented with a central arrow surrounded by arrows or blocks. The central arrow will point left or right.\n\nSometimes the flanking arrows will be pointing in the same direction as the central arrow, and sometimes the flanking arrows will point in the oppoiste direction to the central arrow.\n\neg. >>>>> or >><>>\n\nYour task is to respond to the direction of the central arrow.\n\nIf the central arrow points to the right, press the right arrow key and if the arrow points to the left, press the left arrow key.\n\nPress the space bar to continue.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PracInstruct2"
  PracInstruct2Clock = new util.Clock();
  practInst2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'practInst2',
    text: 'In this task, you must respond to the direction of the centre arrow using the arrow keys.\n\nFirst, a fixation cross will appear in the centre of the screen. The fixation is sometimes followed by blocks on the screen, which may or may not\ncue the location of the target stimulus. If the blocks appear after the fixation, it means that the target will appear shortly.\n\nIf the blocks appears either above OR below the fixation cross, the target will shortly appear in that cued location.\n\nFirst there will be a practice trial, where you will recieve feedback and reaction times for each correct response.\n\nPlace your index fingers on the left and right keys ready to start, and press the spacebar to proceed.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'height', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  cues = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cues', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : 'height', 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  fixationshort = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationshort', units : 'height', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: ' ',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "MainInstruc"
  MainInstrucClock = new util.Clock();
  mainInst = new visual.TextStim({
    win: psychoJS.window,
    name: 'mainInst',
    text: 'That is the end of the practice trials.\n\nThe main trials will now begin. There will be 3 blocks of trials, with a rest period between each one. \n\nThe main trials involve the same instructions as before, however, you will not receive feedback on your responses.\n\nPress the spacebar to continue.',
    font: 'Arial',
    units : 'height', 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'height', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  cues = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cues', units : 'height', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : 'height', 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  fixationshort = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fixationshort', units : 'height', 
    image : 'stim/fix.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "Rest"
  RestClock = new util.Clock();
  rest = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest',
    text: 'You have completed a block of main trials.\n\nHave a short rest as required, and press the space bar to continue to the next block of trials when you are ready.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  endText = new visual.TextStim({
    win: psychoJS.window,
    name: 'endText',
    text: 'That is the end of the main trial. \n\nThank you for taking part in this experiment.\n\nPress any key to exit.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var pracResp1;
var PracInstrucComponents;
function PracInstrucRoutineBegin() {
  //------Prepare to start Routine 'PracInstruc'-------
  t = 0;
  PracInstrucClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  pracResp1 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  PracInstrucComponents = [];
  PracInstrucComponents.push(pracText1);
  PracInstrucComponents.push(pracResp1);
  
  PracInstrucComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function PracInstrucRoutineEachFrame() {
  //------Loop for each frame of Routine 'PracInstruc'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = PracInstrucClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *pracText1* updates
  if (t >= 0.0 && pracText1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pracText1.tStart = t;  // (not accounting for frame time here)
    pracText1.frameNStart = frameN;  // exact frame index
    pracText1.setAutoDraw(true);
  }

  
  // *pracResp1* updates
  if (t >= 0.0 && pracResp1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    pracResp1.tStart = t;  // (not accounting for frame time here)
    pracResp1.frameNStart = frameN;  // exact frame index
    pracResp1.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (pracResp1.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  PracInstrucComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function PracInstrucRoutineEnd() {
  //------Ending Routine 'PracInstruc'-------
  PracInstrucComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "PracInstruc" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var practResp2;
var PracInstruct2Components;
function PracInstruct2RoutineBegin() {
  //------Prepare to start Routine 'PracInstruct2'-------
  t = 0;
  PracInstruct2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  practResp2 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  PracInstruct2Components = [];
  PracInstruct2Components.push(practInst2);
  PracInstruct2Components.push(practResp2);
  
  PracInstruct2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function PracInstruct2RoutineEachFrame() {
  //------Loop for each frame of Routine 'PracInstruct2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = PracInstruct2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *practInst2* updates
  if (t >= 0.0 && practInst2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    practInst2.tStart = t;  // (not accounting for frame time here)
    practInst2.frameNStart = frameN;  // exact frame index
    practInst2.setAutoDraw(true);
  }

  
  // *practResp2* updates
  if (t >= 0.0 && practResp2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    practResp2.tStart = t;  // (not accounting for frame time here)
    practResp2.frameNStart = frameN;  // exact frame index
    practResp2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (practResp2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  PracInstruct2Components.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function PracInstruct2RoutineEnd() {
  //------Ending Routine 'PracInstruct2'-------
  PracInstruct2Components.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "PracInstruct2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var pracLoop;
var currentLoop;
var trialIterator;
function pracLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  pracLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'cond.xlsx', '0:24'),
    seed: undefined, name: 'pracLoop'});
  psychoJS.experiment.addLoop(pracLoop); // add the loop to the experiment
  currentLoop = pracLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = pracLoop[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisPracLoop = result.value;
    thisScheduler.add(importConditions(pracLoop));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(feedbackRoutineBegin);
    thisScheduler.add(feedbackRoutineEachFrame);
    thisScheduler.add(feedbackRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisPracLoop));
  }

  return Scheduler.Event.NEXT;
}


function pracLoopLoopEnd() {
  psychoJS.experiment.removeLoop(pracLoop);

  return Scheduler.Event.NEXT;
}

var blockLoop;
function blockLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  blockLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 3, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'blockLoop'});
  psychoJS.experiment.addLoop(blockLoop); // add the loop to the experiment
  currentLoop = blockLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = blockLoop[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisBlockLoop = result.value;
    thisScheduler.add(importConditions(blockLoop));
    const mainLoopLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(mainLoopLoopBegin, mainLoopLoopScheduler);
    thisScheduler.add(mainLoopLoopScheduler);
    thisScheduler.add(mainLoopLoopEnd);
    thisScheduler.add(RestRoutineBegin);
    thisScheduler.add(RestRoutineEachFrame);
    thisScheduler.add(RestRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisBlockLoop));
  }

  return Scheduler.Event.NEXT;
}

var mainLoop;
function mainLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  mainLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 2, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'cond.xlsx',
    seed: undefined, name: 'mainLoop'});
  psychoJS.experiment.addLoop(mainLoop); // add the loop to the experiment
  currentLoop = mainLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialIterator = mainLoop[Symbol.iterator]();
  while(true) {
    let result = trialIterator.next();
    if (result.done);
      break;
    let thisMainLoop = result.value;
    thisScheduler.add(importConditions(mainLoop));
    thisScheduler.add(fixationRoutineBegin);
    thisScheduler.add(fixationRoutineEachFrame);
    thisScheduler.add(fixationRoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisMainLoop));
  }

  return Scheduler.Event.NEXT;
}


function mainLoopLoopEnd() {
  psychoJS.experiment.removeLoop(mainLoop);

  return Scheduler.Event.NEXT;
}


function blockLoopLoopEnd() {
  psychoJS.experiment.removeLoop(blockLoop);

  return Scheduler.Event.NEXT;
}

var fixDuration;
var durations;
var i;
var step;
var fixationComponents;
function fixationRoutineBegin() {
  //------Prepare to start Routine 'fixation'-------
  t = 0;
  fixationClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  fixDuration  = .4;
  durations = [];
  i=.4;
  step = .05;
  
  function shuffle(a) {
      for (let i = a.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [a[i], a[j]] = [a[j], a[i]];
      }
      return a;
  }
  
  while(i<=1.6) {
      durations.push(i)
      i = i + step;
  }
  
  durations = shuffle(durations);
  fixDuration  = durations[0]; // Take one of the randomized durations
  
  // keep track of which components have finished
  fixationComponents = [];
  fixationComponents.push(image);
  
  fixationComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function fixationRoutineEachFrame() {
  //------Loop for each frame of Routine 'fixation'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = fixationClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  if (t>= fixDuration) {
      continueRoutine = false;}
  
  // *image* updates
  if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  fixationComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function fixationRoutineEnd() {
  //------Ending Routine 'fixation'-------
  fixationComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData("fixDuration", fixDuration);
  // the Routine "fixation" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.200000);
  // update component parameters for each repeat
  cues.setImage(cue);
  target.setOri(targOrientation);
  target.setImage(tar);
  resp = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(cues);
  trialComponents.push(target);
  trialComponents.push(resp);
  trialComponents.push(fixationshort);
  
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cues* updates
  if (t >= 0 && cues.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cues.tStart = t;  // (not accounting for frame time here)
    cues.frameNStart = frameN;  // exact frame index
    cues.setAutoDraw(true);
  }

  frameRemains = 0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cues.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cues.setAutoDraw(false);
  }
  
  // *target* updates
  if (t >= 0.5 && target.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    target.tStart = t;  // (not accounting for frame time here)
    target.frameNStart = frameN;  // exact frame index
    target.setAutoDraw(true);
  }

  frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    target.setAutoDraw(false);
  }
  
  // *resp* updates
  if (t >= 0.5 && resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp.tStart = t;  // (not accounting for frame time here)
    resp.frameNStart = frameN;  // exact frame index
    resp.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    resp.status = PsychoJS.Status.FINISHED;
  }

  if (resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['left', 'right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (resp.keys.length === 0) {  // then this was the first keypress
        resp.keys = theseKeys[0];  // just the first key pressed
        resp.rt = resp.clock.getTime();
        // was this 'correct'?
        if (resp.keys == corrAns) {
            resp.corr = 1;
        } else {
            resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *fixationshort* updates
  if (t >= 0.0 && fixationshort.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fixationshort.tStart = t;  // (not accounting for frame time here)
    fixationshort.frameNStart = frameN;  // exact frame index
    fixationshort.setAutoDraw(true);
  }

  frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (fixationshort.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    fixationshort.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  trialComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  trialComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  
  // check responses
  if (resp.keys === undefined || resp.keys.length === 0) {    // No response was made
      resp.keys = undefined;
  }
  
  // was no response the correct answer?!
  if (resp.keys === undefined) {
    if (['None','none',undefined].includes(corrAns)) {
       resp.corr = 1  // correct non-response
    } else {
       resp.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('resp.keys', resp.keys);
  psychoJS.experiment.addData('resp.corr', resp.corr);
  if (typeof resp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp.rt', resp.rt);
      routineTimer.reset();
      }
  
  return Scheduler.Event.NEXT;
}

var msg;
var feedbackComponents;
function feedbackRoutineBegin() {
  //------Prepare to start Routine 'feedback'-------
  t = 0;
  feedbackClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  var msg = '';
  
  if (resp.corr){
      msg="Correct! RT=" + resp.rt.toFixed(3);
  } else {
      msg = "Incorrect!";
  }
      
  text.setText(msg);
  // keep track of which components have finished
  feedbackComponents = [];
  feedbackComponents.push(text);
  
  feedbackComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function feedbackRoutineEachFrame() {
  //------Loop for each frame of Routine 'feedback'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = feedbackClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  feedbackComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEnd() {
  //------Ending Routine 'feedback'-------
  feedbackComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  return Scheduler.Event.NEXT;
}

var instResp;
var MainInstrucComponents;
function MainInstrucRoutineBegin() {
  //------Prepare to start Routine 'MainInstruc'-------
  t = 0;
  MainInstrucClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instResp = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  MainInstrucComponents = [];
  MainInstrucComponents.push(mainInst);
  MainInstrucComponents.push(instResp);
  
  MainInstrucComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function MainInstrucRoutineEachFrame() {
  //------Loop for each frame of Routine 'MainInstruc'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = MainInstrucClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *mainInst* updates
  if (t >= 0.0 && mainInst.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mainInst.tStart = t;  // (not accounting for frame time here)
    mainInst.frameNStart = frameN;  // exact frame index
    mainInst.setAutoDraw(true);
  }

  
  // *instResp* updates
  if (t >= 0.0 && instResp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instResp.tStart = t;  // (not accounting for frame time here)
    instResp.frameNStart = frameN;  // exact frame index
    instResp.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instResp.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (instResp.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      instResp.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      instResp.rt = instResp.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  MainInstrucComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function MainInstrucRoutineEnd() {
  //------Ending Routine 'MainInstruc'-------
  MainInstrucComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  
  // check responses
  if (instResp.keys === undefined || instResp.keys.length === 0) {    // No response was made
      instResp.keys = undefined;
  }
  
  psychoJS.experiment.addData('instResp.keys', instResp.keys);
  if (typeof instResp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('instResp.rt', instResp.rt);
      routineTimer.reset();
      }
  
  // the Routine "MainInstruc" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var restResp;
var RestComponents;
function RestRoutineBegin() {
  //------Prepare to start Routine 'Rest'-------
  t = 0;
  RestClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  restResp = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  RestComponents = [];
  RestComponents.push(rest);
  RestComponents.push(restResp);
  
  RestComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function RestRoutineEachFrame() {
  //------Loop for each frame of Routine 'Rest'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = RestClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *rest* updates
  if (t >= 0.0 && rest.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    rest.tStart = t;  // (not accounting for frame time here)
    rest.frameNStart = frameN;  // exact frame index
    rest.setAutoDraw(true);
  }

  
  // *restResp* updates
  if (t >= 0.0 && restResp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    restResp.tStart = t;  // (not accounting for frame time here)
    restResp.frameNStart = frameN;  // exact frame index
    restResp.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (restResp.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  RestComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function RestRoutineEnd() {
  //------Ending Routine 'Rest'-------
  RestComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "Rest" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endKey;
var EndComponents;
function EndRoutineBegin() {
  //------Prepare to start Routine 'End'-------
  t = 0;
  EndClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  endKey = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  EndComponents = [];
  EndComponents.push(endText);
  EndComponents.push(endKey);
  
  EndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}


function EndRoutineEachFrame() {
  //------Loop for each frame of Routine 'End'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = EndClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *endText* updates
  if (t >= 0.0 && endText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    endText.tStart = t;  // (not accounting for frame time here)
    endText.frameNStart = frameN;  // exact frame index
    endText.setAutoDraw(true);
  }

  
  // *endKey* updates
  if (t >= 0.0 && endKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    endKey.tStart = t;  // (not accounting for frame time here)
    endKey.frameNStart = frameN;  // exact frame index
    endKey.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (endKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['y', 'n', 'left', 'right', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  EndComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEnd() {
  //------Ending Routine 'End'-------
  EndComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // the Routine "End" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisScheduler, thisTrial) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
