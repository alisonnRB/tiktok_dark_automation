from site_open.site import Site
from button_find.button_find import ButtonFind
from digitador.digitador import Digitador

import os
import time

class Qwen:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, chatPrompt):
        self.site = Site("https://chat.qwenlm.ai")
        time.sleep(10)

        ButtonFind("gerar_videos.PNG", "gerar video", self.base_dir)
        ButtonFind("formato_selection.PNG", "seleção de formato", self.base_dir)
        time.sleep(2)
        ButtonFind("format.PNG", "formato", self.base_dir)

        self.site.move_to_text_input(700, 400)

        Digitador(chatPrompt)
