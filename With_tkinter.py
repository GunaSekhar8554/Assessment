from tkinter import *
import tkinter as tk
import string
import random
import os
global gameboard
global ftickets
global XSIZE
global YSIZE


XSIZE = int(input("Enter Number Of Rows :"))
YSIZE = int(input("Enter Number Of Colmns :"))
NUMOFFAKES = int(input("Enter Number Of Fake Tickets :"))
NUMATTEMPTS = int(input("Enter Number Of Attempts :"))
alpha = list(string.ascii_uppercase)  # TO CREATE A LIST OF APLHABETS
alpha = alpha[:(YSIZE+1)]
# TO CREATE A LIST OF NUMBER IN RANGE OF 1 TO XSIZE
num = [i for i in range(1, XSIZE+1)]
num = num[::-1]

tickets = []
# TO CREATE TICKETS
for i in num:
    row = []
    for j in alpha:
        tickets.append(f"{j}{i}")
# TO GENERATE FAKE TICKETS WITHOUT REPETITION
ftickets = random.sample(tickets, NUMOFFAKES)
# print(ftickets)
gameboard = []  # TO CREATE A EMPTY BORD
for i in range(XSIZE):
    l = []
    for j in range(YSIZE):
        l.append(None)
    gameboard.append(l)
dict1 = {}  # CREATING A DICTIONARY FOR FINDING INDEX VALUE OF AN ALPHABET
for index, i in enumerate(list(string.ascii_uppercase)):
    dict1[i] = index
dict2 = {}  # CREATING A DICTIONARY FOR FINDING INDEX VALUE OF A NUMBER
for index, i in enumerate([_ for _ in range(XSIZE, 0, -1)]):
    dict2[str(i)] = index
window = Tk()  # CREATING A WINDOW WITH TITLE GAMEBORD


def display(gameboard):  # TO DISPLAY CONTENTS OF GAME BOARD

    window.title("gameboard")
    ll = list(string.ascii_uppercase)
    ll = ll[:YSIZE]
    q = 1
    for i in ll:  # TO ADD LABELS TO COLUMNS OF GAMEBOARD
        lb1 = tk.Label(window, text=i)
        lb1.grid(column=q, row=0)
        q += 1
    lll = [i for i in range(1, XSIZE+1)]
    lll = lll[::-1]
    r = 1
    for i in lll:  # TO ADD LABETS TO ROWS OF GAME BOARD
        lb1 = tk.Label(window, text=i)
        lb1.grid(column=0, row=r)
        r += 1

    w = 1
    for l in gameboard:  # TO DISPLAY VALUES OF GAME BOARD
        k = 1
        for h in l:
            lb1 = tk.Label(window, text=h, borderwidth=1, width=3,
                           height=1, relief="solid", bg='#afe8fa')
            lb1.grid(column=k, row=w)
            k = k + 1
        w = w + 1


def ftident(UserInput, st):  # TO IDENTIFY FAKE TICKET ON GAME BOARD

    col = (dict1[UserInput[0]])
    row = dict2[UserInput[1:]]

    gameboard[row][col] = st


INPUT_LIST = []
POINTS = 0
while NUMATTEMPTS > 0:  # ATTEMPTS
    UserInput = input("Enter The Ticket Number: ")
    if UserInput not in INPUT_LIST:  # CHECKING IF THE TICKET ALREADY USED OR NOT
        INPUT_LIST.append(UserInput)
        try:  # FOR CHECKING THE TICKET FORMAT
            # CHECKING IF THE TICKET IS WITHIN THE BOARD
            if (UserInput[0].upper() in alpha) and (int(UserInput[1:]) in num):
                st = ""
                if UserInput in ftickets:  # CHECKING IF THE TICKET IS FAKE TICKET OR NOT
                    st = "X"
                    POINTS += 1  # ADDING POINTS FOR FINDING FAKE TICKET
                else:
                    st = "O"
                ftident(UserInput, st)  # TO IDENTIFY FAKE TICKET ON GAME BOARD
                display(gameboard)  # TO DISPLAY GAME BOARD
                NUMATTEMPTS -= 1
                print(f"Remaining Number Of Attempts :{NUMATTEMPTS}")
                if POINTS > ((2 * NUMOFFAKES) / 3):  # CHECKING IF THE USER WON OR NOT
                    print(
                        f"WON!!!! By Scoring {POINTS} Pionts With Remaining {NUMATTEMPTS} Number Of Attempts")
                    break  # IF WON TERMINATING WHILE LOOP
                if NUMATTEMPTS==0:
                    print("Out Of Attempts")
                    break
            else:
                print("Invalied Ticket Number")
        except:
            print("Invalied Ticket Format")
    else:
        print("Already In Use")

window.mainloop()
os.system("cls")  # CLOSING THE PROGRAM