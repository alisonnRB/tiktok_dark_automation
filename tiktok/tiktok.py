from site_open.site import Site
from button_find.button_find import ButtonFind
from videos.videos import Videos
from digitador.digitador import Digitador

import os
import time
import pyautogui

class TikTok:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, dir):
        self.site = Site("https://www.tiktok.com/tiktokstudio")
        ButtonFind.find("page_upload.PNG", "tiktok upload", self.base_dir)
        time.sleep(2)

        Videos.upload(self.base_dir, dir, "NotMarked.mp4")
        time.sleep(2)

        self.description()
        time.sleep(2)

        self.add_audio()
        time.sleep(2)

        ButtonFind.find("post.PNG", "postar video", self.base_dir)



    def description(self):
        ButtonFind.move_to_text_input(700, 500)
        pyautogui.hotkey('ctrl', 'a')

        Digitador("Legendary sea monster in by camera!")
        time.sleep(1)

        ButtonFind.move_to_text_input(410, 591)
        for _ in range(8):
            pyautogui.click()
            time.sleep(1)

    def add_audio(self):
        ButtonFind.find("edit.PNG", "tiktok audio", self.base_dir, -2000)
        time.sleep(3)
        
        ButtonFind.find("search.PNG", "tiktok search", self.base_dir)
        Digitador("Black Stars")
        time.sleep(3)

        ButtonFind.find("name_music.PNG", "musica", self.base_dir)
        time.sleep(1)
        ButtonFind.find("use.PNG", "selecao de musica", self.base_dir)
        time.sleep(1)

        ButtonFind.find("save_edit.PNG", "salvar musica", self.base_dir)

