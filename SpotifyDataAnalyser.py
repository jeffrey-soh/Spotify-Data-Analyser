# Libraries
import tkinter
from tkinter import filedialog
import json
import datetime
import os

# Global Variables
filesUsed = []
songs = []

class SongData:
    songName: str
    artistName: str
    msListened: int
    numOfStreams: int

# Menu Subroutines
def OpenFiles():
    root = tkinter.Tk()
    root.withdraw()

    #Open file picker for multiple JSON files
    file_paths = filedialog.askopenfilenames(
        title="Select JSON files",
        initialdir=os.path.expanduser("~/Downloads"),
        filetypes=[("JSON files", "*.json")]
    )

    if file_paths:
        print("Selected file names:")
        for filePath in file_paths:
            filesUsed.append(filePath)
    else:
        print("No files selected.")

# Main Program
OpenFiles()
print(filesUsed)