from model.reimbursement import Reimbursement


class ReimbursementUtility:
    @staticmethod
    def reimbursement_format(user_reimbursements):
        user_reimbursements_list = user_reimbursements["success"]
        user_reimbursements_formatted = []
        for user in user_reimbursements_list:
            reimb_id = user[0]
            reimbursement_amount = user[1]
            submitted_at = user[2]
            resolved_at = user[3]
            status = user[4]
            type_of_expense = user[5]
            description = user[6]
            receipt_img = user[9]
            reimb_author = user[7]
            reimb_resolver = user[8]

            user_reimbursements_formatted_in_dict = Reimbursement(reimb_id, reimbursement_amount, submitted_at,
                                                                  resolved_at, status, type_of_expense,
                                                                  description,
                                                                  reimb_author, reimb_resolver, receipt_img).to_dict()
            user_reimbursements_formatted.append(user_reimbursements_formatted_in_dict)

        return user_reimbursements_formatted
