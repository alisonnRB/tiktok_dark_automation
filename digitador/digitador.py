import time
import pyautogui

class Digitador:
    def __init__(self,text):
        
        for char in text:
            if char == '\n':
                pyautogui.hotkey('shift', 'enter')
            else:
                pyautogui.write(char)
            time.sleep(0.03)

        time.sleep(1)

        pyautogui.press('enter')