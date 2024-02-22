import time
import random
import tkinter as tk
import tkinter.ttk as ttk

choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


number = (len(choices)*2)+random.randint(1,len(choices))
sleepTime = 0.01
sleepIncrease = (1.55/(len(choices)))**2
currentIndex = 0

for i in range(number):
    time.sleep(sleepTime)
    print("Current choice: " + str(choices[currentIndex]).upper())
    print("sleep: " + str(sleepTime))
    print()
    currentIndex += 1
    currentIndex %= len(choices)
    sleepTime += sleepIncrease
    