# inputs = eval(input())
from flask import Flask

# def logged_deco(fn):
#     def wrapper(*args):
#         print(f"your dec is {fn.__name__} {args}")
#         resul = fn(args[0], args[1], args[2])
#         print(f"your total is {resul}")

#     return wrapper

# @logged_deco
# def a_function(a, b, c):
#     return a * b * c


# a_function(inputs[0], inputs[1], inputs[2],)

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"


if __name__ == ("__name__"):
    app.run()