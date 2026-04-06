from config.settings import BASE_URL
from pages.management_page import ManagementPage
from pages.login_page import LoginPage

#TC_001: Thêm nhân viên mới
def test_add_employee(page):

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
    

#TC_002: Thêm nhân viên không có first name
def test_add_employee_without_first_name(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Thêm nv không có first name
    management_page.add_employee("", "", "Doe", "12345")

    assert management_page.get_firstname_error_message() == "Required"

    

#TC_003: Thêm nhân viên không có last name
def test_add_employee_withou_last_name(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Thêm nv không có last name
    management_page.add_employee("John", "", "", "12345")

    assert management_page.get_lastname_error_message() == "Required"

    

#TC_004: first name và last name đều rổng

def test_add_empty_first_and_last_name(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Thêm nv không có first name và last name
    management_page.add_employee("", "", "", "12345")

    assert management_page.get_lastname_error_message() == "Required"


    

#TC_005: Ký tự đặc biệt trong first name

def test_add_special_characters_in_first_name(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Thêm nv có ký tự đặc biệt trong first name
    management_page.add_employee("John@123", "", "Doe", "12345")

    
    

#TC_006: Ký tự đặc biệt trong last name     
def test_add_special_characters_in_last_name(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Thêm nv có ký tự đặc biệt trong last name
    management_page.add_employee("John", "", "Doe@123", "12345")



#TC_007: employee ID để trống
def test_add_employee_id_empty(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()

    #Thêm nv có employee ID để trống
    management_page.add_employee("John", "", "Doe", "")

    


#TC_008: employee ID có ký tự đặc biệt
def test_add_employee_id_with_special_characters(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()
    
    #Thêm employee ID có ký tự đặc biệt
    management_page.add_employee("John", "", "Doe", "!!!")
    
    

#TC_009: employee ID đã tồn tại
def test_add_employee_with_existing_id(page):

    #Login
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    #Mở trang quản lý
    management_page = ManagementPage(page)
    management_page.open_management_page()
    
    #Thêm nhân viên với employee ID đã tồn tại
    management_page.add_employee("Jane", "", "Smith", "0249")
    
    assert management_page.get_employee_id_error_message() == "Employee Id already exists"

    


    