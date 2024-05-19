from tkinter import *
import random
from tkinter import messagebox


class Converter:

    def __init__(self, master):

        self.flags_window = None
        self.correct_answers = 0  # Counter for correct answers
        self.completed_quizzes = []  # List to store completed quizzes
        self.asked_questions = []  # List to store questions already asked
        self.current_quiz_title = ""
        self.validate_choice_entry_method = None
        self.check_answer_method = None

        # common format for all buttons
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
        self.current_quiz_title = "Easy Flags Quiz"
        self.validate_choice_entry_method = self.validate_choice_entry_easy
        self.check_answer_method = self.check_answer_easy
        self.open_flags_quiz()

    def open_medium_flags_quiz(self):
        self.current_quiz_title = "Medium Flags Quiz"
        self.validate_choice_entry_method = self.validate_choice_entry_medium
        self.check_answer_method = self.check_answer_medium
        self.open_flags_quiz()

    def open_hard_flags_quiz(self):
        self.current_quiz_title = "Hard Flags Quiz"
        self.validate_choice_entry_method = self.validate_choice_entry_hard
        self.check_answer_method = self.check_answer_hard
        self.open_flags_quiz()

    def open_flags_quiz(self):
        quiz_title = self.current_quiz_title
        validate_choice_entry_method = self.validate_choice_entry_method
        check_answer_method = self.check_answer_method

        # Define quiz data for each difficulty level here
        quiz_data = self.get_quiz_data(quiz_title)

        # Check if there are still questions left
        remaining_questions = [q for q in quiz_data if q not in self.asked_questions]
        if not remaining_questions:
            # Show total correct answers
            messagebox.showinfo("Quiz Finished", f"Total Correct Answers: {self.correct_answers}/10")
            # Update completed quizzes
            self.update_completed_quizzes(quiz_title, self.correct_answers, 10)
            self.to_history_button.config(state=NORMAL)
            self.reset_quiz_state()  # Reset quiz state
            return

        # Randomize the questions
        q = random.choice(remaining_questions)

        # Remove the selected question from quiz_data
        self.asked_questions.append(q)

        # Create a new window for the quiz
        self.flags_window = Toplevel()
        self.flags_window.title(quiz_title)

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

        # Text box for typing choices
        self.choice_entry = Entry(self.flags_window)
        self.choice_entry.grid(row=2, columnspan=2, padx=10, pady=10)
        self.choice_entry.bind("<KeyRelease>", lambda event: validate_choice_entry_method(event, q))

        # Display choices as labels
        choices = q.get('choices')
        for i, choice_value in enumerate(choices):
            choice_label = Label(self.flags_window, text=choice_value, font=("Arial", 12))
            choice_label.grid(row=i + 3, columnspan=2, padx=5, pady=5)

    def get_quiz_data(self, quiz_title):
        if quiz_title == "Easy Flags Quiz":
            return [
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag1.png",
                    "choices": ["A. Belgium", "B. Germany", "C. France", "D. Belgium"],
                    "answer": "A. Belgium"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag2.png",
                    "choices": ["A. China", "B. Turkey", "C. Japan", "D. Vietnam"],
                    "answer": "D. Vietnam"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag3.png",
                    "choices": ["A. Liberia", "B. Canada", "C. Cuba", "D. USA"],
                    "answer": "D. USA"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag4.png",
                    "choices": ["A. France", "B. Germany", "C. Spain", "D. Netherlands"],
                    "answer": "A. France"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag5.png",
                    "choices": ["A. England", "B. US", "C. UK", "D. Britain"],
                    "answer": "C. UK"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag6.png",
                    "choices": ["A. Finland", "B. Poland", "C. France", "D. Russia"],
                    "answer": "D. Russia"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag7.png",
                    "choices": ["A. Japan", "B. China", "C. Thailand", "D. South Korea"],
                    "answer": "A. Japan"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag8.png",
                    "choices": ["A. Ireland", "B. Italy", "C. France", "D. Ivory Coast"],
                    "answer": "B. Italy"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag9.png",
                    "choices": ["A. Australia", "B. New Zealand", "C. UK", "D. Austria"],
                    "answer": "A. Australia"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/easyflag10.png",
                    "choices": ["A. USA", "B. Mexico", "C. Canada", "D. Maple"],
                    "answer": "C. Canada"
                }
            ]
        elif quiz_title == "Medium Flags Quiz":
            return [
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag1.png",
                    "choices": ["A. India", "B. Pakistan", "C. Turkey", "D. Afghanistan"],
                    "answer": "B. Pakistan"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag2.png",
                    "choices": ["A. Nigeria", "B. Chad", "C. Zimbabwe", "D. Niger"],
                    "answer": "A. Nigeria"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag3.png",
                    "choices": ["A. Haiti", "B. Costa Rica", "C. Liberia", "D. Cuba"],
                    "answer": "D. Cuba"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag4.png",
                    "choices": ["A. Poland", "B. Singapore", "C. Indonesia", "D. Ukraine"],
                    "answer": "C. Indonesia"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag5.png",
                    "choices": ["A. Kenya", "B. Ethiopia", "C. Malawi", "D. Mozambique"],
                    "answer": "A. Kenya"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag6.png",
                    "choices": ["A. England", "B. Egypt", "C. Syria", "D. Yemen"],
                    "answer": "B. Egypt"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag7.png",
                    "choices": ["A. Slovakia", "B. Serbia", "C. Czech Republic", "D. France"],
                    "answer": "C. Czech Republic"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag8.png",
                    "choices": ["A. Spain", "B. Argentina", "C. Brazil", "D. Portugal"],
                    "answer": "D. Portugal"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag9.png",
                    "choices": ["A. Chile", "B. Peru", "C. Poland", "D. Singapore"],
                    "answer": "B. Peru"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/mediumflag10.png",
                    "choices": ["A. North Korea", "B. Belarus", "C. Morocco", "D. Thailand"],
                    "answer": "A. North Korea"
                }
            ]
        elif quiz_title == "Hard Flags Quiz":
            return [
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag1.png",
                    "choices": ["A. Bhutan", "B. Brunei", "C. Laos", "D. Singapore"],
                    "answer": "A. Bhutan"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag2.png",
                    "choices": ["A. Laos", "B. Cambodia", "C. Thailand", "D. Maldives"],
                    "answer": "B. Cambodia"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag3.png",
                    "choices": ["A. Libya", "B. Iran", "C. Syria", "D. Afghanistan"],
                    "answer": "D. Afghanistan"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag4.png",
                    "choices": ["A. Andorra", "B. Romania", "C. Moldova", "D. Chad"],
                    "answer": "C. Moldova"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag5.png",
                    "choices": ["A. Colombia", "B. Ethiopia", "C. Chad", "D. Romania"],
                    "answer": "C. Chad"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag6.png",
                    "choices": ["A. Guatemala", "B. Honduras", "C. El Salvador", "D. Nicaragua"],
                    "answer": "A. Guatemala"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag7.png",
                    "choices": ["A. French Guiana", "B. Guyana", "C. Suriname", "D. Bolivia"],
                    "answer": "B. Guyana"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag8.png",
                    "choices": ["A. Tajikistan", "B. Kyrgyzstan", "C. Azerbaijan", "D. Turkmenistan"],
                    "answer": "C. Azerbaijan"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag9.png",
                    "choices": ["A. San Marino", "B. Brunei", "C. Malta", "D. Vatican City"],
                    "answer": "D. Vatican City"
                },
                {
                    "question": "Which country's flag is this",
                    "image": "./images/hardflag10.png",
                    "choices": ["A. Trinidad and Tobago", "B. Barbados", "C. Grenada", "D. The Bahamas"],
                    "answer": "B. Barbados"
                }
            ]

    def validate_choice_entry_easy(self, event, q):
        self.validate_choice_entry_generic(event, q, self.check_answer_easy)

    def validate_choice_entry_medium(self, event, q):
        self.validate_choice_entry_generic(event, q, self.check_answer_medium)

    def validate_choice_entry_hard(self, event, q):
        self.validate_choice_entry_generic(event, q, self.check_answer_hard)

    def validate_choice_entry_generic(self, event, q, check_answer_method):
        entered_choice = self.choice_entry.get().strip().lower()
        choices = [choice.lower().split('. ')[1] for choice in q.get('choices')]
        if entered_choice in ('a', 'b', 'c', 'd'):
            choice_index = ord(entered_choice) - 97
            if choice_index < len(choices):
                check_answer_method(q.get('choices')[choice_index], q)
        else:
            self.disable_buttons()

    def check_answer_easy(self, selected_choice, q):
        self.check_answer_generic(selected_choice, q)

    def check_answer_medium(self, selected_choice, q):
        self.check_answer_generic(selected_choice, q)

    def check_answer_hard(self, selected_choice, q):
        self.check_answer_generic(selected_choice, q)

    def check_answer_generic(self, selected_choice, q):
        if selected_choice == q.get('answer'):
            print("Correct!")
            self.correct_answers += 1
        else:
            print("Incorrect!")
        self.flags_window.destroy()
        self.open_flags_quiz()

    def update_completed_quizzes(self, quiz_name, correct_answers, total_questions):
        print(f"Quiz completed: {quiz_name}, Correct Answers: {correct_answers}/{total_questions}")
        self.completed_quizzes.append({
            "quiz_name": quiz_name,
            "correct_answers": correct_answers,
            "total_questions": total_questions
        })

    def reset_quiz_state(self):
        self.correct_answers = 0
        self.asked_questions = []

    def disable_buttons(self):
        pass

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

            # Add export button
        export_button = Button(history_window, text="Export History", command=self.export_history)
        export_button.grid(row=len(self.completed_quizzes) + 1, columnspan=2, padx=10, pady=10)


    def export_history(self):
        try:
            with open("quiz_history.txt", "w") as file:
                for idx, quiz_result in enumerate(self.completed_quizzes, start=1):
                    quiz_name = quiz_result["quiz_name"]
                    correct_answers = quiz_result["correct_answers"]
                    total_questions = quiz_result["total_questions"]
                    file.write(f"Quiz {idx}: {quiz_name}\n")
                    file.write(f"Correct Answers: {correct_answers}/{total_questions}\n")
                    file.write("\n")
            messagebox.showinfo("Export Successful", "Quiz history has been exported to quiz_history.txt")
        except Exception as e:
            messagebox.showerror("Export Failed", f"An error occurred: {e}")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Countries Quiz")
    app = Converter(root)
    root.mainloop()
