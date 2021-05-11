#!/usr/bin/env python3
import os


print("Input anything but a character, i dare you")

while True:
    try:
        value = float(input())
        os.system('clear')
        break
    except ValueError:
        print("I told you not to type in a character!")
        pass
        break

while True:
    try:
        print("Your value is " + str(value))
        break
    except NameError:
        pass
        break



    

