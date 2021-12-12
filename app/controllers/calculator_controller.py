"""controller app"""
from flask import render_template, request, flash, redirect, url_for # pylint: disable=import-error, unused-import
from app.controllers.controller import ControllerBase # pylint: disable=no-name-in-module
from calculator.calculator import Calculator

class CalculatorController(ControllerBase):
    """calculator controller"""
    history = []

    @staticmethod
    def post():
        """calculator functions"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2.'
        if not request.form['value1'].isnumeric() or not request.form['value2'].isnumeric():
            error = 'You must enter numeric values.'
        else:
            flash('Successful Calculation!')


            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            CalculatorController.history.append(result)
            data = CalculatorController.history

            return render_template('result.html', value1=value1, data=data, value2=value2, operation=operation, result=result) # pylint: disable=line-too-long
        return render_template('calculator2.html', error=error)

    @staticmethod
    def get():
        """returns calculator page"""
        return render_template('calculator2.html')

    @staticmethod
    def aaa():
        """returns aaa page"""
        return render_template('aaa.html')

    @staticmethod
    def python_tips():
        """returns python page"""
        return render_template('python.html')

    @staticmethod
    def soc():
        """returns soc page"""
        return render_template('soc.html')

    @staticmethod
    def oop():
        """returns oop page"""
        return render_template('oop.html')
