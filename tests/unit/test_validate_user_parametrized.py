import pytest
from src.user_validation import validate_user

@pytest.mark.parametrize(
        "username, password, age, expected_result",
        [
            ('admin', '1234', 20, 'Access granted!'),
            ('alex', '1234', 20, 'Invalid username!'),
            ('admin', '0000', 20, 'Invalid password!'),
            ('alex', '0000', 20, 'Invalid username!'),
            ('admin', '1234', 15, 'Access denied - underage user!'),
            ('admin', '1234', 17, 'Access denied - underage user!'),
            ('admin', '1234', 18, 'Access granted!'),
            ('alex', '0000', 10, 'Access denied - underage user!'),
            ('', '1234', 20, 'Invalid username!'),
            ('admin', '', 20, 'Invalid password!')
        ]
)

def test_validate_user(username, password, age, expected_result):
    result = validate_user(username, password, age)
    assert result == expected_result