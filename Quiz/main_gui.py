from tkinter import *

class Converter:

    def __init__(self, master):

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"
        # Set up GUI Frame
        self.temp_frame = Frame(master, padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Countries of the world quizzes",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "There are 4 different quizzes related to the countries" \
                       "of the world to choose from. For each quiz there'll be 10 " \
                       "questions with some quizzes needing to type out countries name and " \
                       "others that are multi-choice. Once completed it'll show your results " \
                       "and you can also see the results from previous quizzes in the history/export " \
                       "button where you can export your results if you wish to."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        # Main image
        self.image_path = "./images/globe2.png"
        self.img = PhotoImage(file=self.image_path)
        self.image_label = Label(self.temp_frame, image=self.img)
        self.image_label.grid(row=2)

        self.temp_error = Label(self.temp_frame, text="",
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # Sub heading
        self.temp_sub_heading = Label(self.temp_frame,
                                  text="Quizzes:",
                                  font=("Arial", "16", "bold"))
        self.temp_sub_heading.grid(row=4)

        # Conversion, help and history / export buttons
        self.quizzes_frame = Frame(self.temp_frame)
        self.quizzes_frame.grid(row=5)

        self.to_flags_button = Button(self.quizzes_frame,
                                      text="To Flags",
                                      bg="#d63f15",
                                      fg=button_fg,
                                      font=button_font, width=14,)

        self.to_flags_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_guess_country_button = Button(self.quizzes_frame,
                                              text="Guess the Country",
                                              bg="#009900",
                                              fg=button_fg,
                                              font=button_font, width=14)
        self.to_guess_country_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_history_button = Button(self.quizzes_frame,
                                        text="History/Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=14)

        self.to_history_button.grid(row=1, column=0,columnspan=2, padx=5, pady=10)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    app = Converter(root)
    root.mainloop()
