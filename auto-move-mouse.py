
# first run---->  pip install pyautogui 

import pyautogui as agui 
import time
from random import randint


#Take Size of the screen 

x,y = agui.size()

#Move mouse randomly
index = 1
while True:
    print(f"Index {index} - Script Running")
    agui.moveTo(randint(0,x),randint(0,y)) # Randomly moves the moves all over the place
    print("----mouse moved")
    if index%2 == 0:
        agui.scroll(5)   # scroll up 10 "clicks"
        print("----page scrolled up")
    else:
        agui.scroll(-5) # scroll up 10 "clicks"
        print("----page scrolled down")
    time.sleep(5) #60 second delay 
    index = index + 1
# End Script by crtl C on terminal