import tkinter as tk 
from tkinter import messagebox

player = "x" #we use this to change player 
moves = 0 
previous_moves = [] #here we will collect all moves
#later I will check if previous moves texts are...... then.......

def show_msg(row, col): #function for display the current moves
    global previous_moves 
    global player
    global moves
    button = buttons[row][col] 
    if (row, col) not in previous_moves: # check if current move was previously selected
        moves = moves + 1 
        previous_moves.append((row, col)) # if not, then add this to our list with previous moves
        button["text"] = player # change text ! 
        if player == "x": 
            player = "o"
        else:
            player = "x"
    check_win()

def check_win():
    global buttons
    global moves
    if buttons[0][0]['text'] == 'x' and buttons[1][0]['text'] == 'x' and buttons[2][0]['text'] == 'x' or buttons[0][1]['text'] == 'x' and buttons[1][1]['text'] == 'x' and buttons[2][1]['text'] == 'x' or buttons[0][2]['text'] == 'x' and buttons[1][2]['text'] == 'x' and buttons[2][2]['text'] == 'x' or buttons[0][0]['text'] == 'x' and buttons[0][1]['text'] == 'x' and buttons[0][2]['text'] == 'x' or buttons[1][0]['text'] == 'x' and buttons[1][1]['text'] == 'x' and buttons[1][2]['text'] == 'x' or buttons[2][0]['text'] == 'x' and buttons[2][1]['text'] == 'x' and buttons[2][2]['text'] == 'x' or buttons[0][0]['text'] == 'x' and buttons[1][1]['text'] == 'x' and buttons[2][2]['text'] == 'x' or buttons[2][0]['text'] == 'x' and buttons[1][1]['text'] == 'x' and buttons[0][2]['text'] == 'x':
        winner = 'x'
        button.after(100, lambda: messagebox.showinfo("showinfo", f"{winner} win!"))
    elif buttons[0][0]['text'] == 'o' and buttons[1][0]['text'] == 'o' and buttons[2][0]['text'] == 'o' or buttons[0][1]['text'] == 'o' and buttons[1][1]['text'] == 'o' and buttons[2][1]['text'] == 'o' or buttons[0][2]['text'] == 'o' and buttons[1][2]['text'] == 'o' and buttons[2][2]['text'] == 'o' or buttons[0][0]['text'] == 'o' and buttons[0][1]['text'] == 'o' and buttons[0][2]['text'] == 'o' or buttons[1][0]['text'] == 'o' and buttons[1][1]['text'] == 'o' and buttons[1][2]['text'] == 'o' or buttons[2][0]['text'] == 'o' and buttons[2][1]['text'] == 'o' and buttons[2][2]['text'] == 'o' or buttons[0][0]['text'] == 'o' and buttons[1][1]['text'] == 'o' and buttons[2][2]['text'] == 'o' or buttons[2][0]['text'] == 'o' and buttons[1][1]['text'] == 'o' and buttons[0][2]['text'] == 'o':
        winner = 'o'
        button.after(100, lambda: messagebox.showinfo("showinfo", f"{winner} win!"))
    elif moves == 9:
        winner = 'Both of you '
        button.after(100, lambda: messagebox.showinfo("showinfo", f"{winner} win!"))

        
frame = tk.Tk()
buttons = []

for row in range(3):
    frame.columnconfigure(row, weight=1, minsize=75)
    frame.rowconfigure(row, weight=1, minsize=50)
    row_buttons = []
    for col in range(3):
        button = tk.Button(master=frame, text="", width=10, height=5, command=lambda r=row, c=col: show_msg(r, c))
        button.grid(row=row, column=col, sticky="nsew")
        row_buttons.append(button)
    buttons.append(row_buttons)

frame.mainloop()
