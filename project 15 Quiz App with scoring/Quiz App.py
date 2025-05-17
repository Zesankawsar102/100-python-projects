import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    # Minecraft Questions
    ("What do you need to activate a Nether Portal?",
     ["A. Flint and Steel", "B. Lava", "C. Blaze Rod", "D. Redstone Torch"], "A"),
    ("Which mob explodes near players?",
     ["A. Skeleton", "B. Enderman", "C. Zombie", "D. Creeper"], "D"),
    ("What do you use to tame a horse?",
     ["A. Golden Apple", "B. Sugar", "C. Saddle", "D. Wheat"], "C"),
    ("What is the rarest ore in Minecraft (Overworld)?",
     ["A. Diamond", "B. Emerald", "C. Netherite", "D. Redstone"], "B"),
    ("What dimension is the Ender Dragon in?",
     ["A. Nether", "B. Overworld", "C. End", "D. Sky"], "C"),
    ("What item lets you breathe underwater longer?",
     ["A. Totem of Undying", "B. Potion of Water Breathing", "C. Golden Apple", "D. Ender Pearl"], "B"),
    ("Which tool mines blocks the fastest?",
     ["A. Wooden Pickaxe", "B. Gold Pickaxe", "C. Diamond Pickaxe", "D. Stone Pickaxe"], "B"),
    ("Which mob drops Ender Pearls?",
     ["A. Zombie Piglin", "B. Blaze", "C. Enderman", "D. Ghast"], "C"),
    ("How do you get to the Nether?",
     ["A. Fly up", "B. Use an End Portal", "C. Build a portal with obsidian", "D. Dig down"], "C"),
    ("What enchantment makes tools last longer?",
     ["A. Sharpness", "B. Unbreaking", "C. Efficiency", "D. Fortune"], "B"),

    # Bangladesh Questions
    ("What is the capital of Bangladesh?",
     ["A. Dhaka", "B. Chittagong", "C. Sylhet", "D. Rajshahi"], "A"),
    ("What is the national flower of Bangladesh?",
     ["A. Lily", "B. Rose", "C. Water Lily", "D. Lotus"], "C"),
    ("What is the currency of Bangladesh?",
     ["A. Rupee", "B. Taka", "C. Dollar", "D. Riyal"], "B"),
    ("What language is spoken in Bangladesh?",
     ["A. Hindi", "B. Urdu", "C. Bengali", "D. Arabic"], "C"),
    ("What is the longest river in Bangladesh?",
     ["A. Meghna", "B. Padma", "C. Jamuna", "D. Brahmaputra"], "B")
]

# GUI Setup
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft & Bangladesh Quiz")
        self.root.geometry("600x400")
        self.score = 0
        self.qn = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=550)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.options = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", font=("Arial", 12), variable=self.var, value=chr(65 + i))
            btn.pack(anchor="w", padx=100)
            self.options.append(btn)

        self.next_btn = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question)
        self.next_btn.pack(pady=20)

        self.display_question()

    def display_question(self):
        q, options, _ = questions[self.qn]
        self.question_label.config(text=f"Q{self.qn + 1}. {q}")
        self.var.set(None)
        for i, option in enumerate(options):
            self.options[i].config(text=option, value=option[0])

    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No answer", "Please select an answer.")
            return

        correct = questions[self.qn][2]
        if selected == correct:
            self.score += 1

        self.qn += 1
        if self.qn == len(questions):
            self.show_result()
        else:
            self.display_question()

    def show_result(self):
        message = f"You scored {self.score} out of {len(questions)}.\n\n"
        if self.score == 15:
            message += "🏆 Perfect! You're a Minecraft and Bangladesh master!"
        elif self.score >= 10:
            message += "🔥 Great job!"
        elif self.score >= 5:
            message += "👍 Not bad, but you can do better."
        else:
            message += "📚 Time to study more!"
        messagebox.showinfo("Quiz Completed", message)
        self.root.destroy()

# Run app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
