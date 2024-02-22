import time
import random
from math import ceil, sqrt
import tkinter as tk
import tkinter.ttk as ttk

# choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# number = (len(choices)*2)+random.randint(1,len(choices)) #Number of times to loop through given choices list
# sleepTime = 0.01
# sleepIncrease = (1.55/(len(choices)))**2 #Increase sleep time between each iteration, to have it slow down as it reaches the final choice
# currentIndex = 0

# for i in range(number):
#     time.sleep(sleepTime)
#     print("Current choice: " + str(choices[currentIndex]).upper())
#     print("sleep time: " + str(sleepTime))
#     print()
#     currentIndex += 1
#     currentIndex %= len(choices)
#     sleepTime += sleepIncrease

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
def pickChoice(numWinners):
    global frameList
    global numChoices
    previousChoice = 0
    for i in range(numWinners):
        # frameList[previousChoice].configure(background="white")
        # picked = random.randint(0, numChoices-1)
        # frameList[picked].configure(background="yellow")
        # previousChoice = picked
        # window.tksleep(0.5)
        currentChoice = (i%(numChoices))
        print(currentChoice)

        frameList[previousChoice].configure(background="#F0F0F0")
        frameList[currentChoice].configure(background="yellow")
        previousChoice = currentChoice
        window.tksleep(0.1)


window = tk.Tk()
window.title("Random")
window.state("zoomed") #start maximized

numChoices = 26

frameList = []

sizeOfGrid = ceil(sqrt(numChoices)) #width and height of grid will be the sqrt of the number of choices, rounded up
currentRow = 0
currentColumn = 0
window.grid_rowconfigure(tuple(range(sizeOfGrid)), weight=1) #set all grid rows and columns to fill the max amount of space
window.grid_columnconfigure(tuple(range(sizeOfGrid)), weight=1)

#Create grid of choices
for i in range(numChoices):
    #frameList.append(tk.Label(window, text="choice " + str(i), font=("Roboto", 15), background=random.choice(["red", "blue", "green"]))) #Create labels with random background colors to easily differentiate borders for now
    frameList.append(tk.Label(window, text="choice " + str(i), font=("Roboto", 15)))
    frameList[i].grid(sticky="news", row=currentRow, column=currentColumn)
    currentColumn += 1 #increase column position for each choice
    
    #if last column reached, set back to first column and start on next row
    if currentColumn == sizeOfGrid:
        currentColumn = 0
        currentRow += 1

button = tk.Button(window, text="Pick", command=lambda: pickChoice(1000))
button.grid(row=0, column=sizeOfGrid)
    
window.mainloop()

