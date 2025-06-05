import tkinter as tk
from tkinter import messagebox
from threading import Thread
from main import InterviewAnalyzer

def start_analysis(name_entry, root):
    user_name = name_entry.get().strip()
    if not user_name:
        messagebox.showwarning("Input Required", "Please enter your name.")
        return
    root.destroy()

    def run_analyzer():
        analyzer = InterviewAnalyzer(user_name)
        analyzer.run()

    Thread(target=run_analyzer).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interview Analyzer")
    root.geometry("500x300")
    root.configure(bg="#eaf6f6")
    root.resizable(False, False)

    # Create a central "card" frame
    card = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RIDGE)
    card.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=360, height=220)

    # Header label
    tk.Label(card, text="🎙️ Interview Analyzer", font=("Segoe UI", 16, "bold"), bg="#ffffff", fg="#333333").pack(pady=(20, 10))

    # Input label
    tk.Label(card, text="Enter your name below:", font=("Segoe UI", 11), bg="#ffffff", fg="#555555").pack(pady=(0, 5))

    # Entry field
    name_entry = tk.Entry(card, font=("Segoe UI", 11), bd=1, relief=tk.FLAT, highlightthickness=1, highlightcolor="#cccccc", width=30)
    name_entry.pack(pady=(0, 10))

    # Start button
    start_button = tk.Button(
        card,
        text="▶ Start Interview Tracking",
        font=("Segoe UI", 11, "bold"),
        bg="#4caf50",
        fg="white",
        activebackground="#45a049",
        relief=tk.FLAT,
        padx=12,
        pady=6,
        cursor="hand2",
        command=lambda: start_analysis(name_entry, root)
    )
    start_button.pack(pady=(10, 5))

    # Footer or tip (optional)
    tk.Label(card, text="Press 'q' to stop tracking once it starts.", font=("Segoe UI", 9), bg="#ffffff", fg="#888888").pack(pady=(10, 0))

    root.mainloop()
