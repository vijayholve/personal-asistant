import pyautogui
import webbrowser as wb
from time import sleep
import pywhatkit as kit
from datetime import datetime
# sleep(6)
# print(pyautogui.position())
now=datetime.now()
hour=now.hour
min=now.minute
from whatsapp.models import persons
persons=["vijay","jio","eatclub"]
def open_whatsapp(person,msg):
    
    # [persons]
    persons_obj=persons.objects.get(id=persons)
    if per
        kit.sendwhatmsg()
        