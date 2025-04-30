from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        #self.LOGIN_BUTTON = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]/div/a[2]')
        self.LOGIN_BUTTON = self.page.get_by_text('Log in')
        #self.EMAIL_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[1]/input')
        self.EMAIL_FIELD = self.page.get_by_placeholder('Email')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="root"]/div/div/div/form/div[2]/input')
        self.LOGIN_BUTTON_LOGIN_PAGE = self.page.locator('//*[@id="root"]/div/div/div/form/button')
        self.PERSONAL_BLOCK = self.page.locator('//*[@id="root"]/div/div/header/div[1]/div/div[2]')

    def open_page(self, link):
        self.page.goto(link)

    def click_login_button(self):
        self.LOGIN_BUTTON.click()

    def fill_email_field(self,email):
        self.EMAIL_FIELD.fill(email)

    def fill_password_field(self,password):
        self.PASSWORD_FIELD.fill(password)
        self.EMAIL_FIELD.click()

    def click_login_button_login_page(self):
        self.LOGIN_BUTTON_LOGIN_PAGE.click()

    def check_personal_block(self):
        expect(self.PERSONAL_BLOCK).to_be_visible()