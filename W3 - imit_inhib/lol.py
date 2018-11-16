# LOL

from psychopy import visual, core, data, event, logging, sound, gui
import numpy as np  # whole numpy lib is available, prepend 'np.'
from psychopy.constants import *  # things like STARTED, FINISHED
from numpy.random import random, randint, normal, shuffle
import pandas as pd
import random
from psychopy.iohub import launchHubServer

#number of trials per conditions
TRIALS = 1
practice_trials= 1
#at the very beginning to load the server
io = launchHubServer()
keyboard = io.devices.keyboard

# gui requesting participant info
participant_id = gui.Dlg(title="Imitation-Inhibition Experiment") 
participant_id.addText('Subject Info')
participant_id.addField('Participant:')
participant_id.addField('Condition:', choices = ['II','IT', 'CT'])
participant_id.show()

if participant_id.OK:
    Participant = participant_id.data[0]                     #saves data from dialogue box into the variable 'ID'
else:
    core.quite()
                        

Condition = participant_id.data[1]

#where we will save the data
columnss = ['Participant', 'Condition', 'Congruity', 'Reaction_time', 'Response', 'Correctness', 'Cue','Finger']
indexs = np.arange(0)
DATA = pd.DataFrame(columns=columnss, index = indexs) 

#window where we will show everything
win = visual.Window(fullscr=True, color='black', colorSpace='rgb', units = 'pix', allowStencil=True)

#watch we will use to measure RT
stopwatch = core.Clock()

#list of waiting times from which we will randomly select later
waitingtimes = [0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4]

#function to show instruction texts
def msg(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 20,alignHoriz='center') # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
    win.flip() # flip the screen to reveal the stimulus


################# LOADING ALL THE PICTURES TO MAKE THE FINGER ANIMATIONS ###############

#static hand line
staticHand = visual.ImageStim(win=win, name='staticHand',image='StaticHand.jpg')

#blue blackground
blue = visual.ImageStim(win=win, name='blue',image='blue.jpg')

######Control task, CT###########

#middle finger congruent list
m2con = visual.ImageStim(win=win, name='m2con',image='m2con.jpg')
m3con = visual.ImageStim(win=win, name='m3con',image='m3con.jpg')
m4con = visual.ImageStim(win=win, name='m4con',image='m4con.jpg')
mconlist = [m2con, m3con, m4con]

#middle finger incongruent list
m2icon = visual.ImageStim(win=win, name='m2icon',image='m2inc.jpg')
m3icon = visual.ImageStim(win=win, name='m3icon',image='m3inc.jpg')
m4icon = visual.ImageStim(win=win, name='m4icon',image='m4inc.jpg')
miconlist = [m2icon, m3icon, m4icon]

#index finger congruent list
i2con = visual.ImageStim(win=win, name='i2con',image='i2con.jpg')
i3con = visual.ImageStim(win=win, name='i3con',image='i3con.jpg')
i4con = visual.ImageStim(win=win, name='i4con',image='i4con.jpg')
iconlist = [i2con, i3con, i4con]

#index finger incongruent list
i2icon = visual.ImageStim(win=win, name='i2icon',image='i2inc.jpg')
i3icon = visual.ImageStim(win=win, name='i3icon',image='i3inc.jpg')
i4icon = visual.ImageStim(win=win, name='i4icon',image='i4inc.jpg')
iiconlist = [i2icon, i3icon, i4icon]

#########Imitation inhibition II, Imitation trainin IT, numberless########

#Index finger numberless
i2Numberless = visual.ImageStim(win=win, name='i2Numberless',image='i2Numberless.jpg')
i3Numberless = visual.ImageStim(win=win, name='i3Numberless',image='i3Numberless.jpg')
i4Numberless = visual.ImageStim(win=win, name='i4Numberless',image='i4Numberless.jpg')
iNumberlesslist = [i2Numberless, i3Numberless, i4Numberless]

#Middle finger numberless
m2Numberless = visual.ImageStim(win=win, name='m2Numberless',image='m2Numberless.jpg')
m3Numberless = visual.ImageStim(win=win, name='m3Numberless',image='m3Numberless.jpg')
m4Numberless = visual.ImageStim(win=win, name='m4Numberless',image='m4Numberless.jpg')
mNumberlesslist = [m2Numberless, m3Numberless, m4Numberless]


################################# MAKING VIDEOS ######################################################
### Here we create four functions; each function is the video made with the pictures we have of the fingers moving. 


#video function for index finger congruent. 
def icon():
    trial_start=core.getTime()
    number = random.choice(waitingtimes)
    staticHand.draw()
    win.flip()
    core.wait(number)
    for i in range(len(iconlist)):
        iconlist[i].draw()
        win.flip()
        if i != 2:
            core.wait(0.34)
        else:
            core.wait(0.5)
    key = keyboard.waitForReleases(keys = ['lcmd','lalt'])
    while str(keyboard.state.keys()) != str(['lalt','lcmd']) and str(keyboard.state.keys()) != str(['lcmd','lalt']):
        print(keyboard.state.keys())
        core.wait(0.1)
    blue.draw()
    win.flip()
    core.wait(0.5)
    RT= key[0].time - number - trial_start
    Congruity = 'Yes'
    cue = 'Index'
    finger= 'Index'
    Response = key[0].key
    if key[0].key == 'lalt':
        correctness = 0
    else:
        correctness = 1
    return(key,Congruity,RT,Response,correctness,cue, finger)



