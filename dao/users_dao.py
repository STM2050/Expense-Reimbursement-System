import psycopg
from decouple import config  # to create environment variable.
from model.user import User

API_HOST = config('host')
API_PORT = config('port')
API_DBNAME = config('dbname')
API_USER = config('user')
API_PASSWORD = config('password')


class UsersDao:
    @staticmethod
    def user_login(username, password):
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from expense_reimbursement_system.users where username=%s and password=%s",
                            (username, password))

                user_info = cur.fetchone()

                if not user_info:
                    return None

                username = user_info[1]
                first_name = user_info[3]
                last_name = user_info[4]
                role = user_info[6]
                return User(username, first_name, last_name, role)
