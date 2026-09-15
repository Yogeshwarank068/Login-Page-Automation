from pages.login_page import LoginPage

def test_valid(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    login_page = LoginPage(driver)
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()
    driver.get_screenshot_as_file("screenshot.png")
    assert "Logged In Successfully" in driver.page_source