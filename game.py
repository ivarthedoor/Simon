import os
from time import sleep
import random

def clear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

main_sequence = []
main_sequence.append(str(random.randint(1, 4)))


while True:
    print(main_sequence)
    sleep(1)
    clear()
    user_sequence = input("Wprowadź poprzednią sekwęcję")
    join_sequence = "".join(main_sequence)
    if user_sequence == join_sequence:
        main_sequence.append(str(random.randint(1, 4)))
    else:
        print("Odpowiedź błędna")



print(main_sequence)
sleep(1)

