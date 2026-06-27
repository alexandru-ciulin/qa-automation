def validate_user(username_input, password_input, age_input):
    VALID_USERNAME = 'admin'
    VALID_PASSWORD = '1234'
    MIN_AGE = 18

    if age_input >= MIN_AGE:
        if username_input != VALID_USERNAME:
            return 'Invalid username!'
        elif password_input != VALID_PASSWORD:
            return 'Invalid password!'
        else:
            return 'Access granted!'
    else:
        return 'Access denied - underage user!'