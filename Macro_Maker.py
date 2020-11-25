from pynput.mouse import Button, Controller
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
def up_arrow():
    print('Up key pressed')
    time.sleep(0.25)
    mouse = Controller()
    global left_current_part
    global right_current_part

#Activates when ↓ is pressed
def down_arrow():
    print("Down key pressed")
    time.sleep(0.25)
    mouse = Controller()
    global left_current_part
    global right_current_part

#Activates when ← is pressed
def left_arrow():
    print('Left key pressed')
    time.sleep(0.25)
    mouse = Controller()
    global left_current_part
    global right_current_part

#Activates when → is pressed
def right_arrow():
    print('Right key pressed')
    time.sleep(0.25)
    mouse = Controller()
    global left_current_part
    global right_current_part

#Continuous loop that listens for keyboard input
while True:
    try:
        #Up Arrow
        if keyboard.is_pressed('up'):
            start_time = time.perf_counter()
            if loop_count > 1:
                for i in range(loop_count):
                    up_arrow()
                    elapsed_time = time.perf_counter() - start_time
                    print(i + 1)
                    print(elapsed_time)
                    print("-----------------------------------")
                break
            if loop_count == 1:
                up_arrow()
                elapsed_time = time.perf_counter() - start_time
                print(elapsed_time)
            print("-----------------------------------")

        #Down Arrow
        elif keyboard.is_pressed('down'):
            start_time = time.perf_counter()
            if loop_count > 1:
                for i in range(loop_count):
                    down_arrow()
                    elapsed_time = time.perf_counter() - start_time
                    print(i + 1)
                    print(elapsed_time)
                    print("-----------------------------------")
                break
            if loop_count == 1:
                down_arrow()
                elapsed_time = time.perf_counter() - start_time
                print(elapsed_time)
            print("-----------------------------------")

        #Left Arrow
        elif keyboard.is_pressed('left'):
            start_time = time.perf_counter()
            if loop_count > 1:
                for i in range(loop_count):
                    left_arrow()
                    elapsed_time = time.perf_counter() - start_time
                    print(i + 1)
                    print(elapsed_time)
                    print("-----------------------------------")
                break
            if loop_count == 1:
                left_arrow()
                elapsed_time = time.perf_counter() - start_time
                print(elapsed_time)
            print("-----------------------------------")

        #Right Arrow
        elif keyboard.is_pressed('right'):
            start_time = time.perf_counter()
            if loop_count > 1:
                for i in range(loop_count):
                    right_arrow()
                    elapsed_time = time.perf_counter() - start_time
                    print(i + 1)
                    print(elapsed_time)
                    print("-----------------------------------")
                break
            if loop_count == 1:
                right_arrow()
                elapsed_time = time.perf_counter() - start_time
                print(elapsed_time)
            print("-----------------------------------")

        elif keyboard.is_pressed('esc'):
            break
    except:
        pass
