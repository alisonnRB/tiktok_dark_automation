from chatGPT.chatGPT import ChatGPT
from qwen.qwen import Qwen
from videos.videos import Videos
from clip.clip import Clip
from tiktok.tiktok import TikTok

import pyautogui

class Main:
    def __init__(self):
        self.chat = ChatGPT()
        self.qwen = Qwen(self.chat.GPTprompt)
        self.video = Videos("download.PNG", self.qwen.base_dir, "marked")
        self.clip = Clip(self.video.base_dir)
        TikTok(self.video.base_dir)
        print("video postado")

        self.video.clear()
        print("pasta limpa")
        pyautogui.hotkey("alt", "f4")


if __name__ == "__main__":
    Main()