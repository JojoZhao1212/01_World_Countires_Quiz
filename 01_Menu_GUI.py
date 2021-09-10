from tkinter import *
from functools import partial
import random

class menu:
    def __init__(self):
        #  Formatting variables
        background_color = "light blue"

        #  Menu frame
        self.menu_frame = Frame(width=1000, bg=background_color, pady=30)
        self.menu_frame.grid()

        #  Quiz heading (row 0)
        self.quiz_heading_label = Label(self.menu_frame,
                                        text="MENU",
                                        font="Arial 20 bold",
                                        bg=background_color,
                                        padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # Introduction of the quiz (row 1)
        self.quiz_introduction_label = Label(self.menu_frame,
                                             text="Welcome to World Countries Quiz"
                                             "     Please push the button to start  ",
                                             font="arial 14 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=150, pady=15)
        self.quiz_introduction_label.grid(row=1)

        # Start button  (row 2)
        self.start_button = Button(self.menu_frame, text="Start",
                                   font="Arial 14", padx=10, pady=10,
                                   bg="light green")
        self.start_button.grid(row=2)


#  Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = menu()
    root.mainloop()


