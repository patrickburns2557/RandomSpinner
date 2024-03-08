import time
import random
from math import ceil, sqrt
import tkinter as tk
import tkinter.ttk as ttk

OG_BACKGROUND = "#F0F0F0"
PICKED_BACKGROUND = "yellow"
FILENAME = "input.txt"
choices = []


#tkinter friendly version of time.sleep, from here: https://stackoverflow.com/questions/10393886/tkinter-and-time-sleep/74162322#74162322
def tksleep(self, time:float) -> None:
    """
    Emulating `time.sleep(seconds)`
    Created by TheLizzard, inspired by Thingamabobs
    """
    self.after(int(time*1000), self.quit)
    self.mainloop()
tk.Misc.tksleep = tksleep


#function to cycle through the choices
def pickChoice():
    global frameList
    global numChoices
    global sleepTime
    global sleepIncrease
    
    sleepTime = 0.01 #reset sleep time so subsequent rolls aren't slower than previous ones
    previousChoice = 0
    
    #Reset all choices back to default color, in case a roll was already done without restarting program
    for i in range(numChoices):
        frameList[i].configure(background=OG_BACKGROUND)

    #Shuffle a list twice as long as the number of choices and iterate through it to visually shuffle through the choices.
    #The last entry in the shuffled list will be the winner
    shuffledList = []
    for i in range(numChoices*2):
        index = i % numChoices
        shuffledList.append(index)
    random.shuffle(shuffledList)
    

    for i in shuffledList:
            frameList[previousChoice].configure(background=OG_BACKGROUND) #reset previous choice to only highlight one choice at a time while program is picking
            frameList[i].configure(background=PICKED_BACKGROUND)
            previousChoice = i
            window.tksleep(sleepTime)
            sleepTime += sleepIncrease

def readListFromFile():
     global choices

     with open(FILENAME, "r") as file:
          line = file.readline()
          while line != "":
               choices.append(line.strip())
               line = file.readline()
               


window = tk.Tk()
window.title("Random")
window.state("zoomed") #start maximized
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

numChoices = 26

sleepTime = 0.01
sleepIncrease = (1.55/numChoices)**2 #Increase sleep time between each iteration, to have it slow down as it reaches the final choice



frameList = []

sizeOfGrid = ceil(sqrt(numChoices)) #width and height of grid will be the sqrt of the number of choices, rounded up
currentRow = 0
currentColumn = 0



choicesFrame = tk.LabelFrame(window, text="Choices", font=("Roboto", 12),relief=tk.RAISED, borderwidth=5)
choicesFrame.grid_rowconfigure(tuple(range(sizeOfGrid)), weight=1) #set all grid rows and columns to fill the max amount of space
choicesFrame.grid_columnconfigure(tuple(range(sizeOfGrid)), weight=1)
choicesFrame.grid(row=0, column=1, sticky="news", padx=50, pady=30)

#Create grid of choices
for i in range(numChoices):
    #frameList.append(tk.Label(window, text="choice " + str(i), font=("Roboto", 15), background=random.choice(["red", "blue", "green"]))) #Create labels with random background colors to easily differentiate borders for now
    frameList.append(tk.Label(choicesFrame, text="choice " + str(i), font=("Roboto", 15), relief=tk.GROOVE, borderwidth=3))
    frameList[i].grid(sticky="news", row=currentRow, column=currentColumn, padx=5, pady=5)
    currentColumn += 1 #increase column position for each choice
    
    #if last column reached, set back to first column and start on next row
    if currentColumn == sizeOfGrid:
        currentColumn = 0
        currentRow += 1

button = tk.Button(window, text="Pick", width=20, relief=tk.GROOVE, borderwidth=5, command=lambda: pickChoice())
button.grid(row=0, column=0, sticky="ns", padx=30, pady=50)


readListFromFile()
print(choices)


window.mainloop()

