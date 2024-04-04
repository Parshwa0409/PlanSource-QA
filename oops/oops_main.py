from base_class import BaseClass
from session_class import SessionClass
from leave_class import LeaveClass

from selenium import webdriver

# DRIVER SETUP
driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
driver.implicitly_wait(14)

comment = 'PSI293007-Leave-Application'

# ALL PAGES INSTANCE
base_page = BaseClass(driver=driver)
session_page = SessionClass(driver=driver)
leave_page = LeaveClass(driver=driver)

# SCRIPT
try:
    base_page.implicit_wait()
    session_page.login_admin()
    leave_page.open_leave_page()

    if leave_page.current_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList":
        print("LEAVE PAGE OPENED!!!")
    elif leave_page.current_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveModule":
        print("SERVICE UNAVAILABLE, TRYING AGAIN!!!!!")
        driver.back()
        leave_page.open_leave_page()
    else:
        raise Exception("UNABLE TO OPEN THE LEAVE PORTAL PAGE!!!!")

    leave_page.choose_apply_tab()
    leave_page.choose_leave_type()
    leave_page.choose_from_date()
    leave_page.choose_to_date()
    leave_page.choose_working_partial_days()
    leave_page.choose_partial_days_working_duration()
    leave_page.comment_for_leave(content=comment)
    leave_page.click_submit('Apply')
    leave_page.choose_my_leave_tab()
    leave_page.view_leave_details(msg=comment)
    leave_page.cancel_all_leave_applications()
    session_page.logout_admin()
except Exception as e:
    print(f'{e}')

input("Type something to exit/quit: ")
