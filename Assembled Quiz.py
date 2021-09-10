from tkinter import *
from functools import partial
import random


class Menu:
    def __init__(self):
        #  Formatting variables
        background_color = "deep sky blue"

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
                                   font="Arial 14", padx=10, pady=10,
                                   bg="light green", command=self.start)
        self.start_button.grid(row=2)

        # History button (row 3)

        # Help button (row 4)
        self.help_button = Button(self.menu_frame, text="Help",
                                  font="Arial 14",
                                  bg="light gray",
                                  padx=2, pady=2, command=self.help)
        self.help_button.grid(row=4, column=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Push 'Start' to start the game,"
                                          "entry your answer and press " 
                                          "'enter' to keep playing.")

    def start(self):
        get_start = Start(self)


# Help page
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


# Start page(game page)
class Start:
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
        self.start_frame = Frame(self.start_box, width=500, pady=50,
                                 bg=background,)
        self.start_frame.grid()

        # set up the heading (row 0)
        self.start_heading = Label(self.start_frame, text="Please type the correct answer",
                                   font="arial 18 bold", bg=background)
        self.start_heading.grid(row=0)

        # Entry box (row 2)
        self.entry_box = Entry(self.start_frame, width=10,
                               font="arial 12")
        self.entry_box.grid(row=3)

        # Quit button (row 3)
        self.quit_button = Button(self.start_frame, text="Exit",
                                  font="Arial 14",
                                  bg="brown",
                                  command=partial(self.close_start, partner))
        self.quit_button.grid(row=4, column=1)

        # Questions text (row 1)
        self.question_text = Label(self.start_frame,
                                   font="Arial 13",
                                   bg="light yellow")
        self.question_text.grid(row=1)

        # Result text (row 2)
        self.result_text = Label(self.start_frame,
                                 font="Arial 13",
                                 bg="light yellow")
        self.result_text.grid(row=2)

        # Submit button (row 5)
        self.submit_button = Button(self.start_frame,
                                    text="Submit",
                                    font="Arial 13",
                                    command=self.submit_answer)
        self.submit_button.grid(row=5)

        # Question List
        self.questionlist = [["What is the biggest country in the world", "Russia"], ["What is the most populated country",
                             "China"], ["What country is the capital of Paris", "France"], ["What is the smallest country in the world",
                             "Vatican"],
                             ["What country is the capital of Wellington", "NewZealand"]]
        self.num_questions = 0
        self.score = 0  # for count the score
        random.shuffle(self.questionlist)
        self.question = self.questionlist[0][0]
        self.correct_answer = self.questionlist[0][1]

        self.question_text.config(text=self.question, fg="black")

    # Submit answer and check the answer
    def submit_answer(self):
        user_answer = self.entry_box.get()
        if user_answer == self.correct_answer:
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        self.num_questions += 1
        if self.num_questions != 5:
            self.question = self.questionlist[self.num_questions][0]
            self.correct_answer = self.questionlist[self.num_questions][1]
            self.question_text.config(text=self.question)
        else:
            print(f"You have got {self.score} out of 5 questions correct!")
            quit()  # print score

    # destroy the program
    def close_start(self, partner):
        partner.start_button.config(state=NORMAL)
        self.start_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("World Countries Quiz")
    something = Menu()
    root.mainloop()
