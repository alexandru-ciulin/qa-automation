from python_fundamente import validate_user

def test_valid_login():
    result = validate_user('admin', '1234', 20)
    assert result == 'Acces permis!'

def test_invalid_username():
    result = validate_user('alex', '1234', 20)
    assert result == 'Username invalid!'

def test_invalid_password():
    result = validate_user('admin', '0000', 20)
    assert result == 'Parola invalida!'

def test_both_invalid_credentials():
    result = validate_user('alex', '0000', 20)
    assert result == 'Username invalid!'

def test_underage_user():
    result = validate_user('admin', '1234', 15)
    assert result == 'Acces interzis - minori!'

def test_age_17():
    result = validate_user('admin', '1234', 17)
    assert result == 'Acces interzis - minori!'

def test_age_exactly_18():
    result = validate_user('admin', '1234', 18)
    assert result == 'Acces permis!'

def test_underage_and_invalid_credentials():
    result = validate_user('alex', '0000', 10)
    assert result == 'Acces interzis - minori!'

def test_empty_username():
    result = validate_user('', '1234', 20)
    assert result == 'Username invalid!'

def test_empty_password():
    result = validate_user('admin', '', 20)
    assert result == 'Parola invalida!'