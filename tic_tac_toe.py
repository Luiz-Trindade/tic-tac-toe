# Simple Tic Tac Toe Game Made In Python!
# Created By: Luiz Gabriel Magalhães Trindade.
# Distributed Under The GPL3 License. 
# GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from os import system
from random import randint as r
from colorama import Fore, Style

table = [
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"],
    ["[ ]", "[ ]", "[ ]"]
]

def update():
    try: system("clear")
    except: system("cls")

def view_table():
    for i in table:
        print(" "*10+"".join(i))
  
def choose_machine():
    while True:
        f = r(0, 2)
        p = r(0, 2)
        if table[f][p] == "[ ]":
            table[f][p] = Fore.RED+"[x]"+Style.RESET_ALL
            break

def choose_human():
    while True:
        f_h = int(input("Line: "))-1
        p_h = int(input("Column: "))-1
        if table[f_h][p_h] == "[ ]":
            table[f_h][p_h] = Fore.GREEN + "[o]" + Style.RESET_ALL
            break
        else:
            print("Choose another!")

def verify_game():
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != "[ ]":
            exit()
        elif table[0][i] == table[1][i] == table[2][i] != "[ ]":
            exit()
    if table[0][0] == table[1][1] == table[2][2] != "[ ]":
        exit()
    elif table[2][0] == table[1][1] == table[0][2] != "[ ]":
        exit()

def Main():
    update()
    print(" "*9+"TIC TAC TOE:")
    choose_machine()
    view_table()
    verify_game()

    choose_human()
    update()
    print(" "*9+"TIC TAC TOE:")
    view_table()
    verify_game()

while True:
    Main()
