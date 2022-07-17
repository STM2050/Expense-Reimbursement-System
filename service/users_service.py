from dao.users_dao import UsersDao
from exception.user_name_not_found import UserNotFoundError


class UserService:
    @staticmethod
    def user_login(username, password):
        user_info = UsersDao.user_login(username, password)
        if user_info:
            return user_info
        raise UserNotFoundError("Username and Password does not match. Please try again with correct credentials !!!")
