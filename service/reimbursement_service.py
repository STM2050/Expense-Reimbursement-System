from dao.reimbursement_dao import ReimbursementDao
from utility.reimbursent_format import ReimbursementUtility


class ReimbursementService:
    @staticmethod
    def get_user_reimbursement(user_id):
        user_reimbursements = ReimbursementDao.get_user_reimbursement(user_id)
        user_reimbursements_formatted = ReimbursementUtility.reimbursement_format(user_reimbursements)

        return {f"Reimbursement details of {user_id}": user_reimbursements_formatted}
