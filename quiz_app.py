import json
import tkinter as tk
from tkinter import messagebox

# ---------------- GUI SETUP ---------------- #
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x400")
root.config(bg="#1e1e2f")

# Now it's SAFE to create Tkinter variables
selected_option = tk.StringVar()

# Load questions
with open("questions.json", "r") as file:
    questions = json.load(file)

current_question = 0
score = 0

# ---------------- FUNCTIONS ---------------- #
def load_question():
    selected_option.set("")
    q = questions[current_question]
    question_label.config(text=f"Q{current_question + 1}. {q['question']}")

    for i in range(4):
        option_buttons[i].config(
            text=q["options"][i],
            value=q["options"][i]
        )

def next_question():
    global current_question, score

    if selected_option.get() == "":
        messagebox.showwarning("Warning", "Please select an option")
        return

    correct_answer = questions[current_question]["answer"]

    if selected_option.get() == correct_answer:
        score_label.config(text="✅ Correct!", fg="#00ff9d")
        score += 1
    else:
        score_label.config(
            text=f"❌ Wrong! Correct: {correct_answer}",
            fg="#ff6b6b"
        )

    root.after(1000, move_next)

def move_next():
    global current_question
    current_question += 1

    if current_question < len(questions):
        score_label.config(text="")
        load_question()
    else:
        show_result()

def show_result():
    messagebox.showinfo(
        "Quiz Completed",
        f"Your Score: {score}/{len(questions)}"
    )
    root.destroy()

# ---------------- UI ELEMENTS ---------------- #
frame = tk.Frame(root, bg="#1e1e2f", padx=20, pady=20)
frame.pack(expand=True, fill="both")

question_label = tk.Label(
    frame,
    text="",
    font=("Segoe UI", 16, "bold"),
    fg="white",
    bg="#1e1e2f",
    wraplength=540,
    justify="left"
)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    rb = tk.Radiobutton(
        frame,
        text="",
        variable=selected_option,
        value="",
        font=("Segoe UI", 12),
        fg="white",
        bg="#2a2a40",
        selectcolor="#4CAF50",
        activebackground="#2a2a40",
        activeforeground="white",
        indicatoron=0,
        width=40,
        pady=8
    )
    rb.pack(pady=5)
    option_buttons.append(rb)

next_btn = tk.Button(
    frame,
    text="Next",
    font=("Segoe UI", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=8,
    command=next_question
)
next_btn.pack(pady=20)

score_label = tk.Label(
    frame,
    text="",
    font=("Segoe UI", 12),
    bg="#1e1e2f"
)
score_label.pack()

# Load first question
load_question()

root.mainloop()
