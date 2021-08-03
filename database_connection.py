"""Database working only with internet connection,
    app use remote database from elephant sql server to acces EVERYWHERE"""

import psycopg2


class DbConnect:
    def __init__(self, db_name, db_user, db_pass, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_host = db_host
        self.db_pass = db_pass
        self.db_port = db_port

    def check_db_connect(self):

        try:
            conn = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                host=self.db_host,
                password=self.db_pass,
                port=self.db_port,
            )
            print("DB CONNECT OK!")
            return True

        except:
            print("FAULT DB CONNECT")

    # @staticmethod
    # def select_test(self):

    #     DB_NAME = "xrwbllcp"
    #     DB_USER = "xrwbllcp"
    #     DB_HOST = "chunee.db.elephantsql.com"
    #     DB_PASS = "gxf8sd4dUvToKP1Ci0STU7KiPX40lXFS"
    #     DB_PORT = "5432"

    #     try:
    #         conn = psycopg2.connect(
    #             database=DB_NAME,
    #             user=DB_USER,
    #             host=DB_HOST,
    #             password=DB_PASS,
    #             port=DB_PORT,
    #         )
    #         print("DB CONNECT OK!")
    #         return True

    #     except:
    #         print("FAULT DB REMOTE CONNECT, Check intetnet connection!")

    # cur = conn.cursor()

    # insert_query = "SELECT * FROM methan_history;"
    # print(insert_query)
    # cur.execute(insert_query)
    # print(insert_query)
    # conn.close()


test_db_connection = DbConnect(
    "xrwbllcp",
    "xrwbllcp",
    "gxf8sd4dUvToKP1Ci0STU7KiPX40lXFS",
    "chunee.db.elephantsql.com",
    "5432",
)


test_db_connection.check_db_connect()
