from dao.users_dao import UserDao
from utility.reimbursent_format import ReimbursementUtility


class UsersService:
    @staticmethod
    def get_user_reimbursement(user_id):
        user_reimbursements = UserDao.get_user_reimbursement(user_id)
        user_reimbursements_formatted = ReimbursementUtility.reimbursement_format(user_reimbursements)

        return {f"Reimbursement details of {user_id}": user_reimbursements_formatted}
