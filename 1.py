import pydirectinput
import threading
import time
from pynput import keyboard
from clc99 import *

stop_flag = False

def on_press(key):
    global stop_flag
    try:
        if key.char == 'q':
            stop_flag = True
            return False
    except AttributeError:
        pass

def listen_keyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def move_mouse_right():
    pydirectinput.PAUSE = 0.01
    print_status("按下 'q' 停止程序，卡琳爽！")
    pydirectinput.mouseDown(button='left')
    
    while not stop_flag:
        for i in range(30): 
            if stop_flag:
                break
            pydirectinput.moveRel(150, 0, relative=True)
            time.sleep(0.005)
        pydirectinput.moveRel(0, 10, relative=True)
    pydirectinput.mouseUp(button='left')

print_good("欢迎来到99的vrchat画笔自动化生成球器")
print_warning("请确保你已经在vrchat里拿着笔并且已经抬头准备好了")

for i in range(3):
    print_status(f"程序将在 {3 - i} 秒后开始...")
    time.sleep(1)
pydirectinput.FAILSAFE = False
pydirectinput.INTERVAL = 0.001

keyboard_thread = threading.Thread(target=listen_keyboard)
keyboard_thread.daemon = True
keyboard_thread.start()

try:
    move_mouse_right()
except KeyboardInterrupt:
    stop_flag = True
finally:
    print_status("程序已停止，bye~")