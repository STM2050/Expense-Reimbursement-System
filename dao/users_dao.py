import psycopg
from decouple import config  # to create environment variable.

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

                return {"user_info": user_info}


