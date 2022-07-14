class Reimbursement:
    def __init__(self, reimb_id, reimbursement_amount, submitted_at, resolved_at, status, type_of_expense, description,
                 reimb_author, reimb_resolver, receipt_img):
        self.reimb_id = reimb_id
        self.reimbursement_amount = reimbursement_amount
        self.submitted_at = submitted_at
        self.resolved_at = resolved_at
        self.status = status
        self.type_of_expense = type_of_expense
        self.description = description
        self.reimb_author = reimb_author
        self.reimb_resolver = reimb_resolver
        self.receipt_img = receipt_img

    def to_dict(self):
        return {
            "reimb_id": self.reimb_id,
            "reimbursement_amount": self.reimbursement_amount,
            "submitted_at": self.submitted_at,
            "resolved_at": self.resolved_at,
            "status": self.status,
            "type_of_expense": self.type_of_expense,
            "description": self.description,
            "reimb_author": self.reimb_author,
            "reimb_resolver": self.reimb_resolver,
            "receipt_img": self.receipt_img
        }
