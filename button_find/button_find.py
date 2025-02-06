import os
import time
import pyautogui

class ButtonFind:

    @staticmethod
    def find(name_arq, name_button, base_dir, scroll = 0):
        pyautogui.scroll(clicks=scroll)
        time.sleep(5)

        copiar_button_location = pyautogui.locateOnScreen(os.path.join(base_dir, name_arq), confidence=0.8)

        if copiar_button_location is not None:
            pyautogui.click(copiar_button_location)
            time.sleep(1) 

        else:
            print(f"Botão {name_button} não encontrado na tela.")

    @staticmethod
    def move_to_text_input(x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(3)