from flask import Blueprint, request, session

from service.users_service import UserService
from exception.user_name_not_found import UserNotFoundError
from exception.log_in_error import LogInError

uc = Blueprint("user_controller", __name__)


@uc.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    try:
        # Create an HTTP session object and associate with the user that is logged in with a key within the HTTP session
        # We add a key to the Http session object called "user_info" that contains the dictionary with all the user information.
        # Any subsequent request that is made by the client will be identified with the appropriate Http session object that contains that key
        user_info = UserService.user_login(username, password)
        session["user_info"] = user_info
        return user_info
    except LogInError as e:
        return {"message": str(e)}, 401


@uc.route("/loginstatus")
def loginstatus():
    if session.get("user_info"):
        return{
            "message": "You are logged in",
            "logged_in_user": session.get("user_info")
        }
    else:
        return "You are not logged in"
