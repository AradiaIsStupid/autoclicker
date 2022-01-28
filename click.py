from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# Tile 1 Position: X:  581 Y:  400 RGB: ( 77,  80, 115)
# Tile 2 Position: X:  682 Y:  400 RGB: (  0,   0,   0)
# Tile 3 Position: X:  770 Y:  400 RGB: ( 79,  82, 116)
# Tile 4 Position: X:  869 Y:  400 RGB: ( 80,  83, 116)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(661, 450)[1] == 1:
        click(661, 450)
    if pyautogui.pixel(745, 450)[1] == 1:
        click(745, 450)
    if pyautogui.pixel(830, 450)[1] == 1:
        click(830, 450)
    if pyautogui.pixel(900, 450)[1] == 1:
        click(900, 450)
