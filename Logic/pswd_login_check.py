def pswd_check(pswd):
    if len(pswd) == 0:
        return 'Введите пароль'
    if len(pswd) < 8:
        return 'Пароль слишком короткий '
    if pswd.lower() == pswd:
        return 'Нет заглавных символов'
    if pswd.upper() == pswd:
        return 'Все символы заглавные'
    if pswd.isdigit():
        return 'Все символы - цифры'
    if not any(map(str.isdigit, pswd)):
        return 'Нет цифр'
    return 'good'


def login_check(login):
    if len(login) == 0:
        return 'Введите логин'
    if len(login) < 5:
        return 'Логин слишком короткий '
    if ' ' in login:
        return 'Используется пробел'
    if login.isdigit():
        return 'Все символы - цифры'
    if login.lower() == login:
        return 'Нет заглавных символов'
    if login.upper() == login:
        return 'Нет строчных символов'
    if not any(map(str.isdigit, login)):
        return 'Нет цифр'
    return 'good'

login_check('123123123')