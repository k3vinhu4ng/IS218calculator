"""index controller"""
from flask import render_template
from app.controllers.controller import ControllerBase # pylint: disable=import-error, no-name-in-module, import-error

class IndexController(ControllerBase): # pylint: disable=too-few-public-methods
    """index controller"""
    @staticmethod
    def get():
        """return index page"""
        return render_template('index.html')
