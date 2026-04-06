import logging
from pages.base_page import BasePage
from pages.management_page import ManagementPage


logger = logging.getLogger(__name__)


class SearchingEmployee(BasePage):

    EMPLOYEE_NAME = "xpath=//label[text()='Employee Name']/ancestor::div[contains(@class,'oxd-input-group oxd-input-field-bottom-space')]//input"
    EMPLOYEE_ID = "xpath=//div[@id='app']/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div[2]/input"

    SEARCH_BUTTON = "button:has-text('Search')"

    RECORD_FOUND = "span:has-text('Records Found')"
    
    def input_employee_name(self, employee_name):
        self.fill(self.EMPLOYEE_NAME, employee_name)
    
    def input_employee_id(self, employee_id):
        self.fill(self.EMPLOYEE_ID, employee_id)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def search_employee_by_name(self, employee_name):
        self.input_employee_name(employee_name)
        self.click_search()
    
    def get_record_count(self):
        self.get_text(self.RECORD_FOUND)

        # Ví dụ: "(50) Records Found"
        import re
        number = re.search(r"\d+", self.get_text(self.RECORD_FOUND))

        return int(number.group())

    def search_employee_by_id(self, employee_id):
        self.input_employee_id(employee_id)
        self.click_search()

    
