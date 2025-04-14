def validate_username_password(username, password):
    if len(username) < 3 or len(password) < 6:
        return False
    return True
