import tkinter as tk
from widgets.ResultJumbotron import ResultJumbotron
from widgets.Keyboard import Keyboard
from Calculator import Calculator
from utils.find import find
from utils.absoulte_path import get_absoulte_path


class App:
    def __init__(self, theme):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("375x667")
        self.window.resizable(0, 0)

        self.window.iconbitmap(get_absoulte_path(
            __file__, "../assets/calc.ico"))

        self.calculator = Calculator()
        self.screen = ResultJumbotron(self.window, theme)
        self.keyboard = Keyboard(self.window, theme)

        self.config_events()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())

        for key in self.keyboard.digits:
            self.window.bind(str(key), lambda event,
                             digit=key: self.add_to_expression(digit))

        for key in self.keyboard.operations:
            self.window.bind(key, lambda event,
                             operator=key: self.append_operator(operator))

    def config_events(self):
        buttons = self.keyboard.buttons

        for numeric_button in buttons["digit_buttons"]:
            numeric_button.set_command(
                command=lambda x=numeric_button.text: self.add_to_expression(x))

        for operator_button in buttons["operator_buttons"]:

            is_square_button = operator_button.text == "x\u00b2"
            is_sqrt_button = operator_button.text == "\u221ax"

            if is_square_button or is_sqrt_button:
                continue

            operations = self.keyboard.operations

            operator = list(operations.keys())[list(
                operations.values()).index(operator_button.text)]

            operator_button.set_command(
                command=lambda x=operator: self.append_operator(x))

        special_buttons = buttons["special_buttons"]

        equal_button = find(special_buttons, "text", "=")
        equal_button.set_command(command=self.evaluate)

        square_button = find(buttons["operator_buttons"], "text", "x\u00b2")
        square_button.set_command(command=self.square)

        sqrt_button = find(buttons["operator_buttons"], "text", "\u221ax")
        sqrt_button.set_command(command=self.sqrt)

        clear_button = find(special_buttons, "text", "C")
        clear_button.set_command(command=self.clear)

        self.bind_keys()

    def add_to_expression(self, digit):
        self.calculator.add_to_expression(digit)
        self.update_label()

    def append_operator(self, operator):
        self.calculator.append_operator(operator)
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        self.calculator.evaluate()
        self.update_label()
        self.update_total_label()

    def square(self):
        self.calculator.square()
        self.update_label()

    def sqrt(self):
        self.calculator.sqrt()
        self.update_label()

    def clear(self):
        self.calculator.clear()
        self.update_label()
        self.update_total_label()

    def update_total_label(self):
        expression = self.calculator.total_expression

        for operator, symbol in self.keyboard.operations.items():
            expression = expression.replace(operator, f' {symbol} ')

        self.screen.update_total_label(expression)

    def update_label(self):
        current_expression = self.calculator.current_expression

        self.screen.update_label(current_expression[:11])

    def run(self):
        self.window.mainloop()
