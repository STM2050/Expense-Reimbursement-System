import flask
from flask import Blueprint, request

uc = Blueprint("user_controller",__name__)

@uc.route('/')
@uc.route('/home')
@uc.route('/index')
def get_home_page():
    return "Welcome To Reimbursement App"