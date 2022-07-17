from flask import Blueprint, request
from service.users_service import UserService
from exception.user_name_not_found import UserNotFoundError

uc = Blueprint("user_controller", __name__)


@uc.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    try:
        return UserService.user_login(username, password)
    except UserNotFoundError as e:
        return str(e)
