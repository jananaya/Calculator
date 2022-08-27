import tkinter as tk
from widgets.KeyboardButton import KeyboardButton


class Keyboard(tk.Frame):
    def __init__(self, master, theme):
        super().__init__(master)

        self.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.rowconfigure(x, weight=1)
            self.columnconfigure(x, weight=1)

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons = {"operator_buttons": [],
                        "digit_buttons": [], "special_buttons": []}

        self.create_buttons()

        self.set_theme(theme)

        self.pack(expand=True, fill=tk.BOTH)

    def create_buttons(self):

        for digit, grid_value in self.digits.items():
            self.buttons["digit_buttons"].append(
                KeyboardButton(self, text=str(digit),
                               row=grid_value[0], column=grid_value[1])
            )

        i = 0
        operation_buttons = self.buttons["operator_buttons"]

        for operator, symbol in self.operations.items():

            operation_buttons.append(
                KeyboardButton(self, text=symbol, row=i, column=4)
            )
            i += 1

        self.buttons["special_buttons"] = [
            KeyboardButton(self, text="C", row=0, column=1),
            KeyboardButton(self, text="=", row=4, column=3, colspan=2),
        ]

        operation_buttons.append(
            KeyboardButton(self, text="x\u00b2", row=0, column=2)
        )

        operation_buttons.append(
            KeyboardButton(self, text="\u221ax", row=0, column=3)
        )

    def config_theme(self):

        colors = self.theme["colors"]

        for button in self.buttons["digit_buttons"]:
            button.set_background_color(colors["primary"])

            button.set_text_color(colors["text"])

        for button in self.buttons["operator_buttons"]:
            button.set_background_color(colors["secondary"])

            button.set_text_color(colors["text"])

        for button in self.buttons["special_buttons"]:
            button.set_background_color(colors["contrast"])

            button.set_text_color("#ffffff")

    def set_theme(self, theme):
        self.theme = theme
        self.config_theme()
