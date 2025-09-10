#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter


@app.route('/count/<int:parameter>')
def count(parameter):
    print(f"Counting up to {parameter}")  # optional log in console
    numbers = [str(i) for i in range(parameter)]
    return "\n".join(numbers) + "\n"


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation in ('/', 'divide', 'div'):
        if num2 == 0:
            return "Error: Division by zero."
        result = num1 / num2
        return str(result)  # keep float format
    elif operation == '%':
        if num2 == 0:
            return "Error: Modulo by zero."
        result = num1 % num2
    else:
        return "Error: Invalid operation. Use +, -, *, /, or %."

    return str(result)
