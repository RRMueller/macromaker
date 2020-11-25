from pynput import mouse
from pynput.mouse import Button, Controller

input = ""

'''
I have no clue how this works but it works
'''

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    '''
    comment out the next 3 lines to disable turn_off_on_click. Only run in python console or IDLE, not Atom or otherwise. Lags to all hell.
    '''
    # if not pressed:
    # # Stop listener
    #     return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join();
