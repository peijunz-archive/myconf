# By default if it is not absolute path, it is relative to ~
# Copy filename to ~/.filename

import os
import shutil
from backupconf import *

class Config:
    @staticmethod
    def allfiles():
        for group in files:
            path = group["path"]
            for bak, src in group["files"].items():
                yield "{}/{}".format(back_path, bak), "{}/{}".format(path, src)
    @staticmethod
    def backup():
        for bak, src in Config.allfiles():
            try:
                shutil.copy(src, bak)
            except FileNotFoundError:
                print("{} does not exist".format(src))
    @staticmethod
    def restore():
        for bak, src in Config.allfiles():
            shutil.copy(bak, src)


#repo_file = 'openSUSE.repo'
#execute = 
if __name__ == "__main__":
    Config.backup()
    #Config.restore()
