from tkinter import *
from functools import partial
import random


class menu:
    def __init__(self):
        #  Formatting variables
        background_color = "light green"

        #  Menu frame
        self.menu_frame = Frame(width=1000, bg=background_color, pady=30)
        self.menu_frame.grid()

        #  Quiz heading (row 0)
        self.quiz_heading_label = Label(self.menu_frame,
                                        text="World Countries Quiz",
                                        font="Arial 20 bold",
                                        bg=background_color,
                                        padx=10, pady=10)
        self.quiz_heading_label.grid(row=0)

        # Introduction of the quiz (row 1)
        self.quiz_introduction_label = Label(self.menu_frame,
                                             text="Push the button to start",
                                             font="arial 14 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=150, pady=15)
        self.quiz_introduction_label.grid(row=1)

        # Answer entry box  (row 2)
        self.start_button = Button(self.menu_frame, text="Start",
                                   font="Arial 14", padx=10, pady=10,)
        self.start_button.grid(row=2)


class Start:
    def __init__(self, partner):
        background = "red"
        partner.start_button.config(state=DISABLED)
        self.start_box = Toplevel()
        self.start_box.protocol('WM_DELETE_WINDOW', partial(self.close_start, partner))
        self.start_frame = Frame(self.start_box, width=500, bg=background)
        self.start_frame.grid()

        self.qus_heading = Label(self.start_box,
                                 txet="What is the biggest "
                                 "country in the world?",
                                 font="arial 14 bold", bg=background)
        self.qus_heading.grid(row=0)


#  Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = menu()
    root.mainloop()


