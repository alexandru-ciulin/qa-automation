class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com")


    def login(self, username, password):
        self.open ()
        
        self.page.get_by_placeholder("Username").fill(username)

        self.page.get_by_placeholder("Password").fill(password)

        self.page.get_by_role("button", name="Login").click()

    def is_error_message_visible(self):
        return self.page.get_by_text("Epic sadface: Username and password do not match any user in this service").is_visible()