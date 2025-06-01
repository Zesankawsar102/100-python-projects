import tkinter as tk
import time
import random

sentences = [
    "Python is a powerful programming language.",
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast and accurately is a useful skill.",
    "This is a simple typing speed test.",
    "Practice every day to improve your speed."
]

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("700x400")

        self.text_to_type = random.choice(sentences)
        self.start_time = None

        self.instruction = tk.Label(root, text="Type the sentence below:", font=("Arial", 14))
        self.instruction.pack(pady=10)

        self.display_text = tk.Label(root, text=self.text_to_type, wraplength=600, font=("Consolas", 14), fg="blue")
        self.display_text.pack(pady=10)

        self.input_text = tk.Text(root, height=5, font=("Consolas", 14), wrap=tk.WORD)
        self.input_text.pack(pady=10)
        self.input_text.bind("<FocusIn>", self.start_timer)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.check_button = tk.Button(root, text="Check Speed", command=self.check_speed, font=("Arial", 12))
        self.check_button.pack(pady=5)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_speed(self):
        end_time = time.time()
        typed_text = self.input_text.get("1.0", tk.END).strip()

        time_taken = end_time - self.start_time if self.start_time else 1
        word_count = len(typed_text.split())
        wpm = word_count / (time_taken / 60)

        # Calculate accuracy
        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.text_to_type) and c == self.text_to_type[i])
        accuracy = (correct_chars / len(self.text_to_type)) * 100

        self.result_label.config(text=f"🕐 Time: {time_taken:.2f} sec | 🧠 WPM: {wpm:.2f} | 🎯 Accuracy: {accuracy:.2f}%")

        self.start_time = None  # Reset for another test

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()
