# Simple Hotel PDF Generator

This application is more specified for a small hotel. Please change hard-corded strings before you use it.

### How to export as .exe

`pyinstaller.exe  --add-data "logo.png;." --add-data "images/*;images" --add-data "outputs/*;outputs" --icon=icon.ico main.py -w --hidden-import "babel.numbers"`