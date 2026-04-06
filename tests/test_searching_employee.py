from config.settings import BASE_URL
from pages.management_page import ManagementPage
from pages.login_page import LoginPage
from pages.searching_employee import SearchingEmployee

#TC_001: Search random check function searching
def test_searching_random(page):
    
    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Open PIM
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Search
    searching_employee = SearchingEmployee(page)

    before_record = searching_employee.get_record_count()
    searching_employee.search_employee_by_name("a")
    after_record = searching_employee.get_record_count()

    assert after_record < before_record

#TC_002: Searching bằng tên với nhân viên vừa tạo mới
def test_search_new_employee(page):
    
    #Login trước khi thêm nhân viên
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý nhân viên
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Thêm nhân viên chưa có trong Data
    management_page.add_employee("John", "", "Doe", "12345")

    #quay về trang quản lý và search
    management_page.open_management_page()

    searching_employee = SearchingEmployee(page)
    before_record = searching_employee.get_record_count()

    # Search theo tên full name (có thể first + last)
    searching_employee.search_employee_by_name("John Doe")
    after_record = searching_employee.get_record_count()

    assert after_record < before_record

