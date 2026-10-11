# Libraries
import tkinter
from tkinter import filedialog
import json
import datetime
import os
from enum import Enum
import sys

# Global Variables
filesUsed = []
songs = []
currentMenu: MenuState
currentTimePeriod: TimePeriodState
currentSortBy: SortByState

class SongData:
    songName: str
    artistName: str
    msListened: int
    numOfStreams: int

class MenuState(Enum):
    SongsMenu = 1
    ArtistsMenu = 2

class TimePeriodState(Enum):
    CurrentMonth = 1
    PreviousMonth = 2
    Last30Days = 3
    Last90Days = 4
    Last180Days = 5
    SinceLastYear = 6
    Lifetime = 7
    CustomDate = 8

class SortByState(Enum):
    TrackAlphabetical = 1
    ArtistAlphabetical = 2
    MostStreams = 3
    HighestTimePlayed = 4

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

def SortingOptions():
    userInput = ""
    DisplaySortingOptions()
    while True:
        try: 
            userInput = input("Enter number (listed on the side): ")
            if (userInput.lower() in ["1", "2", "stop"]):
                if (userInput.lower() == "stop"):
                    sys.exit()
                else:  
                    return userInput
            else:
                raise
        except ValueError:
            print("Invalid Input. Please Try Again.")
            DisplaySortingOptions()

def DisplaySortingOptions():
    print("")
    print("---------------------------------------")
    print("Would you like to sort by: ")
    print("1) Top Songs")
    print("2) Top Artists")
    print("")
    print("Enter 'stop' to exit.")
    print("---------------------------------------")
    print("")

def TimePeriodOptions():
    global currentMenu
    currentOption: str
    otherOption: str
    def DetectOptions():
        currentOption = currentMenu.name.removesuffix("Menu")
        if (currentOption == "Songs"):
            otherOption = "Artists"
            return currentOption, otherOption
        else:
            otherOption = "Songs"
            return currentOption, otherOption

    while True:
        currentOption, otherOption = DetectOptions()
        DisplayTimePeriodOptions(currentOption=currentOption, otherOption=otherOption)
        try:
            print("")
            userInput = input("Enter number (listed on the side): ")
            print("")
            if (userInput.lower() in ["1", "2", "3", "4", "5", "6", "7", "8", "stop", "songs", "artists"]):
                if (userInput.lower() == "stop"):
                    sys.exit()
                elif (userInput.lower() == "songs"):
                    currentMenu = MenuState.SongsMenu
                elif (userInput.lower() == "artists"):
                    currentMenu = MenuState.ArtistsMenu
                else:  
                    return userInput
            else:
                raise
        except ValueError:
            print("Invalid Input. Please Try Again.")

def DisplayTimePeriodOptions(currentOption, otherOption):
    print("---------------------------------------")
    print(f"Top {currentOption}")
    print("What time period do you want to display? ")
    print("")
    print("1) Current Month")
    print("2) Previous Month")
    print("3) Last 30 Days")
    print("4) Last 90 Days")
    print("5) Last 180 Days")
    print("6) Since Last Year")
    print("7) Lifetime")
    print("8) Custom Date to Current Date")
    print("")
    print(f"Enter '{otherOption.lower()}' to switch to Top {otherOption}.")
    print("Enter 'stop' to exit.")
    print("---------------------------------------")

def SortByOptions():
    if (currentMenu == MenuState.SongsMenu):
        while True:
            DisplaySortByOptions()
            try:
                print("")
                userInput = input("Enter number (listed on the side): ")
                print("")
                if (userInput.lower() in ["1", "2", "3", "4"]):
                    return userInput
                else:
                    raise
            except ValueError:
                print("Invalid Input. Please Try Again.")
    else:
        while True:
            try:
                DisplaySortByOptions()
                print("")
                userInput = input("Enter number (listed on the side): ")
                print("")
                if (userInput.lower() in ["1", "2", "3"]):
                    return int(userInput) + 1 # Since first option removed, need to add 1 to ensure compatibility with Enum
                else:
                    raise
            except ValueError:
                print("Invalid Input. Please Try Again.")

def DisplaySortByOptions():
    print("---------------------------------------")
    print("How do you want the data to be sorted by?")
    print("")

    if (currentMenu == MenuState.SongsMenu):
        print("1) Alphabetically (Track Name)")
        print("2) Alphabetically (Artist Name)")
        print("3) Most Times Played")
        print("4) Highest Total Time Played")
    else:
        print("1) Alphabetically (Artist Name)")
        print("2) Most Times Played")
        print("3) Highest Total Time Played")

    print("---------------------------------------")
    print("")

# Sorting Algorithms


# Main Program
#OpenFiles()
currentMenu = MenuState(int(SortingOptions()))
currentTimePeriod = TimePeriodState(int(TimePeriodOptions()))
currentSortBy = SortByState(int(SortByOptions()))


