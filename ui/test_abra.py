from ui.login_page import LoginPage


def test_login(login):
    page = LoginPage(login)
    page.open_page('')
    page.click_login_button()
    page.fill_email_field('')
    page.fill_password_field('')
    #page.click_login_button_login_page()
    page.click_login_button()
    page.check_personal_block()
