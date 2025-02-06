from site_open.site import Site
from button_find.button_find import ButtonFind
from digitador.digitador import Digitador
from videos.videos import Videos

import os
import time
import pyautogui

class Clip:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, video_dir):
        self.site = Site("https://online-video-cutter.com/pt/resize-video#google_vignette")
        self.video_dir = video_dir
        time.sleep(2)
        Videos.upload(self.base_dir, self.video_dir, "Marked.mp4")
        time.sleep(1)
        self.resize()

    def resize(self):
        ButtonFind.find("resize.PNG", "resize", self.base_dir, -200)
        ButtonFind.find("size.PNG", "size", self.base_dir)
        pyautogui.doubleClick()
        Digitador("1194")
        time.sleep(1)

        ButtonFind.find("salvar.PNG", "salvar", self.base_dir)
        time.sleep(5)

        Videos("save2.PNG", self.base_dir, "NotMarked", 0)
        return