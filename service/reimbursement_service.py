from dao.reimbursement_dao import ReimbursementDao
from utility.reimbursent_format import ReimbursementUtility
from exception.user_name_not_found import UserNotFoundError


class ReimbursementService:
    @staticmethod
    def get_user_reimbursement(user_id):
        user_reimbursements = ReimbursementDao.get_user_reimbursement(user_id)
        user_reimbursements_formatted = ReimbursementUtility.reimbursement_format(user_reimbursements)

        return {f"Reimbursement details of {user_id}": user_reimbursements_formatted}

    @staticmethod
    def get_user_reimbursement_args(user_id, args):
        user_reimbursements = ReimbursementDao.get_user_reimbursement_args(user_id, args)
        user_reimbursements_formatted = ReimbursementUtility.reimbursement_format(user_reimbursements)

        return {f"Reimbursement details of {user_id}": user_reimbursements_formatted}

    @staticmethod
    def create_reimbursement(user_id, data):
        new_reimbursement = ReimbursementDao.create_reimbursement(user_id, data)
        if new_reimbursement:
            return new_reimbursement
        raise UserNotFoundError(f"Username {user_id} not found !!!")
