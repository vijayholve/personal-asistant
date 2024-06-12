import pyautogui
from time import sleep
import pyttsx3
# sleep(5)
# print(pyautogui.position())
#Point(x=1580, y=30)
# pyautogui.click(x=1493, y=30)
def tts(text):
    eng=pyttsx3.init()
    eng.say(text)

    eng.runAndWait()

def hack_in_process():
    tts("your accound is hacked")
    _extracted_from_hack_in_process_3(1, 'win', 'r', "cmd")
    sleep(0.3)
    pyautogui.hotkey("enter")
    _extracted_from_hack_in_process_3(1, 'alt', 'enter', "color 0a")
    pyautogui.hotkey("enter")
    pyautogui.typewrite("dir/s")
    pyautogui.hotkey("enter")


# TODO Rename this here and in `hack_in_process`
def _extracted_from_hack_in_process_3(arg0, arg1, arg2, arg3):
    sleep(arg0)
    pyautogui.hotkey(arg1, arg2)
    pyautogui.typewrite(arg3)
# # hack_in_process()
