"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController # pylint: disable=import-error, no-name-in-module
from app.controllers.calculator_controller import CalculatorController # pylint: disable=import-error, no-name-in-module

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    """get indexcontroller"""
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """get calculator controller"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """get post calc"""
    return CalculatorController.post()

@app.route("/aaa", methods=['GET'])
def aaa_get():
    """get aaa page"""
    return CalculatorController.aaa()

@app.route("/python", methods=['GET'])
def python_get():
    """get python page"""
    return CalculatorController.python_tips()

@app.route("/soc", methods=['GET'])
def soc_get():
    """get soc page"""
    return CalculatorController.soc()

@app.route("/oop", methods=['GET'])
def oop_get():
    """get oop page"""
    return CalculatorController.oop()
