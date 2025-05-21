import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Notepad")
def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()

# Set up main window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")
text_area = tk.Text(root, font=("Consolas", 12))
text_area.pack(fill=tk.BOTH, expand=True)

# Menu
menu_bar = tk.Menu(root)
# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
# Attach menu to root
root.config(menu=menu_bar)
# Start the app
root.mainloop()
