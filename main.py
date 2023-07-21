import readkeys
import re
# import tkinter as tk
board = "1|2|3\n4|5|6\n7|8|9"

def string_contains_substring_with_wildcard(string, substring):
    pattern = re.escape(substring) 
    pattern = pattern.replace('\\*', '.*')  
    match = re.search(pattern, string)
    return match is not None
 
print("Press any key to begin...")
print(board)

keys = ["1","2","3","4","5","6","7","8","9"]
player = 'x'
key = ''
while keys:
    key = readkeys.getkey()
    if key in keys:
        board = board.replace(key, player)
        keys.remove(key)
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
        print(board + "\n")
        if string_contains_substring_with_wildcard(board, "x|x|x*") or string_contains_substring_with_wildcard(board, "*x|x|x*") or string_contains_substring_with_wildcard(board, "*x|x|x") or string_contains_substring_with_wildcard(board, "x|*|*\nx|*|*\nx|*|*") or string_contains_substring_with_wildcard(board, "*|x|*\n*|x|*\n*|x|*") or string_contains_substring_with_wildcard(board, "*|*|x\n*|*|x\n*|*|x") or string_contains_substring_with_wildcard(board, "x|*|*\n*|x|*\n*|*|x") or string_contains_substring_with_wildcard(board, "*|*|x\n*|x|*\nx|*|*"):
            print("X won the game!")
            break
        elif string_contains_substring_with_wildcard(board, "o|o|o*") or string_contains_substring_with_wildcard(board, "*o|o|o*") or string_contains_substring_with_wildcard(board, "*o|o|o") or string_contains_substring_with_wildcard(board, "o|*|*\nx|*|*\no|*|*") or string_contains_substring_with_wildcard(board, "*|o|*\n*|o|*\n*|o|*") or string_contains_substring_with_wildcard(board, "*|*|o\n*|*|o\n*|*|o") or string_contains_substring_with_wildcard(board, "o|*|*\n*|o|*\n*|*|o") or string_contains_substring_with_wildcard(board, "*|*|o\n*|o|*\no|*|*"):
            print("O won the game!")
            break
        elif keys == []:
            print("Tie!")
    else:
        print("Try again...")



# import tkinter as tk

# window = tk.Tk()

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1,
#             bg="white"
#         )
#         frame.grid(row=i, column=j,padx=5,pady=5, sticky="nsew")
#         label = tk.Button(master=frame)
#         label.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)

# window.mainloop()
