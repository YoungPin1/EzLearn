import sqlite3

from constants import *


class Database:
    def __init__(self):
        self.con = sqlite3.connect(DB_LOCATION)
        self.cur = self.con.cursor()

    def get_log_pswd_db(self, login_inp):
        res = self.cur.execute(ONLY_LOGIN, (login_inp,)).fetchone()
        return res

    def save_user_id(self, login_inp, pswd_inp):
        logged_user_id = self.cur.execute(GET_LOGGED_USER_ID, (login_inp, pswd_inp)).fetchall()[0][0]
        return logged_user_id

    def insert_to_db(self, login_inp, pswd_inp):
        self.cur.execute(INSERT_DATA, (login_inp, pswd_inp)).fetchall()
        self.con.commit()

    def get_module_names(self, logged_user_id):
        return [i for i in self.cur.execute(GET_MODULE_NAMES, (logged_user_id,)).fetchall()]

    def create_db_table(self, logged_user_id, table_name):
        module_id = int(self.cur.execute(GET_LAST_MODULE_ID).fetchone()[0]) + 1
        self.cur.execute(USER_MODULE_SAVE_DATA, (logged_user_id, table_name, module_id)).fetchone()
        self.con.commit()
        return module_id

    def add_row_to_db(self, row, module_id):
        self.cur.execute(INSERT_ROW_TO_DB, (str(row[0]), str(row[1]), module_id)).fetchone()
        self.con.commit()

    def words_from_db(self, module_id):
        return self.cur.execute(GET_WORDS_FROM_DB, (module_id,)).fetchall()

    def delete(self, module_id):
        self.cur.execute(DELETE_MODULE_FROM_DB, (module_id,)).fetchall()
        self.con.commit()

    def get_progress(self, module_id):
        return self.cur.execute(GET_MODULE_PROGRESS, (module_id,)).fetchall()

    def mark_as_learned(self, level, module_id, id):
        self.cur.execute(REMOVE_LEARNED_WORD, (level, id, module_id)).fetchall()
        self.con.commit()

    def get_all_data_module(self, module_id):
        return self.cur.execute(GET_ID_WORDS_DEFINITIONS, (module_id,)).fetchall()

    def get_name_id(self, module_id):
        return self.cur.execute(GET_NAME_USER_ID, (module_id,)).fetchall()

    def reset_progress(self, module_id):
        self.cur.execute(RESET_MODULE_PROGRESS, (module_id,)).fetchall()
        self.con.commit()
