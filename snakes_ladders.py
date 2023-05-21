import tkinter as tk
from PIL import ImageTk,Image
import random

def start_game():
    global im
    global b1, b2
    
    # Insert buttons for the players 

    # Player_1 
    b1.place(x=900, y=300)

    # Player_2 
    b2.place(x=900, y=400)

    # Dice roll button with image to show
    # Read image
    im = Image.open("images/two_red_dice_roll.png")
    im = im.resize((70,70))
    im = ImageTk.PhotoImage(im)
    b = tk.Button(root, image=im, height=80, width=80,  bg="#008080" )
    b.place(x=950, y=150)

    # Exit button
    b = tk.Button(root, text="Click Here to End Game", height=2, width=20, fg="black", bg="#FA8128", font=('Cursive', 14, 'bold'), activebackground= 'white', command=root.destroy)
    b.place(x=875, y=20)

def reset_coins ():

    global player_1, player_2
    global pos1,pos2

    player_1.place(x=0, y=615)
    player_2.place(x=30, y=615)

    pos1=0
    pos2=0

def load_dice_images():

    global Dice
    names = ["Dicey-1.png","Dicey-2.png","Dicey-3.png","Dicey-4.png","Dicey-5.png","Dicey-6.png"]
    for nam in names:
        im = Image.open("images/" + nam)
        im = im.resize((70,70))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)


def roll_dice():

    global Dice
    global turn
    global pos1, pos2
    global b1, b2

    #Selecting random number on dice
    r = random.randint(1,6)
    b3 = tk.Button(root, image=Dice[r-1], height=80, width=80,  bg="#008080" )
    b3.place(x=950, y=150)

    if turn ==1:
        if (pos1 + r) <= 100:
            pos1 = pos1 + r
        move_coin(turn,pos1)
        if r != 6:
            turn = 2
            b1.configure(state='disabled')
            b2.configure(state='normal')
    else:
        if (pos2 + r) <= 100:
            pos2 = pos2 + r
        move_coin(turn,pos2)
        if r != 6:
            turn = 1
            b1.configure(state='normal')
            b2.configure(state='disabled')

def move_coin(Turn,r):

    global player_1, player_2
    global Index

    if Turn ==1 :
        player_1.place(x=Index[r][0], y=Index[r][1])
    else: 
        player_2.place(x=Index[r][0], y=Index[r][1])

def get_index():

    global player_1, player_2

    Num = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # player_1.place(x=20, y=33)
    # player_2.place(x=605, y=618)
    # row = 33
    # column = 20

    row = 33
    i = 0
    for x in range(1,11):
        col = 20
        for y in range(1,11):
            Index[Num[i]]=(col, row)
            col = col + 65
            i= i+1
        row = row + 65
    # print(Index)
                       
                       
                       
#To store Dice Images
Dice = []

#To store x & y Co-ordinates of given num
Index = {}

#Initial Positions of players
pos1 = None
pos2 = None

root = tk.Tk()
root.geometry("1200x800")
root.title("Laeticia's Snakes and Ladders game")

F1 = tk.Frame(root, width =1200, height = 800, relief = 'raised')
F1.place(x=0, y=0)

# Set Board (Image)
img1 = ImageTk.PhotoImage(Image.open("images/snakesandladdersboard.png"))
Lab = tk.Label(F1, image=img1)
Lab.place(x=0, y=0)

# Player_1 button
b1 = tk.Button(root, text="Player 1", height=2, width=15, fg="yellow", bg="#FA8128", font=('Cursive', 14, 'bold'), activebackground= 'white', command=roll_dice)


# Player_2 button
b2 = tk.Button(root, text="Player 2", height=2, width=15, fg="#FD5DA8", bg="#008080", font=('Cursive', 14, 'bold'), activebackground= 'white', command=roll_dice)


#Player 1 Coin
player_1 = tk.Canvas(root, width = 30, height = 30)
player_1.create_oval(5,5,30,30, fill = 'yellow')


#Player 2 Coin
player_2 = tk.Canvas(root, width = 30, height = 30)
player_2.create_oval(5,5,30,30, fill = '#FD5DA8')


#First turn by default Player 1
turn = 1

#Keep coins at Initial positions
reset_coins()

#Get index of Each Num
get_index()

#Load Dice Images
load_dice_images()

#Setting All the buttons
start_game()

root.mainloop()