import webbrowser
import time
import pyautogui

class Site:
    def __init__(self, url):
        self.url = url
        self.open()

    def open(self):
        webbrowser.open(self.url)
        time.sleep(5)

    def move_to_text_input(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(5)