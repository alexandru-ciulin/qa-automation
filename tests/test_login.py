from pages.login_page import LoginPage

def test_login_success(page, valid_credentials):
    login_page = LoginPage(page)

    login_page.login(valid_credentials["username"], valid_credentials["password"])

    assert "inventory" in page.url

def test_login_fail(page, invalid_credentials):
    login_page = LoginPage(page)

    login_page.login(invalid_credentials["username"], invalid_credentials["password"])

    assert page.get_by_text("Epic sadface: Username and password do not match any user in this service").is_visible()

