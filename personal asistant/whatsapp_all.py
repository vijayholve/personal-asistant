import pyautogui
import webbrowser as wb
from time import sleep
# sleep(6)
# print(pyautogui.position())
persons=["vijay","eatclub","karan","jio"]
def open_whatsapp(person,msg):
    wb.open("https://web.whatsapp.com/")
    sleep(7)
    
    # pyautogui.hotkey("F11")
    sleep(1)
    # print(pyautogui.position())
    pyautogui.click(x=116, y=172)
    for person in persons:

        pyautogui.typewrite(person)
        sleep(1)
        pyautogui.click(x=120, y=296)
        sleep(0.3)
        pyautogui.click(x=615, y=845)
        sleep(0.3)
        pyautogui.typewrite(msg)
        sleep(0.3)
        pyautogui.hotkey("enter")
        pyautogui.click(x=423, y=172)
    pyautogui.hotkey("alt","tab")
    
open_whatsapp(persons,"hiii how are you")