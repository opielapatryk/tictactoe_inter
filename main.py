import tkinter as tk 
class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.createBoard()
        self.createBoardGrid()

    def createBoard(self):
        frame = tk.Frame(master=self)
        label = tk.Label(master=frame, text="Reaaaady?")
        frame.pack()
        label.pack()

    def createBoardGrid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=50)
            for col in range(3):
                button = tk.Button(master=grid_frame,text="")
                self.cells[button] = (row,col)
                button.grid(row=row,column=col,padx=5,pady=5,sticky="nsew")



def main():
    game = Game()
    game.mainloop()

if __name__ == "__main__":
    main()