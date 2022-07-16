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
    args = request.args.get("status")
    print(args)
    # if args == "pending":
    #     return ReimbursementService.get_user_reimbursement(user_id, args)
    # elif args == "approved":
    #     return f"Args {args} at Controller"
    # elif args == "denied":
    #     return f"Args {args} at Controller"
    if args:
        return ReimbursementService.get_user_reimbursement_args(user_id, args)
    else:
        return ReimbursementService.get_user_reimbursement(user_id)
