# mypackage/module2.py
def divide(a, b):
    """Function to divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
