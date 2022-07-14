from decouple import config
import psycopg
import base64
import json

API_HOST = config('host')
API_PORT = config('port')
API_DBNAME = config('dbname')
API_USER = config('user')
API_PASSWORD = config('password')


class UserDao:
    @staticmethod
    def get_user_reimbursement(user_id):
        with psycopg.connect(host=API_HOST, port=API_PORT, dbname=API_DBNAME, user=API_USER,
                             password=API_PASSWORD) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from expense_reimbursement_system.reimbursements;")
                # cur.execute(
                #     "select reimbursement_amount, type, description, reimb_author from expense_reimbursement_system.reimbursements;")
                # print(f"cur is {cur}")
                users_all_list = cur.fetchall()
                new_list = []

                # for user in users_all_list:
                #     for data in user:
                #         # print(f"{data} is type {type(data)}")
                #         if type(data) == bytes:
                #             my_img = data
                #             json_str = json.dumps(my_img.decode('utf-8'))
                #             new_list.append(json_str)
                #         else:
                #             new_list.append(data)
                # print(f"new_list: {new_list}")
                # # print(f"Fetch Dats is {users_all_list[1][-3]}")
                # # print(f"Fetch Dats is {type(users_all_list[1][-3])}")
                # # print(f"Data type is {type(users_all_list[0])}")
                # return{"success":  new_list}
                # # return {'success': f"{list(map(lambda x: {'emp': x}, users_all_list))}"}

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

                print(new_list)
                print(f"num of elements = {len(new_list)}")
                return {"success": new_list}
