APP_STYLE = 'Fusion'
DB_LOCATION = '../NotCode/User_db.db'
IMPORT_MODULE_DIR = '../Temp_files/import_block.csv'
ONLY_LOGIN = """SELECT * FROM auth_data
        WHERE login = ? """
INSERT_DATA = """INSERT INTO auth_data(login, password)  
                        VALUES(?, ?)"""
GET_LOGGED_USER_ID = """SELECT id FROM auth_data
        WHERE login = ? and password = ?"""
NEW_MODULE_DB = """CREATE TABLE User_module_{} (
    id       INTEGER PRIMARY KEY AUTOINCREMENT
                     UNIQUE
                     NOT NULL,
    word     STRING  NOT NULL,
    meaning  STRING  NOT NULL,
    learning INTEGER DEFAULT (0) 
                     NOT NULL
);"""
INSERT_ROW_TO_DB = """INSERT INTO User_module_{} (word, meaning) VALUES(?, ?)"""
GET_LAST_MODULE_ID = """SELECT MAX(module_id) from user_modules"""
USER_MODULE_SAVE_DATA = """INSERT INTO user_modules(id_user,module_name, module_id) VALUES(?, ?, ?)"""
GET_MODULE_ID_FROM_USER_MODULES = """SELECT module_id FROM user_modules WHERE id_user = ? and module_name = ?"""
GET_MODULE_NAMES = """SELECT module_name, module_id FROM user_modules WHERE id_user = ? and is_deleted = False"""
get_words_from_db = """SELECT word, meaning FROM User_module_{}"""
DELETE_MODULE_FROM_DB = """UPDATE user_modules SET is_deleted = True WHERE module_id = ?"""
GET_MODULE_PROGRESS = """SELECT word, meaning, learning FROM User_module_{}"""
REMOVE_LEARNED_WORD = """UPDATE User_module_{} SET learning = 2 WHERE id = ?"""
GET_ID_WORDS_DEFINITIONS = """SELECT * FROM User_module_{}"""
GET_NAME_USER_ID = """SELECT id_user, module_name FROM user_modules WHERE module_id = ?"""
MODULE_LEANED_TEXT = "Модуль успешно пройден"
RESET_MODULE_PROGRESS = """UPDATE User_module_{} SET learning = 0 WHERE id = ?"""
