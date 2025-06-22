class Calculator:
    def add (self, a, b):
        return a + b

    def subtraCT(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = a * b
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


calc = Calculator()
print("Add: ", calc.add(5, 3))
print("Subtract: ", calc.subtraCT(5, 3))
print("Multiply: ", calc.multiply(5, 3))
print("Divide: ", calc.divide(5, 3))
