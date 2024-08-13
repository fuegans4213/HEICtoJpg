# HEIC to JPG Converter

This project is a Python script that converts HEIC images to JPG format in batch mode. It utilizes ImageMagick for the conversion process. The script is packaged as a standalone executable using PyInstaller, which includes the necessary ImageMagick binaries.

## Requirements

- Python 3.x
- ImageMagick (included in the executable)
- PyInstaller (for building the executable)

## Installation

### 1. Install Python and PyInstaller

Ensure Python with tk feature is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

To install PyInstaller, use pip:

```bash
pip install pyinstaller
```

### 2. Run the Script
You can run the Python script directly:

```bash
python HeicToJpg.py
```


### 3.Build the Executable

To create the executable, use the following command:

```bash
pyinstaller --onefile --windowed --add-data "ImageMagick-6.9.13-14-portable-Q16-HDRI-x64;ImageMagick-6.9.13-14-portable-Q16-HDRI-x64" HeicToJpg.py
```

- --onefile: Packages everything into a single executable file.
- --windowed: Hides the console window (useful for GUI applications).
- --add-data: Includes the ImageMagick binaries in the executable.

The output executable will be located in the dist directory.

### Usage

After building the executable, you can run it directly by double-clicking the generated .exe file. The application will prompt you to select a directory containing .heic files. It will then convert all .heic files in the selected directory to .jpg format.

### Notes

Ensure that the path to convert.exe in the script is correct. It is assumed that the ImageMagick binaries are located in the ImageMagick-6.9.13-14-portable-Q16-HDRI-x64 directory.
The original .heic files will be deleted after conversion.