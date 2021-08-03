from tkinter import *
from functools import partial
import random


class menu:
    def __init__(self):
        #  Formatting variables
        background_color = "light blue"
        background = "light green"

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
                                   bg=background)
        self.start_button.grid(row=2)


# Start page(game page)
class start:
    def __init__(self, partner):

        # color of page
        background = "light yellow"

        # disable start button
        partner.start_button.config(state=DISABLED)

        # set up child window(start page)
        self.start_box = Toplevel()

        # after user closed start page, released start button
        self.start_box.protocol('WM_DELETE_WINDOW', partial(self.close_start, partner))

        # set up start frame
        self.start_frame = Frame(self.start_box, width=1000,
                                 bg=background,)
        self.start_frame.grid()

        # set up the heading (row 0)
        self.start_heading = Label(self.start_box, text="Please select the correct one",
                                   font="arial 18 bold", bg=background)
        self.start_heading.grid(row=0)

        # questions text (row 1)
        self.start_text = Label(self.start_box, text="What is the biggest country in the world?",
                                width=30, padx=10)
        self.start_text.grid(row=1)

        # answer buttons (row 3)
        self.answer_a_button = Button(self.start_box, text="A. Australia",
                                      width=8, bg="brown", font="arial 12 bold")




#  Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    something = menu()
    root.mainloop()


