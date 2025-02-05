from site_open.site import Site
from button_find.button_find import ButtonFind
from digitador.digitador import Digitador

import os
import time
import pyautogui

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
        self.espera()

    def salvar_video(self):
        time.sleep(2)
        ButtonFind("download.PNG", "download", self.base_dir, -2000)
        pyautogui.click()
        time.sleep(2)
        self.site.move_to_text_input(900, 96)
        Digitador(self.base_dir + "/videos")
        time.sleep(2)
        ButtonFind("salvar.PNG", "salvar", self.base_dir)

    def espera(self):
        print("🔍 Aguardando botão de download aparecer...")
        time.sleep(2)

        try:
            botao_erro = pyautogui.locateOnScreen(
                os.path.join(self.base_dir, "erro.PNG"), confidence=0.6
            )

            if botao_erro:
                print("Erro, limite exedido")
                return
            
        except pyautogui.ImageNotFoundException:
            pass

        max_attempts = 120
        attempt = 0

        while attempt < max_attempts:
            try:
                botao_download = pyautogui.locateOnScreen(
                    os.path.join(self.base_dir, "download.PNG"), confidence=0.6
                )

                if botao_download:
                    print("✅ Botão de download encontrado! Iniciando o salvamento do vídeo...")
                    self.salvar_video()
                    return  

            except pyautogui.ImageNotFoundException:
                print(f"🔍 Tentativa {attempt + 1}: Imagem não encontrada.")

            except Exception as e:
                print(f"⚠️ Erro inesperado: {e}")

            print("⏳ Aguardando 30 segundos antes de tentar novamente...")
            time.sleep(30)  
            attempt += 1  

        print("⏰ Tempo de espera excedido. O botão não foi encontrado em 1 hora.")
        self.restart() 

    def restart(self):
        print("🔄 Recarregando página e tentando novamente...")
        pyautogui.hotkey("ctrl", "r") 
        time.sleep(20) 
        self.espera() 

