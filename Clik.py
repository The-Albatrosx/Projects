import pyautogui
import time

# Give you time to move the mouse
#print("Move your mouse to a spot... 3 seconds...")
#time.sleep(3)

# Get and print mouse position
#pos = pyautogui.position()
#print(f"Mouse Position: {pos}")

# Get and print pixel color at (10,10)
#pixel_color = pyautogui.pixel(274,312)
#print(f"Pixel at (10, 10): {pixel_color}")
import pyautogui

while True:
    if pyautogui.pixel(274, 312) == (75, 219, 106):
         pyautogui.click(274, 312)
         break
    #time.sleep(1)  # Sleep for a second before checking again