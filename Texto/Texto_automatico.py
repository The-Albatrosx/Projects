#import pyautogui

#print(pyautogui.position())
#print(pyautogui.pixel(10,10))


import pyautogui
import time

# Wait 3 seconds before starting so you can open another window
time.sleep(3)

# Move the mouse to a position
pyautogui.moveTo(700, 400, duration=1)

# Click there
pyautogui.click()

# Type something
pyautogui.write("Warning", interval=0.1)

pyautogui.press('enter')

pyautogui.press('enter')

pyautogui.write("automatic writer", interval=0.1)
pyautogui.press('enter')

#pyautogui.press('enter')

#pyautogui.write("First off, fuck your bitch and the clique you claim", interval=0.1)
#pyautogui.press('enter')
#pyautogui.write("You claim to be a player, but I fucked your wife", interval=0.1)