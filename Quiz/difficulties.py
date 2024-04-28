from tkinter import *
import random
from tkinter import messagebox


class Converter:

    def __init__(self, master):

        self.flags_window = None
        self.correct_answers = 0  # Counter for correct answers
        self.completed_quizzes = []  # List to store completed quizzes

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
        self.main_image_path = "./images/globe2.png"
        self.main_img = PhotoImage(file=self.main_image_path)
        self.main_image_label = Label(self.temp_frame, image=self.main_img)
        self.main_image_label.grid(row=2)

        self.temp_error = Label(self.temp_frame, text="",
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # Sub heading
        self.temp_sub_heading = Label(self.temp_frame,
                                      text="Quizzes:",
                                      font=("Arial", "16", "bold"))
        self.temp_sub_heading.grid(row=4)

        # Quizzes and history buttons
        self.quizzes_frame = Frame(self.temp_frame)
        self.quizzes_frame.grid(row=5)

        # To Flags button command
        self.to_flags_button = Button(self.quizzes_frame,
                                      text="Flags",
                                      bg="#d63f15",
                                      fg=button_fg,
                                      font=button_font, width=14,
                                      command=self.difficulty_window)
        self.to_flags_button.grid(row=0, column=0, padx=5, pady=5)

        # To guess the country button c
        self.to_guess_country_button = Button(self.quizzes_frame,
                                              text="Guess the Country",
                                              bg="#009900",
                                              fg=button_fg,
                                              font=button_font, width=14)
        self.to_guess_country_button.grid(row=0, column=1, padx=5, pady=5)

        # To history button command
        self.to_history_button = Button(self.quizzes_frame,
                                        text="History/Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=14,
                                        state=DISABLED,
                                        command=self.show_history)

        self.to_history_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def difficulty_window(self):

        difficulty_window = Toplevel()
        difficulty_window.title("Difficulty")

        difficulty_label = Label(difficulty_window, text="Choose your difficulty", font=("Arial", "16", "bold"))
        difficulty_label.grid(row=0, columnspan=2, padx=10, pady=10)

        button_font = ("Arial", "14", "bold")

        # Set up difficulty button Frame
        self.diff_button_frame = Frame(difficulty_window, padx=10, pady=10)
        self.diff_button_frame.grid(row=1)

        # To Easy Flags button command
        self.to_easy_flags_button = Button(self.diff_button_frame,
                                           text="Easy",
                                           bg="#40eb34",
                                           fg="#000000",
                                           font=button_font, width=14,
                                           command=self.open_easy_flags_quiz)
        self.to_easy_flags_button.grid(row=0, column=0, padx=5, pady=5)

        # To Medium Flags button command
        self.to_medium_flags_button = Button(self.diff_button_frame,
                                             text="Medium",
                                             bg="#fbff14",
                                             fg="#000000",
                                             font=button_font, width=14,
                                             command=self.open_medium_flags_quiz)
        self.to_medium_flags_button.grid(row=0, column=1, padx=5, pady=5)

        # To Hard Flags button command
        self.to_hard_flags_button = Button(self.diff_button_frame,
                                           text="Hard",
                                           bg="#ed3511",
                                           fg="#000000",
                                           font=button_font, width=14,
                                           command=self.open_hard_flags_quiz)
        self.to_hard_flags_button.grid(row=0, column=2, padx=5, pady=5)

    def open_easy_flags_quiz(self):

        # List to keep track of asked questions
        if not hasattr(self, 'asked_questions'):
            self.asked_questions = []

        quiz_data = [
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag1.png",
                "choices": ["Belgium", "Germany", "France", "Belguim"],
                "answer": "Belgium"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag2.png",
                "choices": ["China", "Turkey", "Japan", "Vietnam"],
                "answer": "Vietnam"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag3.png",
                "choices": ["Liberia", "Canada", "Cuba", "USA"],
                "answer": "USA"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag4.png",
                "choices": ["France", "Germany", "Spain", "Netherlands"],
                "answer": "France"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/easyflag5.png",
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

        # Check if there are still questions left
        remaining_questions = [q for q in quiz_data if q not in self.asked_questions]
        if not remaining_questions:
            # Show total correct answers
            messagebox.showinfo("Quiz Finished", f"Total Correct Answers: {self.correct_answers}/10")
            # Update completed quizzes
            self.update_completed_quizzes("Easy Flags Quiz", self.correct_answers, 10)
            self.to_history_button.config(state=NORMAL)
            self.reset_quiz_state()  # Reset quiz state
            return

        # Randomise the questions
        q = random.choice(remaining_questions)

        # Remove the selected question from quiz_data
        self.asked_questions.append(q)

        # Create a new window for the quiz
        self.flags_window = Toplevel()
        self.flags_window.title("Easy Flags Quiz")

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
                self.correct_answers += 1  # Increment correct answer counter

            else:
                # Incorrect answer logic
                print("Incorrect!")

            # Destroy current window
            self.flags_window.destroy()

            # Open next question or end quiz if all questions are answered
            self.open_easy_flags_quiz()

    def open_medium_flags_quiz(self):

        # List to keep track of asked questions
        if not hasattr(self, 'asked_questions'):
            self.asked_questions = []

        quiz_data = [
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag1.png",
                "choices": ["India", "Pakistan", "Turkey", "Afghanistan"],
                "answer": "Pakistan"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag2.png",
                "choices": ["Nigeria", "Chad", "Zimbabwe", "Niger"],
                "answer": "Nigeria"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag3.png",
                "choices": ["Haiti", "Costa Rica", "Liberia", "Cuba"],
                "answer": "Cuba"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag4.png",
                "choices": ["Poland", "Singapore", "Indonesia", "Ukraine"],
                "answer": "Indonesia"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag5.png",
                "choices": ["Kenya", "Ethiopia", "Malawi", "Mozambique"],
                "answer": "Kenya"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag6.png",
                "choices": ["England", "Egypt", "Syria", "Yemen"],
                "answer": "Egypt"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag7.png",
                "choices": ["Slovakia", "Serbia", "Czech Republic", "France"],
                "answer": "Czech Republic"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag8.png",
                "choices": ["Spain", "Argentina", "Brazil", "Portugal"],
                "answer": "Portugal"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag9.png",
                "choices": ["Chile", "Peru", "Poland", "Singapore"],
                "answer": "Peru"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/mediumflag10.png",
                "choices": ["North Korea", "Belarus", "Morocco", "Thailand"],
                "answer": "North Korea"
            },
        ]

        # Check if there are still questions left
        remaining_questions = [q for q in quiz_data if q not in self.asked_questions]
        if not remaining_questions:
            # Show total correct answers
            messagebox.showinfo("Quiz Finished", f"Total Correct Answers: {self.correct_answers}/10")
            # Update completed quizzes
            self.update_completed_quizzes("Medium Flags Quiz", self.correct_answers, 10)
            self.to_history_button.config(state=NORMAL)
            self.reset_quiz_state()  # Reset quiz state
            return

        # Randomise the questions
        q = random.choice(remaining_questions)

        # Remove the selected question from quiz_data
        self.asked_questions.append(q)

        # Create a new window for the quiz
        self.flags_window = Toplevel()
        self.flags_window.title("Medium Flags Quiz")

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
                self.correct_answers += 1  # Increment correct answer counter

            else:
                # Incorrect answer logic
                print("Incorrect!")

            # Destroy current window
            self.flags_window.destroy()

            # Open next question or end quiz if all questions are answered
            self.open_medium_flags_quiz()

    def open_hard_flags_quiz(self):

        # List to keep track of asked questions
        if not hasattr(self, 'asked_questions'):
            self.asked_questions = []

        quiz_data = [
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag1.png",
                "choices": ["Bhutan", "Brunei", "Laos", "Singapore"],
                "answer": "Bhutan"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag2.png",
                "choices": ["Laos", "Cambodia", "Thailand", "Maldives"],
                "answer": "Cambodia"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag3.png",
                "choices": ["Libya", "Iran", "Syria", "Afghanistan"],
                "answer": "Afghanistan"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag4.png",
                "choices": ["Andorra", "Romania", "Moldova", "Chad"],
                "answer": "Moldova"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag5.png",
                "choices": ["Colombia", "Ethiopia", "Chad", "Romania"],
                "answer": "Chad"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag6.png",
                "choices": ["Guatemala", "Honduras", "El Salvador", "Nicaragua"],
                "answer": "Guatemala"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag7.png",
                "choices": ["French Guiana", "Guyana", "Suriname", "Bolivia"],
                "answer": "Guyana"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag8.png",
                "choices": ["Tajikistan", "Kyrgyzstan", "Azerbaijan", "Turkmenistan"],
                "answer": "Azerbaijan"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag9.png",
                "choices": ["San Marino", "Brunei", "Malta", "Vatican City"],
                "answer": "Vatican City"
            },
            {
                "question": "Which countries flag is this",
                "image": "./images/hardflag10.png",
                "choices": ["Trinidad and Tobago", "Barbados", "Grenada", "The Bahamas"],
                "answer": "Barbados"
            },
        ]

        # Check if there are still questions left
        remaining_questions = [q for q in quiz_data if q not in self.asked_questions]
        if not remaining_questions:
            # Show total correct answers
            messagebox.showinfo("Quiz Finished", f"Total Correct Answers: {self.correct_answers}/10")
            # Update completed quizzes
            self.update_completed_quizzes("Hard Flags Quiz", self.correct_answers, 10)
            self.to_history_button.config(state=NORMAL)
            self.reset_quiz_state()  # Reset quiz state
            return

        # Randomise the questions
        q = random.choice(remaining_questions)

        # Remove the selected question from quiz_data
        self.asked_questions.append(q)

        # Create a new window for the quiz
        self.flags_window = Toplevel()
        self.flags_window.title("Hard Flags Quiz")

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
                self.correct_answers += 1  # Increment correct answer counter

            else:
                # Incorrect answer logic
                print("Incorrect!")

            # Destroy current window
            self.flags_window.destroy()

            # Open next question or end quiz if all questions are answered
            self.open_hard_flags_quiz()

    def show_history(self):
        if not self.completed_quizzes:
            messagebox.showinfo("History", "No quizzes completed yet!")
            return

        history_window = Toplevel()
        history_window.title("Quiz History")

        history_label = Label(history_window, text="Quiz History", font=("Arial", "16", "bold"))
        history_label.grid(row=0, columnspan=2, padx=10, pady=10)

        # Display completed quizzes and results
        for idx, quiz_result in enumerate(self.completed_quizzes, start=1):
            quiz_name = quiz_result["quiz_name"]
            correct_answers = quiz_result["correct_answers"]
            total_questions = quiz_result["total_questions"]

            quiz_info_label = Label(history_window, text=f"Quiz {idx}: {quiz_name}, "
                                                         f"Correct Answers: {correct_answers}/{total_questions}")
            quiz_info_label.grid(row=idx, columnspan=2, padx=10, pady=5)

    def update_completed_quizzes(self, quiz_name, correct_answers, total_questions):
        self.completed_quizzes.append({
            "quiz_name": quiz_name,
            "correct_answers": correct_answers,
            "total_questions": total_questions
        })

    def reset_quiz_state(self):
        self.correct_answers = 0
        self.asked_questions = []


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    app = Converter(root)
    root.mainloop()
