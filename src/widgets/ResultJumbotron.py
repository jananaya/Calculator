import tkinter as tk


class ResultJumbotron(tk.Frame):
    def __init__(self, master, theme):
        super().__init__(master)

        self.pack(expand=True, fill="both")

        self.label = tk.Label(self, anchor=tk.E, padx=24, font=("Arial", 20, "bold"))
        self.total_label = tk.Label(self, anchor=tk.E, padx=24, font=("Arial", 30))
        
        self.set_theme(theme)

        self.label.pack(expand=True, fill='both')
        self.total_label.pack(expand=True, fill='both')
        
    def set_theme(self, theme):
        self.theme = theme
        self.config_theme()

    def config_theme(self):
        colors = self.theme["colors"]
        backgroud_color = colors["primary"]
        text_color = colors["text"]

        self.label.config(bg=backgroud_color, fg=text_color)
        self.total_label.config(bg=backgroud_color, fg=text_color)

    def update_label(self, text):
        self.total_label.config(text=text)
    
    def update_total_label(self, text):
        self.label.config(text=text)