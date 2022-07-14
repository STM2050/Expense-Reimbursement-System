from dao.users_dao import UserDao


class UsersService:
    @staticmethod
    def get_user_reimbursement(user_id):
        user_reimbursements = UserDao.get_user_reimbursement(user_id)
        # print(user_reimbursements)
        # print(type(user_reimbursements))
        return user_reimbursements
