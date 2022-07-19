import flask
from flask import Blueprint, request, session
from service.reimbursement_service import ReimbursementService
from exception.user_name_not_found import UserNotFoundError

rc = Blueprint("reimbursement_controller", __name__)


@rc.route('/')
@rc.route('/home')
@rc.route('/index')
def get_home_page():
    return "Welcome To Reimbursement App"


@rc.route('/users/<user_id>')
def get_user_reimbursement(user_id):
    if session["user_info"]["username"] == user_id:
        args = request.args.get("status")
        if args:
            return ReimbursementService.get_user_reimbursement_args(user_id, args)
        else:
            return ReimbursementService.get_user_reimbursement(user_id)


@rc.route('/users/<user_id>', methods=['POST'])
def create_reimbursement(user_id):
    data = request.get_json()
    try:
        return ReimbursementService.create_reimbursement(user_id, data), 201
    except UserNotFoundError as e:
        return{"message": str(e)}, 404
