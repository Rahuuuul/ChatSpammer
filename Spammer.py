
# Importing stuff
import pyautogui

# Configure Typing Thing
pyautogui.PAUSE = 0

# Input
input_list = "Put the Words Here K THx"


# generate words
output_list = input_list.split()

for x in output_list:
    pyautogui.write(x)
    pyautogui.press("enter")

