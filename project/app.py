""" First small project as introduction to IO subject related to 
    Intoroduction to WEB Application Technology
"""
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    """ Return welcome sentence for home path """
    return "Hello, Flask!"

@app.route('/calculate')
def calculate():
    """Function realize simpel calculation operation.

    Function calculate requested operation for given arguments.
    Current version support: SUM for 2 given arguments

    Args:
        arg1 (str): request form GET metod type of calculation
        arg2 (int): first number for calculation
        arg3 (int): second number for calculation

    Returns:
        str: Rturn sum of calculated arguments

    """
    op   = request.args.get('op', type=str)
    arg1 = 0
    arg2 = 0

    ret_val = "Requested operation is not supported"
    if op == "sum":
        arg1 = request.args.get('arg1', type=int)
        arg2 = request.args.get('arg2', type=int)
        ret_val = f"Calculated sum is = {str(arg1 + arg2)}"

    return ret_val
