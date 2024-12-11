from tkinter import *
import random

def next_turn(row, col):
    
    global player
    
    if buttons[row][col]["text"] == "" and check_winner() is False:
        
        if player == players[0]:
            buttons[row][col]["text"] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text= (players[1] + "'s turn"))
                
            elif check_winner() is True:
                label.config(text= (players[0] + " is the winner!"))
                
            elif check_winner() == "Tie":
                label.config(text= "It is a tie!")
                
        else:
            buttons[row][col]["text"] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text= (players[0] + "'s turn"))
                
            elif check_winner() is True:
                label.config(text= (players[1] + " is the winner!"))
                
            elif check_winner() == "Tie":
                label.config(text= "It's a tie!")


def check_winner():


    ## Check horizontal wins
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            disable_buttons()
            return True
    

    ## Check vertical wins
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            disable_buttons()
            return True
        
    
    ## Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        disable_buttons()
        return True
    
    elif buttons[2][0]["text"] == buttons[1][1]["text"] == buttons[0][2]["text"] != "":
        buttons[2][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[0][2].config(bg="green")
        disable_buttons()
        return True

    elif empty_spaces() is False:
        
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")
        disable_buttons()        
        return "Tie"
    
    else:
        return False


def empty_spaces():
    
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
                
    if spaces == 0:
        return False
    else:
        return True
    

def new_game():
    
    global player
    
    player = random.choice(players)
    label.config(text= player + "'s turn", font=("Arial", 40))
    
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text= "", bg= "#F0F0F0")
            buttons[row][column]["state"] = "normal"
            
def disable_buttons():
    
    for row in range(3):
        for column in range(3):
            buttons[row][column]["state"] = "disabled"
            


window = Tk()
##window.geometry("400x400")

## Naming the window
window.title("Tic-Tac_Toe")


## Naming players and choosing the first player
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


## Displaying who's turn is it
label = Label(window, text= player + "'s turn", font= ("Arial", 40))
##label.place(relx = 0.5, rely = 0, anchor = N)
label.pack(side="top")


## Reset Button
reset_button = Button(text="restart", font=("Arial", 20), command = new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()


## Making a grid for the field
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("Arial", 40), width = 4, height = 1, disabledforeground="black", command = lambda row = row, col = col: next_turn(row, col))
        buttons[row][col].grid(row = row, column = col)

window.mainloop()
