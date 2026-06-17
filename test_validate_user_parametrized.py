import pytest
from python_fundamente import validate_user

@pytest.mark.parametrize(
        "username, password, age, expected_result",
        [
            ('admin', '1234', 20, 'Acces permis!'),
            ('alex', '1234', 20, 'Username invalid!'),
            ('admin', '0000', 20, 'Parola invalida!'),
            ('alex', '0000', 20, 'Username invalid!'),
            ('admin', '1234', 15, 'Acces interzis - minori!'),
            ('admin', '1234', 17, 'Acces interzis - minori!'),
            ('admin', '1234', 18, 'Acces permis!'),
            ('alex', '0000', 10, 'Acces interzis - minori!'),
            ('', '1234', 20, 'Username invalid!'),
            ('admin', '', 20, 'Parola invalida!')
        ]
)

def test_validate_user(username, password, age, expected_result):
    result = validate_user(username, password, age)
    assert result == expected_result