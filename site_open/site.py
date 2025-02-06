from button_find.button_find import ButtonFind

import os
import webbrowser
import time
import pyautogui

class Site:
    def __init__(self, url = None):
        self.url = url
        if self.url is not None:
            self.open()

    def open(self):
        webbrowser.open(self.url)
        time.sleep(5)

    @staticmethod
    def start(trys):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        time.sleep(2)
        
        ButtonFind.move_to_text_input(1580, 10)
        time.sleep(1)

        ButtonFind.find("chrome.PNG", "chrome", base_dir)
        time.sleep(2)

        ButtonFind.find("perfil" + str(trys) + ".PNG", "perfil", base_dir)

        try:
            ButtonFind.find("maximizar" + str(trys) + ".PNG", "maximizar", base_dir)  
        except pyautogui.ImageNotFoundException:
            pass
        
        time.sleep(1)