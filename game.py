import os
from time import sleep
import random

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

main_sequence = []

def show_sequence():
    clear()
    for number in main_sequence:
        print(number)
        sleep(1)
        clear()
running = True

while running:
    main_sequence.append(str(random.randint(1, 4)))
    show_sequence()
    user_sequence = input("Wprowadź poprzednią sekwęcję")
    join_sequence = "".join(main_sequence)
    if user_sequence != join_sequence:
        print("Odpowiedź błędna")
        running = False



