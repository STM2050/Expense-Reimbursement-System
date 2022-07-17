from decouple import config  # to create environment variable.
import psycopg
import json  # to jsonify image which is stored in bytea format in the database

API_HOST = config('host')
API_PORT = config('port')
API_DBNAME = config('dbname')
API_USER = config('user')
API_PASSWORD = config('password')


class ReimbursementDao:
    @staticmethod
    def get_user_reimbursement(user_id):
        if not ReimbursementDao.check_if_finance_manager(user_id):
            with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                                 password=API_PASSWORD) as conn:
                with conn.cursor() as cur:
                    cur.execute("select * from expense_reimbursement_system.reimbursements where reimb_author=%s",
                                (user_id,))

                    users_all_list = cur.fetchall()
                    new_list = []

                    for user in users_all_list:
                        user_list = list(user)
                        new_list.append(user_list)

                    for user in new_list:
                        for data in user:
                            if type(data) == bytes:
                                my_img = data
                                index_of_each_item = user.index(data)
                                user.pop(index_of_each_item)
                                json_str = json.dumps(my_img.decode('utf-8'))
                                user.append(json_str)

                    return new_list
        else:
            with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                                 password=API_PASSWORD) as conn:
                with conn.cursor() as cur:
                    cur.execute("select * from expense_reimbursement_system.reimbursements")

                    users_all_list = cur.fetchall()
                    new_list = []

                    for user in users_all_list:
                        user_list = list(user)
                        new_list.append(user_list)

                    for user in new_list:
                        for data in user:
                            if type(data) == bytes:
                                my_img = data
                                index_of_each_item = user.index(data)
                                user.pop(index_of_each_item)
                                json_str = json.dumps(my_img.decode('utf-8'))
                                user.append(json_str)

                    return new_list

    @staticmethod
    def get_user_reimbursement_args(user_id, args):
        if not ReimbursementDao.check_if_finance_manager(user_id):
            with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                                 password=API_PASSWORD) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "select * from expense_reimbursement_system.reimbursements where reimb_author=%s and status=%s",
                        (user_id, args))

                    users_all_list = cur.fetchall()
                    new_list = []

                    for user in users_all_list:
                        user_list = list(user)
                        new_list.append(user_list)

                    for user in new_list:
                        for data in user:
                            if type(data) == bytes:
                                my_img = data
                                index_of_each_item = user.index(data)
                                user.pop(index_of_each_item)
                                json_str = json.dumps(my_img.decode('utf-8'))
                                user.append(json_str)

                    return new_list
        else:
            with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                                 password=API_PASSWORD) as conn:
                with conn.cursor() as cur:
                    cur.execute("select * from expense_reimbursement_system.reimbursements where status=%s", (args,))

                    users_all_list = cur.fetchall()
                    new_list = []

                    for user in users_all_list:
                        user_list = list(user)
                        new_list.append(user_list)

                    for user in new_list:
                        for data in user:
                            if type(data) == bytes:
                                my_img = data
                                index_of_each_item = user.index(data)
                                user.pop(index_of_each_item)
                                json_str = json.dumps(my_img.decode('utf-8'))
                                user.append(json_str)

                    return new_list

    @staticmethod
    def check_if_finance_manager(user_id):
        role = 'finance_manager'
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from expense_reimbursement_system.users where username=%s and role=%s ",
                            (user_id, role))
                user_details = cur.fetchall()
                return user_details

    @staticmethod
    def create_reimbursement(user_id, data):
        try:
            reimbursement_amount = data["reimbursement_amount"]
            type_of_expense = data["type_of_expense"]
            description = data["description"]
            receipt_img = data["receipt_img"]
            with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                                 password=API_PASSWORD) as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "insert into expense_reimbursement_system.reimbursements(reimbursement_amount, type, description, receipt_img ,reimb_author) values(%s, %s, %s, %s,%s) RETURNING *",
                        (reimbursement_amount, type_of_expense, description, receipt_img, user_id))
                    reimbursement_just_created = cur.fetchone()
                    print(reimbursement_just_created)
                    return "New reimbursement successfully created"
        except psycopg.errors.ForeignKeyViolation:
            return None
