from playwright.sync_api import sync_playwright

def test_open_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.google.ro")

        page.wait_for_timeout(3000)

        page.get_by_role("button", name="Acceptă tot").click()

        page.wait_for_timeout(30000)

        assert "Google" in page.title()

        browser.close()

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        assert "inventory" in page.url

        page.wait_for_timeout(30000)

        browser.close()

def test_products_after_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        locator = page.get_by_text("Products")

        assert locator.is_visible()

        browser.close()

def test_product_01():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        assert page.get_by_text("Sauce Labs Backpack").is_visible()

        browser.close

def test_all_products_6_in_total():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        products_count = page.get_by_role("button", name="Add to cart").count()

        assert products_count == 6
        # assert products_count == 5

        browser.close

