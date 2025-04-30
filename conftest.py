import pytest


@pytest.fixture(scope='session')
def login(playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page
    page.open_page('https://dev.abra-market.com/')
    page.click_login_button()
    page.fill_email_field('logego6633@hikuhu.com')
    page.fill_password_field('Password1!')
    #page.click_login_button_login_page()
    page.click_login_button()
    page.check_personal_block()
    yield page
    browser.close()
