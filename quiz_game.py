import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "C++ adalah bahasa pemograman yang di khususkan untuk pembuatan ?",
        "options": ["Game mobile", "Server", "Aplikasi", "OS perangkat"],
        "answer": "OS perangkat"
    },
    { 
        "question": "Siapa pencipta bahasa Python ?",
        "options": ["Steve Jobs", "Guido van Rossum","Bill Gates", "Anonymouse"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Minecraft Java Edition yang telah dibuat oleh Notch dikembangkan menggunakan bahasa pemograman ?",
        "options": ["C++", "HTML", "Python", "JavaScript"],
        "answer": "JavaScript"
    },
    {
        "question": "Apa kepanjangan dari OOP ?",
        "options": ["Object Oriented Process", "Object Oriented Prototyping", "Object Oriented Product", "Object Oriented Programming"],
        "answer": "Object Oriented Programming"
    },
    {
        "question": "Seorang SecurityCyber harus mempelajari bahasa pemograman ?",
        "options": ["JavaScript", "C++", "Python", "semua jawaban benar"],
        "answer": "semua jawaban benar"
    },
    {
        "question": "Pencipta bahasa JavaScript adalah ?",
        "options": ["Brendan Eich", "Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Brendan Eich"
    },
    {
        "question": "Seorang peretas biasanya menggunakan bahasa pemograman ?",
        "options": ["Python", "C++", "JavaScript", "HTML"],
        "answer": "Python"
    },
    {
        "question": "Hana terkena serangan virus komputer yang disebabkan oleh salah satu software yang dia download secara ilegal, apa yang harus dia lakukan untuk mengatasi masalah tersebut ?",
        "options": ["Install ulang OS", "Membawa kepada pihak yang berpengalaman", "Memformat hardisk", "Membiarkan saja"],
        "answer": "Membawa kepada pihak yang berpengalaman"
    },
    {
        "question": "Penggunaan kali linux biasanya memakai bahasa ?",
        "options": ["Python", "Bash", "JavaScript", "C++"],
        "answer": "Bash"
    },
    {
        "question": "Agar si Hana tidak terkena serangan virus komputer kembali, apa yang harus dia lakukan ?",
        "options": ["Menginstall antivirus", "Membiarkan saja", "Belajar pemrograman", "Menggunakan VPN"],
        "answer": "Menginstall antivirus"
    }
]

WINNING_SCORE_PERCENT = 80

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("2500x1500")
        self.configure(bg="#fff7fb")
        self.resizable(False, False)
        self.score = 0
        self.q_index = 0
        self.total_questions = len(questions)
        self.setup_widgets()
        self.display_question()

    def setup_widgets(self):
        self.title_label = tk.Label(self, text="Welcome to the Quiz Game", font=("Segoe UI", 26, "bold"), bg="#fff7fb", fg="#a832a8")
        self.title_label.pack(pady=25)
        self.question_label = tk.Label(self, text="", font=("Segoe UI", 17, "bold"), bg="#fff7fb", fg="#222")
        self.question_label.pack(pady=15)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self, text="", font=("Segoe UI", 14, "bold"), bg="#e0d6f7", fg="#222",
                activebackground="#d1c4e9", activeforeground="#a832a8",
                width=50, height=2, bd=0, relief=tk.RAISED, command=lambda i=i: self.check_answer(i)
            )
            btn.pack(pady=8)
            self.option_buttons.append(btn)

        self.score_label = tk.Label(self, text=f"Score: {self.score}", font=("Segoe UI", 14), bg="#fff7fb", fg="#a832a8")
        self.score_label.pack(pady=18)

    def display_question(self):
        q = questions[self.q_index]
        self.question_label.config(text=q["question"])
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, state=tk.NORMAL)
        self.score_label.config(text=f"Score: {self.score}")

    def check_answer(self, selected):
        q = questions[self.q_index]
        chosen = q["options"][selected]
        if chosen == q["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "😊 Well done! That's the right answer.")
        else:
            messagebox.showerror("Incorrect", f"☹️ Oops! The correct answer was: {q['answer']}")
        self.q_index += 1
        if self.q_index < self.total_questions:
            self.display_question()
        else:
            self.end_game()

    def end_game(self):
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)
        percent_score = (self.score / self.total_questions) * 100
        if percent_score >= WINNING_SCORE_PERCENT:
            messagebox.showinfo("You Win!", f"Congratulations! 😊\nYou scored {self.score} out of {self.total_questions} ({percent_score:.0f}%)")
        else:
            messagebox.showinfo("Game Over", f"You scored {self.score} out of {self.total_questions} ({percent_score:.0f}%)\n☹️ Better luck next time!")
        self.destroy()

if __name__ == "__main__":
    QuizGame().mainloop()