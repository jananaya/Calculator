class Calculator:
    def __init__(self):
        self.total_expression = ""
        self.current_expression = ""

    def evaluate(self):
        self.total_expression += self.current_expression

        try:
            self.current_expression = str(eval(self.total_expression))
        except Exception:
            self.current_expression = ""
        finally:
            self.total_expression = ""

    def add_to_expression(self, value):
        self.current_expression += str(value)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
