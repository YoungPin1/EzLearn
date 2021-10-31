app_style = 'Fusion'
db_location = '../NotCode/EzLearndb.db'
import_module_dir = '../Temp_files/import_block.csv'
user_created_dir = '../Temp_files/user_block.csv'
only_login = """SELECT * FROM auth_data
        WHERE login = ? """
insert_data = """INSERT INTO auth_data(login, password)  
                        VALUES(?, ?)"""
get_logged_user_id = """SELECT id FROM auth_data
        WHERE login = ? and password = ?"""
new_module_db = """CREATE TABLE [{}] (
    id      INTEGER PRIMARY KEY AUTOINCREMENT
                    UNIQUE
                    NOT NULL,
    word    STRING  NOT NULL,
    meaning STRING  NOT NULL
)"""
insert_row_to_db = """INSERT INTO '{}' (word, meaning) VALUES(?, ?)"""
user_module_save_data = """INSERT INTO user_modules(id_user,module_name) VALUES(?, ?)"""
get_module_id_from_user_modules = """SELECT module_id FROM user_modules WHERE id_user = ? and module_name = ?"""
