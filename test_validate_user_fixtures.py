import pytest
from python_fundamente import validate_user

@pytest.fixture
def valid_user():
    return {
        'username' : 'admin',
        'password' : '1234',
        'age' : 20
    }

def test_valid_username(valid_user):
    user = valid_user.copy()
    user['username'] = 'admin'
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Acces permis!'

def test_invalid_username(valid_user):
    user = valid_user.copy()
    user['username'] = 'alex'
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Username invalid!'

def test_invalid_password(valid_user):
    user = valid_user.copy()
    user['password'] = '0000'
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Parola invalida!'

def test_invalid_credentials(valid_user):
    user = valid_user.copy()
    user['username'] = 'alex'
    user['password'] = '0000'
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Username invalid!'

def test_underage_age(valid_user):
    user = valid_user.copy()
    user['age'] = 15
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Acces interzis - minori!'

def test_age_17(valid_user):
    user = valid_user.copy()
    user['age'] = 17
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Acces interzis - minori!'

def test_age_18(valid_user):
    user = valid_user.copy()
    user['age'] = 18
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Acces permis!'

def test_underage_and_invalid_credentials(valid_user):
    user = valid_user.copy()
    user['username'] = 'alex'
    user['password'] = '0000'
    user['age'] = 10
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Acces interzis - minori!'

def test_empty_username(valid_user):
    user = valid_user.copy()
    user['username'] = ''
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Username invalid!'

def test_empty_password(valid_user):
    user = valid_user.copy()
    user['password'] = ''
    result = validate_user(
        user['username'],
        user['password'],
        user['age']
    )
    assert result == 'Parola invalida!'