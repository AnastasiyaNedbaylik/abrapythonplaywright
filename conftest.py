# import pytest
#
# from config import settings
#
#
# @pytest.fixture(scope='session')
# def login(playwright, base_url: settings.BASE_URL ,email: settings.EMAIL, password: settings.PASSWORD):
#     browser = playwright.chromium.launch()
#     context = browser.new_context()
#     page = context.new_page
#     page.open_page(base_url)
#     page.click_login_button()
#     page.fill_email_field(email)
#     page.fill_password_field(password)
#     #page.click_login_button_login_page()
#     page.click_login_button()
#     page.check_personal_block()
#     yield page
#     browser.close()
