import flask
from flask import Blueprint, request
from service.reimbursement_service import ReimbursementService

rc = Blueprint("reimbursement_controller", __name__)


@rc.route('/')
@rc.route('/home')
@rc.route('/index')
def get_home_page():
    return "Welcome To Reimbursement App"


@rc.route('/users/<user_id>')
def get_user_reimbursement(user_id):
    return ReimbursementService.get_user_reimbursement(user_id)
