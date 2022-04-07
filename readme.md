# Simple Hotel PDF Generator

This application is more specified for a small hotel. Please change hard-corded strings before you use it.

### How to export as .exe

`pyinstaller.exe --onefile -F --add-data "logo.png;." --icon=icon.ico main.py -w --hidden-import "babel.numbers"`