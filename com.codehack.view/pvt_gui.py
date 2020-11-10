from tkinter import *

class InputBox():

    def __init__(self, title):
        self.shape = 'Rectangle'
        self.title = title

    def draw_window(self):
        window = Tk()
        # Code to add widgets will be here
        window.title(self.title)

        window.geometry("350x550")
        label = Label(window, text="This is a PVT Calculator").pack()

        window.resizable(0, 0)
        input_frame = Frame(window, width=300, height=60, bd=0, highlightbackground="black",
                                    highlightcolor="black", highlightthickness=1)
        nameLabel = Label(input_frame, text="Name  ")
        nameLabel.grid(row = 0, column = 0)
        nameTF = Entry(input_frame, text=StringVar(), width=50)
        nameTF.grid(row = 0, column = 1)

        input_frame.pack()

        window.mainloop()

    def add_labels(self):
        pass


gui = InputBox("PVT Calculator GUI")
gui.draw_window()
