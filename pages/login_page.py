import logging
import pages.base_page as BasePage

logger = logging.getLogger(__name__)
 
class LoginPage(BasePage.BasePage):
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".oxd-alert-content-text"
    USERNAME_ERROR = "div.oxd-input-group:has(input[name='username']) .oxd-input-field-error-message"
    PASSWORD_ERROR = "div.oxd-input-group:has(input[name='password']) .oxd-input-field-error-message"

    def navigate(self, url):
        self.page.goto(url)

    def input_usernam(self, username):
        self.fill(self.USERNAME_INPUT, username)

    def  input_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    
    #Login
    def login(self, username, password):
        self.input_usernam(username)
        self.input_password(password)
        self.click_login()
        

    #Get error message
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    #Get username required message
    def get_username_error_message(self):
        return self.get_text(self.USERNAME_ERROR)

    #Get password required message
    def get_password_error_message(self):
        return self.get_text(self.PASSWORD_ERROR)