#video function for index finger incongruent. 
def iicon():
    trial_start=core.getTime()
    number = random.choice(waitingtimes)
    staticHand.draw()
    win.flip()
    core.wait(number)
    for i in range(len(iiconlist)):
        iiconlist[i].draw()
        win.flip()
        if i != 2:
            core.wait(0.34)
        else:
            core.wait(0.5)
    key = keyboard.waitForReleases(keys = ['lcmd','lalt'])
    while str(keyboard.state.keys()) != str(['lalt','lcmd']) and str(keyboard.state.keys()) != str(['lcmd','lalt']):
        core.wait(0.1)
    blue.draw()
    win.flip()
    core.wait(0.5)
    RT= key[0].time - number - trial_start
    Congruity = 'No'
    cue = 'Middle'
    finger = 'Index'
    Response = key[0].key
    if key[0].key == 'lcmd':
        correctness = 0
    else:
        correctness = 1
    return(key,Congruity,RT,Response,correctness,cue, finger)



    
#video function middle finger congruent
def mcon():
    trial_start=core.getTime()
    stopwatch.reset()
    number = random.choice(waitingtimes)
    staticHand.draw()
    win.flip()
    core.wait(number)
    for i in range(len(mconlist)):
        mconlist[i].draw()
        win.flip()
        if i != 2:
            core.wait(0.34)
        else:
            core.wait(0.5)
    key = keyboard.waitForReleases(keys = ['lcmd','lalt'])
    while str(keyboard.state.keys()) != str(['lalt','lcmd']) and str(keyboard.state.keys()) != str(['lcmd','lalt']):
        print(keyboard.state.keys())
        core.wait(0.1)
    blue.draw()
    win.flip()
    core.wait(0.5)
    RT= key[0].time - number - trial_start
    Congruity = 'Yes'
    cue = 'Middle'
    finger='Middle'
    Response = key[0].key
    if key[0].key == 'lcmd':
        correctness = 0
    else:
        correctness = 1
    return(key,Congruity,RT,Response,correctness,cue, finger)


    
#video function middle finger incongruent
def micon():
    trial_start=core.getTime()
    stopwatch.reset()
    number = random.choice(waitingtimes)
    staticHand.draw()
    win.flip()
    core.wait(number)
    for i in range(len(miconlist)):
        miconlist[i].draw()
        win.flip()
        if i != 2:
            core.wait(0.34)
        else:
            core.wait(0.5)
    key = keyboard.waitForReleases(keys = ['lcmd','lalt'])
    while str(keyboard.state.keys()) != str(['lalt','lcmd']) and str(keyboard.state.keys()) != str(['lcmd','lalt']):
        print(keyboard.state.keys())
        core.wait(0.1)
    blue.draw()
    win.flip()
    core.wait(0.5)
    RT= key[0].time - number - trial_start
    Congruity = 'No'
    cue = 'Index'
    finger='Middle'
    Response = key[0].key
    if key[0].key == 'lcmd':
        correctness = 1
    else:
        correctness = 0
    return(key,Congruity,RT,Response,correctness,cue, finger)

######### NUMBERLESS INDEX FINGER #############
#video for numberless index finger
def iNumberless():
    trial_start=core.getTime()
    number = random.choice(waitingtimes)
    staticHand.draw()
    win.flip()
    core.wait(number)
    for i in range(len(iNumberlesslist)):
        iNumberlesslist[i].draw()
        win.flip()
        if i != 2:
            core.wait(0.34)
        else:
            core.wait(0.5)
    key = keyboard.waitForReleases(keys = ['lcmd','lalt'])
    while str(keyboard.state.keys()) != str(['lalt','lcmd']) and str(keyboard.state.keys()) != str(['lcmd','lalt']):
        print(keyboard.state.keys())
        core.wait(0.1)
    blue.draw()
    win.flip()
    core.wait(0.5)
    RT= key[0].time - number - trial_start
    Congruity = 'Yes'
    cue = 'None'
    finger = 'Index'
    Response = key[0].key
    if key[0].key == 'lalt':
        correctness = 0
    else:
        correctness = 1
    return(key,Congruity,RT,Response,correctness,cue, finger)



