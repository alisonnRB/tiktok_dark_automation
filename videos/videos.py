from button_find.button_find import ButtonFind
from digitador.digitador import Digitador

import os
import time
import shutil

class Videos:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, download_name = None, dir_button = None, name = None, scroll = -2000):
        time.sleep(2)
        ButtonFind.find(download_name, "download", dir_button, scroll)
        
        time.sleep(2)
        ButtonFind.move_to_text_input(900, 96)
        Digitador(self.base_dir + "/video")

        time.sleep(2)
        ButtonFind.move_to_text_input(803, 740)
        Digitador(name)

        time.sleep(2)

    @staticmethod
    def upload(button_dir, video_dir, name_arq):
        time.sleep(2)
        ButtonFind.find("upload.PNG", "upload", button_dir)
        time.sleep(2)

        ButtonFind.move_to_text_input(900, 96)
        Digitador(video_dir + "/video")

        ButtonFind.move_to_text_input(803, 770)
        Digitador(name_arq)
        time.sleep(1)

    def clear(self):
        dir = self.base_dir + "/video"
        if not os.path.exists(dir):
            print(f"A pasta não existe.")
            return

        for item in os.listdir(dir):
            item_path = os.path.join(dir, item)
            
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

        print(f"Todo o conteúdo da pasta '{dir}' foi apagado.")