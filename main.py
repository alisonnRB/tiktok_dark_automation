from chatGPT.chatGPT import ChatGPT
from qwen.qwen import Qwen

class Main:
    def __init__(self):
        self.chat = ChatGPT()
        self.qwen = Qwen(self.chat.GPTprompt)
        


if __name__ == "__main__":
    Main()