#video for numberless middle finger
def mNumberless():
    trial_start=core.getTime()
    number = random.choice(waitingtimes)
    staticHand.draw()
    win.flip()
    core.wait(number)
    for i in range(len(mNumberlesslist)):
        mNumberlesslist[i].draw()
        win.flip()
        if i != 2:
            core.wait(0.34)
        else:
            core.wait(0.5)
    key = keyboard.waitForReleases(keys = ['lcmd','lalt'])
    while str(keyboard.state.keys()) != str(['lalt','lcmd']) and str(keyboard.state.keys()) != str(['lcmd','lalt']):
        print(keyboard.state.keys())
        core.wait(0.1)
    blue.draw()
    win.flip()
    core.wait(0.5)
    RT= key[0].time - number - trial_start
    Congruity = 'Yes'
    cue = 'None'
    finger = 'Middle'
    Response = key[0].key
    if key[0].key == 'lalt':
        correctness = 1
    else:
        correctness = 0
    return(key,Congruity,RT,Response,correctness,cue, finger)



II_instructions ='''
Welcome to this experiment.\n\nYou will be holding down the Cmd/Windows and Alt keys on the left side of the keyboard with your \
middle and index fingers respectively throughout this task.\n\nIn each trial you will see a hand lifting either the index or the middle finger. When you see activation in the index finger of the hand, lift your middle finger \
as quickly as possible.\n\nWhen you see activation in the middle finger of the hand, lift your index finger as quickly as possible. \
Regardless of the response, return to holding down both Cmd/Windows and Alt/Option after each lifting movement.\n\nYou will first have a few practice trials. \
Afterwards, the experiment will being.\n\n Position your left index and middle fingers on the left Cmd/Windows and Alt buttons respectively.\n\n When you are ready press \
the spacebar to begin the set of practice trials.
'''



IT_instructions ='''
Welcome to this experiment.\n\nYou will be holding down the Cmd/Windows and Alt keys on the left side of the keyboard with your \
middle and index fingers respectively throughout this task.\n\nIn each trial you will see a hand lifting either the index or the middle finger. When you see activation in the index finger of the hand, lift your index finger \
as quickly as possible.\n\nWhen you see activation in the middle finger of the hand, lift your middle finger as quickly as possible. \
Regardless of the response, return to holding down both Cmd/Windows and Alt/Option after each lifting movement.\n\nYou will first have a few practice trials. \
Afterwards, the experiment will being.\n\n Position your left index and middle fingers on the left Cmd/Windows and Alt buttons respectively.\n\n When you are ready press \
the spacebar to begin the set of practice trials.
'''


CT_instructions ='''
Welcome to this experiment.\n\nYou will be holding down the Cmd/Windows and Alt keys on the left side of the keyboard with your \
middle and index fingers respectively throughout this task.\n\nWhen the number "1" appears, lift your index finger \
as quickly as possible.\n\nWhen the number "2" appears, lift your middle finger as quickly as possible. \
Regardless of the response, return to holding down both Cmd/Windows and Alt/Option after each lifting movement.\n\nYou will first have a few practice trials. \
Afterwards, the experiment will being.\n\n Position your left index and middle fingers on the left Cmd/Windows and Alt buttons respectively.\n\n When you are ready press \
the spacebar to begin the set of practice trials.
'''

#list with the functions of the videos used according to the condition and choice of instruction
if Condition == 'II':
    function_list = [iNumberless, mNumberless]
    #show instructions till they press space
    msg(II_instructions)
    event.waitKeys(keyList = 'space')
    
elif Condition == 'IT':
    function_list = [iNumberless, mNumberless]
    #show instructions till they press space
    msg(IT_instructions)
    event.waitKeys(keyList = 'space')
    
elif Condition == 'CT' :
    function_list = [iicon,icon,micon,mcon]
    #show instructions till they press space
    msg(CT_instructions)
    event.waitKeys(keyList = 'space')

#practice loop with practice_trials (defined in the beginning) trials. Each video appears practice_trials times. DATA IS NOT SAVED
for t in range(practice_trials):#
    #each time, we randomize the order of the videos, therefore, it is impossible for the same video to appear twice in a row. 
    random_functions = np.random.permutation(function_list)
    for o in range(len(function_list)):
        #do the function
        key,Congruity,RT,Response,correctness,cue,finger = random_functions[o]()

msg('You have completed all practice trials.\n\nPlease make sure to have your fingers on the buttons and press SPACE to move on to the experiment')
event.waitKeys(keyList = 'space')

#for loop with TRIALS (defined in the beginning) trials. Each video appears TRIALS times. data is saved
for t in range(TRIALS):#
    key = event.getKeys()
    
    if key=='escape':
        break
    #each time, we randomize the order of the videos, therefore, it is impossible for the same video to appear twice in a  row. 
    random_functions = np.random.permutation(function_list)
    for w in range(len(function_list)):
        #do the function
        key,Congruity,RT,Response,correctness,cue,finger = random_functions[w]()
        #append trial data to pandas
        DATA = DATA.append({
            'Participant': Participant,
            'Condition': Condition,
            'Congruity': Congruity,
            'Reaction_time':RT,
            'Response': Response,
            'Correctness': correctness,
            'Cue':cue,
            'Finger':finger}, ignore_index=True)
    DATA.to_csv('data/II_'+Participant+'.csv')
msg('You are now done with the experiment :-) Please press SPACE')
event.waitKeys(keyList = 'space')
#save to csv file - put this in the end of the script 
DATA.to_csv('data/II_'+Participant+'.csv')