import os
import time
import pyautogui

class ButtonFind:

    def __init__(self, name_arq, name_button, base_dir):
        pyautogui.scroll(clicks=-50)
        time.sleep(5)

        copiar_button_location = pyautogui.locateOnScreen(os.path.join(base_dir, name_arq), confidence=0.8)

        if copiar_button_location is not None:
            pyautogui.click(copiar_button_location)
            time.sleep(1) 

        else:
            print(f"Botão {name_button} não encontrado na tela.")