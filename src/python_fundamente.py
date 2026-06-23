def validate_user(username_input, password_input, age_input):
    username = 'admin'
    password = '1234'
    min_age = 18

    if age_input >= min_age:
        if username_input != username:
            return 'Username invalid!'
        elif password_input != password:
            return 'Parola invalida!'
        else:
            return 'Acces permis!'
    else:
        return 'Acces interzis - minori!'