import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("300x200")
        self.time = 0
        self.running = False

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 32))
        self.label.pack(pady=20)

        self.start_btn = tk.Button(root, text="Start", width=10, command=self.start)
        self.start_btn.pack(side=tk.LEFT, padx=10)

        self.stop_btn = tk.Button(root, text="Stop", width=10, command=self.stop)
        self.stop_btn.pack(side=tk.LEFT, padx=10)

        self.reset_btn = tk.Button(root, text="Reset", width=10, command=self.reset)
        self.reset_btn.pack(side=tk.LEFT, padx=10)

    def update(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
