import os
from time import sleep
import random

zmienna = [1, 2, 3]
x = input("cos tam: ")
print(x)
sleep(1)
os.system('cls')

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

clear()