def check_login_pswd(self, login_inp, pswd_inp, origin='sign_up', db_log_pswd=None):
    try:
        if len(login_inp) == 0:
            raise Exception('Введите логин')
        elif origin == 'sign_in' and db_log_pswd is None:
            raise Exception('Такого пользователя не существует')
        elif len(pswd_inp) == 0:
            return 'Введите пароль'
        elif origin == 'sign_in' and pswd_inp != str(db_log_pswd[2]):
            raise Exception('Неправильный пароль')
        else:
            raise Exception('ok')
    except Exception as error:
        return str(error)