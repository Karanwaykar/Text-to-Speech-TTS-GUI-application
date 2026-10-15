import tkinter as tk
from tkinter import messagebox
import pyttsx3


class TextToSpeechGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text To Speech")
        self.root.geometry("500x300")
        self.root.config(bg="lightblue")

        self.engine = pyttsx3.init()

        self.label = tk.Label(
            self.root,
            text="Enter Text:",
            font=("Arial", 16),
            bg="lightblue"
        )
        self.label.pack(pady=10)

        self.textbox = tk.Entry(
            self.root,
            font=("Arial", 16),
            width=30
        )
        self.textbox.pack(pady=10)

        self.speak_btn = tk.Button(
            self.root,
            text="Speak",
            font=("Arial", 14),
            bg="green",
            fg="white",
            command=self.speak_text
        )
        self.speak_btn.pack(pady=5)

        self.clear_btn = tk.Button(
            self.root,
            text="Clear",
            font=("Arial", 14),
            bg="orange",
            command=self.clear_text
        )
        self.clear_btn.pack(pady=5)

        self.exit_btn = tk.Button(
            self.root,
            text="Exit",
            font=("Arial", 14),
            bg="red",
            fg="white",
            command=self.root.destroy
        )
        self.exit_btn.pack(pady=5)

        self.root.mainloop()

    def speak_text(self):
        text = self.textbox.get()

        if text.strip() == "":
            messagebox.showwarning(
                "Warning",
                "Please enter some text!"
            )
            return

        self.engine.say(text)
        self.engine.runAndWait()

    def clear_text(self):
        self.textbox.delete(0, tk.END)


TextToSpeechGUI()