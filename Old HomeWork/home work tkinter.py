# infomation v0.3
# this was made with a linux os, Some code might not work on other os
# e.g. window,mac and other versions of linux.
# made by Redacted
#
#import for important stuff
from random import *
from tkinter import *
import sys
#to set up the main  window
window = Tk()
window.title("work v0.3")
def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1,6)))
#
#
#debug tools and other tools to test code
score = 1
num_test_movement = 0
def move1():#moves the player 1 counter
    canvas.move(player1, 50,000)
    print("player moved")
#
#
#
def move2():#moves the player 1 counter
    canvas.move(player1, 000,50)
    print("player moved")
#
#
#
def movescore():#score system testing
    canvas.move(player1, 50,000)
    num_score = score + 1
    text.insert(END, str(num_score))
    print("movescore test",num_score)
#
#
#
def gen_moving():#testing how to use random genrating number to move player ?
    text.delete(0.0, END)
    text.insert(END, str(randint(1,6)))
    
#
#
#
#back ground 
canvas = Canvas(window, width = 510, height = 360, bg="blue")


#playing board
#row 1
canvas.create_rectangle(5,5,55,55, fill = "white")
canvas.create_rectangle(55,5,105,55, fill = "black")
canvas.create_rectangle(105,5,155,55, fill = "white")
canvas.create_rectangle(155,5,205,55, fill = "black")
canvas.create_rectangle(205,5,255,55, fill = "white")
canvas.create_rectangle(255,5,305,55, fill = "black")
canvas.create_rectangle(305,5,355,55, fill = "white")

#row 2
canvas.create_rectangle(5,55,55,105, fill = "black")
canvas.create_rectangle(55,55,105,105, fill = "white")
canvas.create_rectangle(105,55,155,105, fill = "black")
canvas.create_rectangle(155,55,205,105, fill = "white")
canvas.create_rectangle(205,55,255,105, fill = "black")
canvas.create_rectangle(255,55,305,105, fill = "white")
canvas.create_rectangle(305,55,355,105, fill = "black")

#row 3
canvas.create_rectangle(5,105,55,155, fill = "white")
canvas.create_rectangle(55,105,105,155, fill = "black")
canvas.create_rectangle(105,105,155,155, fill = "white")
canvas.create_rectangle(155,105,205,155, fill = "black")
canvas.create_rectangle(205,105,255,155, fill = "white")
canvas.create_rectangle(255,105,305,155, fill = "black")
canvas.create_rectangle(305,105,355,155, fill = "white")

#row 4
canvas.create_rectangle(5,155,55,205, fill = "black")
canvas.create_rectangle(55,155,105,205, fill = "white")
canvas.create_rectangle(105,155,155,205, fill = "black")
canvas.create_rectangle(155,155,205,205, fill = "white")
canvas.create_rectangle(205,155,255,205, fill = "black")
canvas.create_rectangle(255,155,305,205, fill = "white")
canvas.create_rectangle(305,155,355,205, fill = "black")

#row 5
canvas.create_rectangle(5,205,55,255, fill = "white")
canvas.create_rectangle(55,205,105,255, fill = "black")
canvas.create_rectangle(105,205,155,255, fill = "white")
canvas.create_rectangle(155,205,205,255, fill = "black")
canvas.create_rectangle(205,205,255,255, fill = "white")
canvas.create_rectangle(255,205,305,255, fill = "black")
canvas.create_rectangle(305,205,355,255, fill = "white")

#row 6
canvas.create_rectangle(5,255,55,305, fill = "black")
canvas.create_rectangle(55,255,105,305, fill = "white")
canvas.create_rectangle(105,255,155,305, fill = "black")
canvas.create_rectangle(155,255,205,305, fill = "white")
canvas.create_rectangle(205,255,255,305, fill = "black")
canvas.create_rectangle(255,255,305,305, fill = "white")
canvas.create_rectangle(305,255,355,305, fill = "black")

#row 7
canvas.create_rectangle(5,305,55,355, fill = "white")
canvas.create_rectangle(55,305,105,355, fill = "black")
canvas.create_rectangle(105,305,155,355, fill = "white")
canvas.create_rectangle(155,305,205,355, fill = "black")
canvas.create_rectangle(205,305,255,355, fill = "white")
canvas.create_rectangle(255,305,305,355, fill = "black")
canvas.create_rectangle(305,305,355,355, fill = "white")

#player 1 green
player1 = canvas.create_oval(5,5,55,55, fill = "green")

#player 2 red
#player2 = canvas.create_oval(5,5,55,55, fill = "red")

#scorboard for 2 player and saves for high scores
#canvas.create_rectangle(55,455,55,455, fill= "black")

#buttons
text = Text(window, width = 2, height = 1)
button = Button(window, text="Roll", command=roll)
#debug section of buttons and text
score = Text(window, width = 2, height = 1)
debug1 = Button(window, text="debug move forward", command=move1)#debug tool move forward
debug2 = Button(window, text="debug move down", command=move2)#debug tool move down
debug3 = Button(window, text="debug score", command=movescore)#debug tool score ?
debug4 = Button(window, text="debug gen num moving", command=gen_moving)#debug tool move ?
#.packs section
score.pack()
text.pack()
canvas.pack()
button.pack()
#debug sction of packs
debug1.pack()
debug2.pack()
debug3.pack()
debug4.pack()

