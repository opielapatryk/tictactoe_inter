import tkinter as tk 

player = "x"
previous_moves = []

def show_msg(row, col):
    global previous_moves
    global player
    button = buttons[row][col]
    if (row, col) not in previous_moves:
        previous_moves.append((row, col))
        button["text"] = player
        if player == "x":
            player = "o"
        else:
            player = "x"
        print(list(previous_moves))
        
    


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
