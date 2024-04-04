from classified import *

# LOGIN THE ADMIN
login_admin('username', 'password', 'Admin', 'admin123')

# OPEN THE LEAVE APPLICATION PAGE
try:
    open_leave_page()

    if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList":
        print("LEAVE PAGE OPENED!!!")
    elif driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveModule":
        print("SERVICE UNAVAILABLE, TRYING AGAIN!!!!!")
        driver.back()
        open_leave_page()
    else:
        raise Exception("UNABLE TO OPEN THE LEAVE PORTAL PAGE!!!!")

    # Once THE LINK IS OPENED THEN GO TO APPLY PAGE
    choose_from_nav('Apply')
except Exception as e:
    print(f'ERROR: WHILE OPENING LEAVE APPLICATION PAGE :==> {e}')

# SELECT LEAVE TYPE
choose_from_dropdown('CAN - FMLA')

# SELECT FROM DATE
from_date = DT.datetime.now() - DT.timedelta(days=1)
choose_date(from_date, 0)

# SELECT TO DATE
to_date = DT.datetime.now()
choose_date(to_date, 1)

# SELECT PARTIAL DAYS
choose_from_dropdown('All Days')

# SELECT DURATION
choose_from_dropdown('Half Day - Morning')

# COMMENT SOMETHING
msg = comment_for_leave(
    content='PSI-295-007 applying for a leave ',
    from_date=from_date,
    to_date=to_date,
)

# APPLY FOR LEAVE
wait_a_sec()
submit('Apply')

# NOW GO TO MY-LEAVE & THEN CLICK ON CANCEL
wait_a_sec()
choose_from_nav('My Leave')

wait_a_sec(3)
view_details(msg)

# CANCEL LEAVE APPLICATIONS
CANCEL_XPATH = "//button[contains(normalize-space(), 'Cancel')]"
cancel_btn_count = len(driver.find_elements(By.XPATH, CANCEL_XPATH))
wait_a_sec()

for i in range(0, cancel_btn_count):
    driver.find_element(By.XPATH, CANCEL_XPATH).click()
    wait_a_sec(2)

# LOGOUT
driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
wait_a_sec()
submit('Logout', 'a')

# END
input("TYPE SOMETHING TO EXIT: ")
