from pages.login_page import LoginPage
from config.settings import BASE_URL

#TC_001: ĐĂNG NHẬP VỚI TÀI KHOẢN VÀ MẬT KHẨU HỢP LỆ
def test_login_with_valid_input_data(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "admin123")
    login_page.page.wait_for_selector("h6:has-text('Dashboard')")
    
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

#TC_002: ĐĂNG NHẬP VỚI MẬT KHẨU KHÔNG HỢP LỆ
def test_login_with_invalid_password(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "invalid_password")
    
    error_message = login_page.get_error_message()
    assert error_message == "Invalid credentials"

#TC_003: ĐĂNG NHẬP VỚI USERNAME RỖNG
def test_login_with_empty_username(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("", "admin123")

    username_error = login_page.get_username_error_message()
    assert username_error == "Required"

#TC_004: ĐĂNG NHẬP VỚI MẬT KHẨU RỖNG
def test_login_with_empty_password(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("Admin", "")

    password_error = login_page.get_password_error_message()
    assert password_error == "Required"


#TC_005: ĐĂNG NHẬP VỚI USERNAME VÀ MẬT KHẨU RỖNG
def test_login_with_empty_username_and_password(page):
    login_page = LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login("", "")

    username_error = login_page.get_username_error_message()
    password_error = login_page.get_password_error_message()
    assert username_error == "Required"
    assert password_error == "Required"