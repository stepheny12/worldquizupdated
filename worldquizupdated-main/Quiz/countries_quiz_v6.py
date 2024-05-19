from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox
from tkinter import Entry, Listbox, END
from tkinter import ttk


class AutocompleteEntry(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()
        self.var.trace('w', self.update)
        self.choices = []
        self.popup = None
        self.bind("<KeyRelease>", self.on_key_release)

    def update(self, name, index, mode):
        self.comparison()

    def comparison(self):
        pattern = self.var.get().lower()
        words = [choice for choice in self.choices if pattern in choice.lower()]

        if words:
            if not self.popup:
                self.popup = Toplevel(self)
                self.popup.wm_overrideredirect(True)
                self.lb = Listbox(self.popup, width=self["width"])
                self.lb.pack()
            else:
                self.popup.lift()  # Bring the popup to the front

            self.lb.bind("<Double-Button-1>", self.set_choice)

            self.lb.delete(0, END)
            for w in words:
                self.lb.insert(END, w)

            # Position the popup relative to the main window
            x, y = self.winfo_rootx(), self.winfo_rooty() + self.winfo_height()
            self.popup.geometry("+%d+%d" % (x, y))
        else:
            if self.popup:
                self.popup.destroy()
                self.popup = None

    def on_key_release(self, event):
        if event.keysym not in ["Up", "Down", "Left", "Right"]:
            self.comparison()

    def set_choice(self, event):
        if self.lb.curselection():
            index = self.lb.curselection()[0]
            value = self.lb.get(index)
            self.var.set(value)
            self.focus_set()
            if self.popup:
                self.popup.destroy()
                self.popup = None

    def set_choices(self, choices):
        self.choices = choices

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
                                              font=button_font, width=14,
                                              command=self.open_country_quiz)
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

        self.difficulty_window = Toplevel()
        self.difficulty_window.title("Difficulty")

        difficulty_label = Label(self.difficulty_window, text="Choose your difficulty", font=("Arial", "16", "bold"))
        difficulty_label.grid(row=0, columnspan=2, padx=10, pady=10)

        button_font = ("Arial", "14", "bold")

        # Set up difficulty button Frame
        self.diff_button_frame = Frame(self.difficulty_window, padx=10, pady=10)
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

        # Gets rid of difficulty window
        self.difficulty_window.destroy()

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

        # Gets rid of difficulty window
        self.difficulty_window.destroy()

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

        # Gets rid of difficulty window
        self.difficulty_window.destroy()

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

    def open_country_quiz(self):

        # List to keep track of asked questions
        if not hasattr(self, 'asked_questions'):
            self.asked_questions = []

        quiz_data = [
            {
                "question": "What country is this",
                "image": "./images/countries1.png",
                "answer": "Mexico"
            },
            {
                "question": "What country is this",
                "image": "./images/countries2.png",
                "answer": "Australia"
            },
            {
                "question": "What country is this",
                "image": "./images/countries3.png",
                "answer": "Sweden"
            },
            {
                "question": "What country is this",
                "image": "./images/countries4.png",
                "answer": "Iran"
            },
            {
                "question": "What country is this",
                "image": "./images/countries5.png",
                "answer": "United Kingdom"
            },
            {
                "question": "What country is this",
                "image": "./images/countries6.png",
                "answer": "Brazil"
            },
            {
                "question": "What country is this",
                "image": "./images/countries7.png",
                "answer": "Vietnam"
            }, {
                "question": "What country is this",
                "image": "./images/countries8.png",
                "answer": "Thailand"
            },
            {
                "question": "What country is this",
                "image": "./images/countries10.png",
                "answer": "Ukraine"
            },


        ]

        # Check if there are still questions left
        remaining_questions = [q for q in quiz_data if q not in self.asked_questions]
        if not remaining_questions:
            # Show total correct answers
            messagebox.showinfo("Quiz Finished", f"Total Correct Answers: {self.correct_answers}/10")
            # Update completed quizzes
            self.update_completed_quizzes("Easy Countries Quiz", self.correct_answers, 10)
            self.to_history_button.config(state=NORMAL)
            self.reset_quiz_state()  # Reset quiz state
            return

        # Randomise the questions
        q = random.choice(remaining_questions)

        # Remove the selected question from quiz_data
        self.asked_questions.append(q)

        # Create a new window for the quiz
        self.countries_window = Toplevel()
        self.countries_window.title("Easy Countries Quiz")

        # Add image
        self.image_path = q.get('image')
        if self.image_path:
            self.img = PhotoImage(file=self.image_path)
            self.image_label = Label(self.countries_window, image=self.img)
            self.image_label.grid(row=0, columnspan=2, padx=10, pady=10)

        # Add question
        question_label = Label(self.countries_window, text=q.get('question'), font=("Arial", "14", "bold"))
        question_label.grid(row=1, columnspan=2, padx=10, pady=10)

        # Entry widget for user's answer
        self.answer_entry = AutocompleteEntry(self.countries_window, width=30)
        self.answer_entry.grid(row=2, columnspan=2, padx=10, pady=10)
        self.answer_entry.choices = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
                                     "Argentina", "Armenia",
                                     "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh",
                                     "Barbados", "Belarus", "Belgium",
                                     "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana",
                                     "Brazil", "Brunei", "Bulgaria",
                                     "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
                                     "Central African Republic", "Chad",
                                     "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba",
                                     "Cyprus", "Czech Republic",
                                     "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador",
                                     "Egypt", "El Salvador",
                                     "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
                                     "Finland", "France", "Gabon", "Gambia",
                                     "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
                                     "Guinea-Bissau", "Guyana", "Haiti",
                                     "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
                                     "Israel", "Italy", "Ivory Coast",
                                     "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo",
                                     "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
                                     "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
                                     "Luxembourg", "Madagascar", "Malawi",
                                     "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
                                     "Mauritius", "Mexico", "Micronesia",
                                     "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar",
                                     "Namibia", "Nauru", "Nepal",
                                     "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
                                     "North Macedonia", "Norway", "Oman",
                                     "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
                                     "Philippines", "Poland",
                                     "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
                                     "Saint Lucia", "Saint Vincent and the Grenadines",
                                     "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
                                     "Serbia", "Seychelles", "Sierra Leone",
                                     "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
                                     "South Korea", "South Sudan", "Spain",
                                     "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan",
                                     "Tajikistan", "Tanzania", "Thailand",
                                     "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
                                     "Tuvalu", "Uganda", "Ukraine",
                                     "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
                                     "Vanuatu", "Vatican City",
                                     "Venezuela", "Vietnam", "Yemen", "Zambia",
                                     "Zimbabwe"]  # Country List

        # Checks if selected answer is right or wrong for countries quiz
        def check_answer():
            while True:
                user_answer = self.answer_entry.get().strip().capitalize()  # Get user's answer
                if user_answer in self.answer_entry.choices:
                    if user_answer.lower() == q.get('answer').lower():
                        # Correct answer logic
                        print("Correct!")
                        self.correct_answers += 1  # Increment correct answer counter
                    else:
                        # Incorrect answer logic
                        print("Incorrect!")
                    break  # Break out of the loop when a valid answer is entered
                else:
                    # Invalid response
                    messagebox.showerror("Invalid Response", "Please input a valid country name.")
                    print(user_answer)

                    self.answer_entry.delete(0, END)  # Clear the entry widget
                    self.answer_entry.focus_set()  # Set focus back to the entry widget
                    self.countries_window.wait_window()  # Wait for user input

            # Destroy current window
            self.countries_window.destroy()

            # Open next question or end quiz if all questions are answered
            self.open_country_quiz()

        # Button to submit answer
        submit_button = Button(self.countries_window, text="Submit", command=check_answer)
        submit_button.grid(row=3, columnspan=2, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    app = Converter(root)
    root.mainloop()
