import service.csv_proxy

# Pos: 0 -> ID
# Pos: 1 -> User
# Pos: 2 -> Password

USER_LOG_FILES = "./user-log.csv"
user_rows = []
service.csv_proxy.read(USER_LOG_FILES, user_rows)


def validate_user(user, password):
    try:
        for scoped_rows in user_rows:
            if scoped_rows[1] == user and scoped_rows[2] == password:
                return scoped_rows[0]
            else:
                return None
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")


def create_user(user, password):
    is_ok = True
    try:
        for scoped_rows in user_rows:
            if scoped_rows[1] == user:
                is_ok = False
        if is_ok:
            service.csv_proxy.write(USER_LOG_FILES, [[service.csv_proxy.get_last_id(user_rows) + 1, user, password]])
            service.csv_proxy.read(USER_LOG_FILES, user_rows)
        return is_ok
    except (AttributeError, TypeError, AssertionError):
        raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")
