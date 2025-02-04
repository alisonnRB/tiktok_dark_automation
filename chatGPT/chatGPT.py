from prompt.prompt import Prompt
from digitador.digitador import Digitador
from button_find.button_find import ButtonFind
from site_open.site import Site

import os
import time
import pyperclip

class ChatGPT:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.prompt = Prompt()

        self.site = Site("https://chatgpt.com")
        self.site.move_to_text_input(700, 400)
    
        Digitador(self.prompt.prompt)

        time.sleep(15)

        ButtonFind("copiar.PNG", "copiar", self.base_dir, -2000)
        self.GPTprompt = pyperclip.paste()



        

        
