# Дизайны
APP_STYLE = 'Fusion'
DB_LOCATION = '../NotCode/User_db.db'
IMPORT_MODULE_DIR = '../Temp_files/import_block.csv'
MAIN_LEARN_DESIGN = '../Designs/learn_main.ui'
AUTHORIZATION_DESIGN = '../Designs/authorization.ui'
EZMAIN_DESIGN = '../Designs/main_window.ui'
ADD_MODULE_DESIGN = '../Designs/add_module.ui'
LEARN_WRITE_DESIGN = '../Designs/learn_write.ui'
LEARN_BH_DESIGN = '../Designs/learn_bh.ui'
LEARN_CARDS_DESIGN = '../Designs/learn_cards.ui'

# запросы в базу данных
ONLY_LOGIN = """SELECT * FROM auth_data
        WHERE login = ? """
INSERT_DATA = """INSERT INTO auth_data(login, password)  
                        VALUES(?, ?)"""
GET_LOGGED_USER_ID = """SELECT id FROM auth_data
        WHERE login = ? and password = ?"""
INSERT_ROW_TO_DB = """INSERT INTO words (word, meaning, module_id) VALUES(?, ?, ?)"""
GET_LAST_MODULE_ID = """SELECT MAX(module_id) from user_modules"""
USER_MODULE_SAVE_DATA = """INSERT INTO user_modules(id_user,module_name, module_id) VALUES(?, ?, ?)"""
GET_MODULE_ID_FROM_USER_MODULES = """SELECT module_id FROM user_modules WHERE id_user = ? and module_name = ?"""
GET_MODULE_NAMES = """SELECT module_name, module_id FROM user_modules WHERE id_user = ? and is_deleted = False"""
GET_WORDS_FROM_DB = """SELECT word, meaning FROM words WHERE module_id = ?"""
DELETE_MODULE_FROM_DB = """UPDATE user_modules SET is_deleted = True WHERE module_id = ?"""
GET_MODULE_PROGRESS = """SELECT * FROM words WHERE module_id = ?"""
REMOVE_LEARNED_WORD = """UPDATE words SET learning = ? WHERE word_id = ? and module_id = ?"""
GET_ID_WORDS_DEFINITIONS = """SELECT * FROM words WHERE module_id = ?"""
GET_NAME_USER_ID = """SELECT id_user, module_name FROM user_modules WHERE module_id = ?"""
RESET_MODULE_PROGRESS = """UPDATE words SET learning = 0 WHERE module_id = ?"""

# Текст
MODULE_LEANED_TEXT = "Модуль успешно пройден"
OK = 'ok'
SIGN_IN = 'sign_in'
SIGN_UP = 'sign_up'
USER_EXISTS = 'Такой пользователь уже существует'
ENTER_LOGIN = 'Введите логин'
USER_DOES_NOT_EXIST = 'Такого пользователя не существует'
ENTER_PASSWORD = 'Введите пароль'
WROGN_PASSWORD = 'Неправильный пароль'
EDIT_MODULE_TEXT = 'Редактировать учебный модуль'
DELETE_MESSAGE = "Все ваши данные не будут сохранены\n Вы точно хотите выйти?"
SUCCESS_MESSAGE = "Модуль успешно сохранен\n Возвращаю на главную страницу"
MESSAGE = 'Сообщение'
SEPARATOR = "Разделитель"
IMPORT_DIALOG_MESSAGE = "Введите delimiter и quotechar\nвашего файла через пробел"
NO_LESS_THAN_5_WORDS = 'Введите не менее 5 слов'
DELETE_MODULE_TEXT = "Модуль будет удален без возможности восстановления\n Вы точно хотите выйти?"
MESSAGE_SAVED = "Модуль успещно сохранен"
MODULE_RESET = "После редактирования прогресс будет сброшен\n Вы точно хотите изменить модуль?"
BLOCK_LEARNED = 'Блок успешно пройден'

# Стайл шит
GREEN_BTN_STYLE = 'background-color:green;color:white;'
RED_BTN_STYLE = 'background-color:red;color:white;'
NORMAL_STYLE_SHEET = 'background-color: rgb(242, 180, 0); color: rgb(255, 255, 255);'
LEDIT_WHITE = 'color:white;'
LEDIT_RED = 'color:red;'
LEDIT_GREEN = 'color:green;'
TABLE_STYLE_SHEET = "::section{Background-color:rgb(40,40,40)}"
WHITE_COLOR = 'color : white'