import os
import time
import pyautogui
import pyperclip
import webbrowser


class Window:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    def __init__(self, url, prompt):
        webbrowser.open(url)
        time.sleep(5)


        pyautogui.moveTo(700, 400)
        pyautogui.click()

        for char in prompt:
            if char == '\n':
                pyautogui.hotkey('shift', 'enter')
            else:
                pyautogui.write(char)

        time.sleep(1)

        pyautogui.press('enter')

        time.sleep(10)


        copiar_button_location = pyautogui.locateOnScreen(os.path.join(self.base_dir, 'copiar.PNG'), confidence=0.8)

        if copiar_button_location is not None:
            pyautogui.click(copiar_button_location)
            time.sleep(1) 


            copied_text = pyperclip.paste()
        else:
            print("Botão de copiar não encontrado na tela.")
