from flask import Blueprint, request
from service.users_service import UserService

uc = Blueprint("user_controller", __name__)


@uc.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    return UserService.user_login(username, password)