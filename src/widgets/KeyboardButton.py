import tkinter as tk


class KeyboardButton(tk.Button):
    def __init__(self, master, text, row, column, colspan=1):
        super().__init__(master)

        self.text = text

        self.config(text=text, borderwidth=0, font=("Arial", 20))
        self.grid(row=row, column=column, sticky=tk.NSEW, columnspan=colspan)

    def set_background_color(self, color):
        self.config(bg=color)

    def set_text_color(self, color):
        self.config(fg=color)

    def set_command(self, command):
        self.config(command=command)
