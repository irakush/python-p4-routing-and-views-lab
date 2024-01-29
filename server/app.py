#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=5555, debug=True)


@app.route("/")
def index():
    return ("<h1>Python Operations with Flask Routing and Views</h1>", 200)


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return (parameter, 200)


@app.route("/count/<int:parameter>")
def count(parameter):
    res = ""
    for i in range(parameter):
        res += str(i) + "\n"

    return (res, 200)


@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    print(num1, operation, num2)

    if operation == "+":
        return (str(num1 + num2), 200)
    elif operation == "-":
        return (str(num1 - num2), 200)
    elif operation == "*":
        return (str(num1 * num2), 200)
    elif operation == "div":
        return (str(float(num1 / num2)), 200)
    elif operation == "%":
        return (str(num1 % num2), 200)
    else:
        return ("wrong operation", 200)
