from pynput import keyboard, mouse
from pynput.keyboard import Listener, Key

record_key = Key.ctrl_l
recording = False
recorded_events = []

def on_press(key):
    global recording

    if key == record_key:
        if not recording:
            recording = True
            recorded_events.append(('start', mouse.Controller().position))
        else:
             # temporary, to see what is going on
             for x in recorded_events:
                print(x, end="\n")
          
    elif key != record_key and recording: 
          recorded_events.append(('key', key))

def on_click(x, y, button, pressed):
      if pressed and recording:
            recorded_events.append(('click', (x, y, button)))

def on_move(x, y):
     if recording:
          recorded_events.append(('move', (x, y)))

def on_scroll(x, y, dx, dy):
     if recording:
          recorded_events.append(('scroll', (x, y, dx, dy)))


keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move)

keyboard_listener.start()
mouse_listener.start()

try:
    keyboard_listener.join()
    mouse_listener.join()
except KeyboardInterrupt:
    pass