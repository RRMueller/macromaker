from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import logging
import keyboard
import time
import pyperclip
import csv

'''
This general purpose script is meant to help speed up the repetitiveness of everyday tasks. It operates in the background allowing you to have any amount of windows stacked on top of it while still allowing it to operate. The delays are necessary but not optimal due to how fast the programs this script is interacting with can operate.

Controls:
↑               -- Activates up_arrow() function
↓               -- Activates down_arrow() function
→               -- Activates right_arrow() function
←               -- Activates left_arrow() function
"esc"           -- exits the program

Code:
mouse.position = (x, y)                                             # Move to position (x,y)
mouse.press(Button.side)                                            # Presses mouse button <side>
mouse.release(Button.side)                                          # Releases mouse button <side>
mouse.scroll(x, y)                                                  # Scroll x and y times
keyboard.send('ctrl, c, up, down, left, right, shift, esc, etc.')   # Sends keyboard command combo
keyboard.write('string of text')                                    # Type a string of text
data = pyperclip.paste()                                            # Copies the clipboard to variable data
time.sleep(20)                                                      # Pause for 20 seconds
time.perfcounter()                                                  # The current time, useful for time/iteration analysis
'''

loop_count=1
buttons = {"left": Button.left, "right": Button.right}
FastTimeDelay=0.25
SlowTimeDelay=0.5

# TO THE IDIOT THAT WANT'S TO CUSTOMIZE THE KEY BEING PRESSED - DO IT HERE
#############################################################################
startRepeatingKey1A = "ctrl" # HOW TO START REPEATING repeatedKey1
startRepeatingKey1B = "1"    # HOW TO START REPEATING repeatedKey1
repeatedKey1 = "enter" # CTRL + 1
sleepTime1 = 1 # (s) HOW LONG TO WAIT BETWEEN KEY PRESSES FOR repeatedKey1

startRepeatingKey2A = "ctrl" # HOW TO START REPEATING repeatedKey2
startRepeatingKey2B = "2"    # HOW TO START REPEATING repeatedKey2
repeatedKey2 = "e" # CTRL + 2
sleepTime2 = 1 # (s) HOW LONG TO WAIT BETWEEN KEY PRESSES FOR repeatedKey1

stopRepeatingKeyA = "ctrl" # HOW TO STOP REPEATING ANY REPEATED KEYS
stopRepeatingKeyB = "3"    # HOW TO STOP REPEATING ANY REPEATED KEYS

exitProgramKeyA = "ctrl"   # HOW TO STOP PROGRAM COMPLETELY
exitProgramKeyB = "4"      # HOW TO STOP PROGRAM COMPLETELY
#############################################################################

#Clicks a location, copies, clicks another location, pastes

def click_drag_and_release(xpos1, ypos1, xpos2, ypos2, side="left"):
    mouse = Controller()
    mouse.position = (xpos1, ypos1)
    mouse.press(buttons[side])
    mouse.position = (xpos2, ypos2)
    mouse.release(buttons[side])

# Clicks a location twice
def double_click(x, y, side="left"):
    mouse = Controller()
    mouse.position = (x, y)
    mouse.press(buttons[side])
    time.sleep(0.1)
    mouse.release(buttons[side])
    mouse.position = (x, y)
    mouse.press(buttons[side])
    time.sleep(0.1)
    mouse.release(buttons[side])
    
def copy_paste(xpos1, ypos1, xpos2, ypos2):
    mouse = Controller()
    click(xpos1, ypos1, left)
    keyboard.send('ctrl+c')
    time.sleep(FastTimeDelay)
    click(xpos2, ypos2, right)
    keyboard.send('ctrl+v')

#Clicks a location
def click(x, y, side="left"):
    mouse = Controller()
    mouse.position = (x, y)
    mouse.press(buttons[side])
    time.sleep(FastTimeDelay)
    mouse.release(buttons[side])

#Saves
def save():
    keyboard.send("ctrl+s")

#Copies
def copy():
    keyboard.send("ctrl+c")

#Pastes
def paste():
    keyboard.send("ctrl+v")

#Goes left 1 page
def page_left():
    click(440, 60)

#Goes Right 1 page
def page_right():
    click(460, 60)

#Activates when ↑ is pressed
def n_function():
    print('N key pressed')
    time.sleep(0.25)
    mouse = Controller()

    x_start = -15500
    x_end = 20000

    z_start = 20000
    z_end = 0

    keyboard.send("t")
    time.sleep(0.25)
    keyboard.write("/tp digbic {} 900 {}".format(x_start, z_start))
    keyboard.send("enter")

    while z_end <= z_start:
        while x_end >= x_start:
            x_start+=1500
            keyboard.send("t")
            time.sleep(0.25)
            keyboard.write("/tp digbic {} 900 {}".format(x_start, z_start))
            time.sleep(300)
            keyboard.send("enter")
            time.sleep(0.25)
        z_start-= 1500
        x_start= -20000

    keyboard.send("t")
    time.sleep(0.25)
    keyboard.write("/tp digbic {} 100 {}".format(x_start, z_start))
    keyboard.send("enter")
    

def get_input():
    keyboard.get_typed_strings(2, allow_backspace=True)
#Continuous loop that listens for keyboard input
while True:
    try:
        time.sleep(0.01) # SHIT GETS LAGGY WHEN WE DON'T PUT A DELAY HERE
        #Up Arrow
        if keyboard.is_pressed(startRepeatingKey1A) and keyboard.is_pressed(startRepeatingKey1B):
            while True:
                keyboard.send(repeatedKey1)
                time.sleep(sleepTime1)
                if keyboard.is_pressed(stopRepeatingKeyA) and keyboard.is_pressed(stopRepeatingKeyB):
                  break
            print("-----------------------------------")
        if keyboard.is_pressed(startRepeatingKey2A) and keyboard.is_pressed(startRepeatingKey2B):
            while True:
                keyboard.send(repeatedKey2)
                time.sleep(sleepTime2)
                if keyboard.is_pressed(stopRepeatingKeyA) and keyboard.is_pressed(stopRepeatingKeyB):
                  break
#             print("-----------------------------------")



        elif keyboard.is_pressed(exitProgramKeyA) and keyboard.is_pressed(exitProgramKeyB):
            break
    except:
        pass
