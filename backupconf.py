back_path = 'backups'
home_path = '/home/zpj'

files = (
    {"path": home_path,
     "back": back_path,
     "files": {
         'aliases': '.aliases',
         'astylerc': '.astylerc',
         'gitconfig': '.gitconfig',
         'gitignore_global': '.gitignore_global',
         'vimrc': '.vimrc',
         'xournalpp': '.xournalpp/settings.xml',
         'xournal': '.xournal/config',
         }
     },
     {"path": '{}/.config'.format(home_path),
      "back": back_path,
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
