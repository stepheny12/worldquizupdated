from tkinter import *
import random
from tkinter import messagebox


class Converter:

    def __init__(self, master):

        self.asked_questions = None

        # Initialize correct answers count
        self.correct_answers_count = 0

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

        # To Flags button command
        self.to_flags_button = Button(self.quizzes_frame,
                                      text="To Flags",
                                      bg="#d63f15",
                                      fg=button_fg,
                                      font=button_font, width=14,
                                      command=self.open_flags_quiz)
        self.to_flags_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_guess_country_button = Button(self.quizzes_frame,
                                              text="Guess the Country",
                                              bg="#009900",
                                              fg=button_fg,
                                              font=button_font, width=14)
        self.to_guess_country_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_match_flag_button = Button(self.quizzes_frame,
                                           text="Match the flag",
                                           bg="#f5e90c",
                                           fg=button_fg,
                                           font=button_font, width=14)
        self.to_match_flag_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_capitals_button = Button(self.quizzes_frame,
                                         text="Capitals",
                                         bg="#CC6600",
                                         fg=button_fg,
                                         font=button_font, width=14)
        self.to_capitals_button.grid(row=1, column=1, padx=5, pady=5)

        self.to_history_button = Button(self.quizzes_frame,
                                        text="History/Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=14)

        self.to_history_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def open_flags_quiz(self):
        # List to keep track of asked questions
        if not hasattr(self, 'asked_questions'):
            self.asked_questions = []

        quiz_data = [
            {
                "question": "Which countries flag is this",
                "image": "./images/flag1.png",
                "choices": ["Belgium", "Germany", "France", "Belguim"],
                "answer": "Belgium"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/flag2.png",
                "choices": ["China", "Turkey", "Japan", "Vietnam"],
                "answer": "Vietnam"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/flag3.png",
                "choices": ["Liberia", "Canada", "Cuba", "USA"],
                "answer": "USA"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/flag4.png",
                "choices": ["France", "Germany", "Spain", "Netherlands"],
                "answer": "France"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/flag5.png",
                "choices": ["England", "US", "UK", "Britain"],
                "answer": "UK"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag6.png",
                "choices": ["Finland", "Poland", "France", "Russia"],
                "answer": "Russia"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag7.png",
                "choices": ["Japan", "China", "Thailand", "South Korea"],
                "answer": "Japan"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag8.png",
                "choices": ["Ireland", "Italy", "France", "Ivory Coast"],
                "answer": "Italy"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag9.png",
                "choices": ["Australia", "New Zealand", "UK", "Austria"],
                "answer": "Australia"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag10.png",
                "choices": ["USA", "Mexico", "Canada", "Maple"],
                "answer": "Canada"
            },
        ]

        # Randomise the questions
        q = random.choice(quiz_data)

        # Remove the selected question from quiz_data
        self.asked_questions.append(q)

        # Create a new window for the quiz
        self.flags_window = Toplevel()
        self.flags_window.title("Flags Quiz")

        # Add image
        self.image_path = q.get('image')
        if self.image_path:
            self.img = PhotoImage(file=self.image_path)
            self.image_label = Label(self.flags_window, image=self.img)
            self.image_label.grid(row=0, columnspan=2, padx=10, pady=10)

        # Add question
        question_label = Label(self.flags_window, text=q.get('question'), font=("Arial", "14", "bold"))
        question_label.grid(row=1, columnspan=2, padx=10, pady=10)

        # Display choices as 2x2 buttons
        choices = q.get('choices')
        for i, choice_value in enumerate(choices):
            button = Button(self.flags_window, text=choice_value, width=20,
                            command=lambda selected_choice=choice_value: check_answer(selected_choice))
            button.grid(row=i // 2 + 2, column=i % 2, padx=5, pady=5)

        # Checks if selected answer is right or wrong
        def check_answer(selected_choice):
            if selected_choice == q.get('answer'):
                # Correct answer logic
                print("Correct!")
                self.correct_answers_count += 1  # Increase correct answer count by one
            else:
                # Incorrect answer logic
                print("Incorrect!")

            # Destroy current window
            self.flags_window.destroy()

            # Open next question or end quiz if all questions are answered
            self.open_next_quiz()

    # Method to open the next quiz or show the result if all questions are answered
    def open_next_quiz(self):
        remaining_questions = [q for q in quiz_data if q not in self.asked_questions]

        if not remaining_questions:
            # All questions answered, display result
            messagebox.showinfo("Quiz Result", f"You got {self.correct_answers_count} out of 10 questions correct!")
            return
        else:
            self.open_flags_quiz()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    app = Converter(root)
    root.mainloop()
