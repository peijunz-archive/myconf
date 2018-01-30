# By default if it is not absolute path, it is relative to ~
# Copy filename to ~/.filename

import os
import shutil

files = (
    {"path": "~",
     "files": {
         'aliases': '.aliases',
         'astylerc': '.astylerc',
         'gitconfig': '.gitconfig',
         'gitignore_global': '.gitconfig_global',
         'vimrc': '.vimrc',
         'xournalpp': '.xournalpp/setting.xml',
         'xournal': '.xournal/config',
         }
     },
     {"path": '~/.config',
      "files": {
          'kdeglobals': 'kdeglobals',
          'kwinqtcurve': 'kwinqtcurverc',
          'kwin': 'kwinrc',
          'kwinrules': 'kwinrulesrc',
          'okularpart': 'okularpartrc',
          'katepart': 'katepartrc',
          'konsole': 'konsolerc',
          'krunner': 'krunnerrc',
          'plasmashell': 'plasmashellrc',
          'kservicemenu': 'kservicemenurc',
          'kate': 'katerc',
          'dolphin': 'dolphinrc',
          'texstudio': 'texstudio/texstudio.ini',
          'gitk':'git/gitk',
          }
      }
      )

class Config:
    @staticmethod
    def allfiles():
        for group in files:
            path = group["path"]
            for bak, src in group["files"].items():
                yield bak, "{}/{}".format(path, src)
    @staticmethod
    def backup():
        for bak, src in self.allfiles():
            shutil.copy(src, bak)
    @staticmethod
    def restore():
        for bak, src in self.allfiles():
            shutil.copy(bak, src)


#repo_file = 'openSUSE.repo'
#execute = 
if __name__ == "__main__":
    for bak, src in Config.allfiles():
        print(bak, src)
