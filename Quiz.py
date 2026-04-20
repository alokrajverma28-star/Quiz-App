import tkinter as tk
from tkinter import messagebox

# Questions (20)
questions = [
    ("What does CPU stand for?", ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"], 1),
    ("Which country has the largest population?", ["USA", "India", "China", "Russia"], 2),
    ("Which animal is known as King of Jungle?", ["Tiger", "Lion", "Elephant", "Bear"], 1),
    ("What is RAM?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "None"], 0),
    ("Capital of India?", ["Mumbai", "Delhi", "Kolkata", "Chennai"], 1),
    ("Fastest land animal?", ["Lion", "Cheetah", "Horse", "Tiger"], 1),
    ("What is Python?", ["Snake", "Programming Language", "Game", "OS"], 1),
    ("Capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2),
    ("Largest ocean?", ["Atlantic", "Indian", "Pacific", "Arctic"], 2),
    ("Which is a mammal?", ["Shark", "Dolphin", "Octopus", "Fish"], 1),
    ("Which company made Windows?", ["Apple", "Google", "Microsoft", "IBM"], 2),
    ("Capital of Japan?", ["Tokyo", "Seoul", "Beijing", "Bangkok"], 0),
    ("Which bird can fly highest?", ["Eagle", "Sparrow", "Crow", "Pigeon"], 0),
    ("What is HTML?", ["Markup Language", "Programming Language", "OS", "Game"], 0),
    ("Capital of USA?", ["New York", "Washington DC", "LA", "Chicago"], 1),
    ("Which animal is fastest in water?", ["Shark", "Dolphin", "Sailfish", "Whale"], 2),
    ("What is OS?", ["Operating System", "Open Software", "Order System", "None"], 0),
    ("Capital of UK?", ["London", "Paris", "Rome", "Berlin"], 0),
    ("Largest land animal?", ["Elephant", "Giraffe", "Rhino", "Hippo"], 0),
    ("Which device is used to input data?", ["Monitor", "Keyboard", "Printer", "Speaker"], 1)
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.q_no = 0
        self.score = 0
        self.time_left = 1200
        self.user_answers = [-1] * len(questions)

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()
        self.options = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value=i, font=("Arial", 12))
            btn.pack(anchor="w")
            self.options.append(btn)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.prev_btn = tk.Button(btn_frame, text="Previous", command=self.prev_question)
        self.prev_btn.grid(row=0, column=0, padx=10)

        self.next_btn = tk.Button(btn_frame, text="Next", command=self.next_question)
        self.next_btn.grid(row=0, column=1, padx=10)

        self.timer_label = tk.Label(root, text="Time: 20:00", font=("Arial", 12))
        self.timer_label.pack()

        self.load_question()
        self.update_timer()

    def load_question(self):
        q, opts, _ = questions[self.q_no]
        self.question_label.config(text=f"Q{self.q_no + 1}. {q}")
        self.var.set(self.user_answers[self.q_no])

        for i in range(4):
            self.options[i].config(text=opts[i])

    def next_question(self):
        self.user_answers[self.q_no] = self.var.get()

        if self.q_no < len(questions) - 1:
            self.q_no += 1
            self.load_question()
        else:
            self.calculate_result()

    def prev_question(self):
        self.user_answers[self.q_no] = self.var.get()

        if self.q_no > 0:
            self.q_no -= 1
            self.load_question()

    def calculate_result(self):
        self.score = 0
        result_text = ""  # will store full review with questions

        for i in range(len(questions)):
            q, opts, correct = questions[i]
            user_ans = self.user_answers[i]

            if user_ans == correct:
                self.score += 1
                status = "Correct"
            else:
                status = "Wrong"

            correct_option = opts[correct]
            chosen_option = opts[user_ans] if user_ans != -1 else "Not Answered"

            result_text += (
                f"Q{i+1}. {q}\n"
                f"Status: {status}\n"
                f"Your Answer: {chosen_option}\n"
                f"Correct Answer: {correct_option}\n\n"
            )

        percentage = (self.score / len(questions)) * 100

        messagebox.showinfo("Final Result", f"Score: {self.score}/{len(questions)}\nPercentage: {percentage:.2f}%")

        # Show detailed answers
        result_window = tk.Toplevel(self.root)
        result_window.title("Answer Review")

        text_box = tk.Text(result_window, wrap="word", width=60, height=25)
        text_box.pack()
        text_box.insert("1.0", result_text)
        text_box.config(state="disabled")

    def update_timer(self):
        mins = self.time_left // 60
        secs = self.time_left % 60
        self.timer_label.config(text=f"Time: {mins:02}:{secs:02}")

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time Up", "Time is over!")
            self.calculate_result()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
