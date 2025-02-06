import webbrowser
import time

class Site:
    def __init__(self, url = None):
        self.url = url
        if self.url is not None:
            self.open()

    def open(self):
        webbrowser.open(self.url)
        time.sleep(5)