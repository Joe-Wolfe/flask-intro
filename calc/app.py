# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


@app.route("/add")
def add():
    """returns a+b from querry string"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return str(operations.add(a, b))


@app.route("/sub")
def sub():
    """returns a-b from querry string"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return str(operations.sub(a, b))


@app.route("/mult")
def mult():
    """returns a*b from querry string"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return str(operations.mult(a, b))


@app.route("/div")
def div():
    """returns a/b from querry string"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return str(operations.div(a, b))


@app.route("/math/<func>")
def all_func(func):
    """returns result from querry string"""
    functions = {
        'add': operations.add,
        'sub': operations.sub,
        'mult': operations.mult,
        'div': operations.div,
    }
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    return str(functions[func](a, b))
