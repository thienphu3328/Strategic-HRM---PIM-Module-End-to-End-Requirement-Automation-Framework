import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ManagementPage(BasePage):
    PIM_MENU = "span:has-text('PIM')"
    ADD_EMPLOYEE_BUTTON = "button:has-text('Add')"

    FIRST_NAME = "input[name='firstName']"
    MIDDLE_NAME = "input[name='middleName']"
    LAST_NAME = "input[name='lastName']"

    EMPLOYEE_ID = "xpath=//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/div[2]/input"

    SAVE_BUTTON = "button:has-text('Save')"

    SUCCESS_MESSAGE = "xpath=//div[@id='oxd-toaster_1']/div/div/div[2]/p[2]"
    PERSONAL_DETAIL_HEADING = "h6:has-text('Personal Detail')"


    def open_management_page(self):
        self.page.wait_for_selector(self.PIM_MENU)
        self.click(self.PIM_MENU)
        self.page.wait_for_selector(self.ADD_EMPLOYEE_BUTTON)

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def input_first_name(self, first_name):
        self.fill(self.FIRST_NAME, first_name)

    def input_middle_name(self, middle_name):
        self.fill(self.MIDDLE_NAME, middle_name)

    def input_last_name(self, last_name):
        self.fill(self.LAST_NAME, last_name)

    def input_id(self, employee_id):
        self.fill(self.EMPLOYEE_ID, employee_id)
    
    def click_save(self):
        self.click(self.SAVE_BUTTON)

    #Thêm nhân viên
    def add_employee(self, first_name, middle_name, last_name, employee_id):

        self.click_add_employee()
        self.page.wait_for_selector(self.FIRST_NAME)

        self.input_first_name(first_name)
        self.input_middle_name(middle_name)
        self.input_last_name(last_name)
        self.input_id(employee_id)

        self.click_save()
        self.page.wait_for_selector(self.PIM_MENU)
    
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def get_firstname_error_message(self):
        return self.get_text("xpath=//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div/div/div/div[2]/div/span")
    
    def get_lastname_error_message(self):
        return self.get_text("xpath=//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div/div/div/div[2]/div[3]/span")
    
    def get_employee_id_error_message(self):
        return self.get_text("xpath=//span[contains(.,'Employee Id already exists')]")