from login_page import LoginPage


def test_login(login):
    page = LoginPage(login)
    page.open_page('https://dev.abra-market.com/')
    page.click_login_button()
    page.fill_email_field('logego6633@hikuhu.com')
    page.fill_password_field('Password1!')
    #page.click_login_button_login_page()
    page.click_login_button()
    page.check_personal_block()