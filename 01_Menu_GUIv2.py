from tkinter import *
from functools import partial


class Menu:
    def __init__(self):
        #  Formatting variables
        background_color = "deep sky blue"
        background = "light green"

        #  Menu frame
        self.menu_frame = Frame(width=10, bg=background_color, pady=10)
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
                                   font="Arial 14", padx=10, pady=10, width=8,
                                   bg="light green", command=self.start)
        self.start_button.grid(row=2)

        # Help button (row 3)
        self.help_button = Button(self.menu_frame, text="Help",
                                  font="Arial 14",
                                  bg="light gray",
                                  padx=2, pady=10, command=self.help)
        self.help_button.grid(row=3, column=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Push 'Start' to start the game,"
                                          "entry your answer and press " 
                                          "'enter' to keep playing.")

    def start(self):
        get_start = start(self)


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
        self.start_frame = Frame(self.start_box, width=50, pady=50,
                                 bg=background,)
        self.start_frame.grid()

        # set up the heading (row 0)
        self.start_heading = Label(self.start_frame, text="Please type the correct answer",
                                   font="arial 18 bold", bg=background)
        self.start_heading.grid(row=0)

        # questions text (row 1)
        self.start_text = Label(self.start_frame, text="What is the biggest country in the world?",
                                bg=background, width=30, padx=10)
        self.start_text.grid(row=1)

        # Entry box (row 2)
        self.entry_box = Entry(self.start_frame, width=10,
                               font="arial 12")
        self.entry_box.grid(row=2)

        # Next button (row 3)
        self.next_button = Button(self.start_frame, text="NEXT",
                                  width=8, bg="green", font="arial 14 bold")
        self.next_button.grid(row=3)

    def close_start(self, partner):
        partner.start_button.config(state=NORMAL)
        self.start_box.destroy()


class Help:
    def __init__(self, partner):
        background = "orange"
        partner.help_button.config(state=DISABLED)
        self.help_box = Toplevel()
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        self.how_heading = Label(self.help_frame, text="Help/Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        self.dismiss_btn = Button(self.help_frame, text=" I got it",
                                  width=10, bg="green", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=3, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("World Countries Quiz")
    something = Menu()
    root.mainloop()



