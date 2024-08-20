import os
import subprocess
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Progressbar
import sys

def resource_path(relative_path):
    """Obtain the absolute path to a resource in the bundled app."""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Configuration de la fenêtre
window = Tk()
# Définir la taille de la fenêtre à 400x400
window.geometry("400x60")
window.title("HEIC to JPG Converter")

progress_bar = Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=20)

folder_selected = filedialog.askdirectory()

# Compter le nombre total de fichiers HEIC
heic_files = []
for dirpath, _, filenames in os.walk(folder_selected):
    for filename in filenames:
        if filename.lower().endswith(".heic"):
            heic_files.append(os.path.join(dirpath, filename))

total_files = len(heic_files)
progress_bar["maximum"] = total_files

# Conversion des fichiers HEIC en JPG
for i, filepath in enumerate(heic_files):
    progress_bar["value"] = i + 1
    window.update_idletasks()
    
    print(f'Converting {filepath}...')
    convert_path = resource_path('ImageMagick-6.9.13-14-portable-Q16-HDRI-x64\\convert.exe')
    subprocess.run([convert_path, filepath, filepath[0:-5] + '.jpg'])
    
    try:
        os.remove(filepath)
    except OSError:
        pass

window.destroy()
