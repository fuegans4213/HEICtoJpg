#HEIC to JPG en batch

import os
import subprocess
from tkinter import filedialog
from tkinter import *
import sys

# Fonction pour obtenir le chemin des ressources, même après conversion en .exe
def resource_path(relative_path):
    """Obtain the absolute path to a resource in the bundled app."""
    if getattr(sys, 'frozen', False):
        # If the app is frozen (running as an executable)
        base_path = sys._MEIPASS
    else:
        # If the app is running as a script
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Code pour sélectionner le dossier
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

# Dossier des ressources
resources_folder = resource_path('ImageMagick-6.9.13-14-portable-Q16-HDRI-x64')

for dirpat, _, filenames in os.walk(folder_selected):
    for filename in filenames:
        if filename.lower().endswith(".heic"):
            print('Converting %s...' % os.path.join(dirpat, filename))
            # Chemin vers convert.exe dans le dossier de ressources
            convert_path = resource_path('ImageMagick-6.9.13-14-portable-Q16-HDRI-x64\\convert.exe')
            subprocess.run([convert_path, os.path.join(dirpat, filename), os.path.join(dirpat, filename[0:-5] + '.jpg')])
            try:
                os.remove(os.path.join(dirpat, filename))
            except OSError:
                pass
            continue