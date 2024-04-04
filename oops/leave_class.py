from base_class import BaseClass
import time
import datetime as DT


class LeaveClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.APPLY_TAB = 'Apply'
        self.MY_LEAVE_TAB = 'My Leave'
        self.LEAVE_TYPE = 'CAN - FMLA'
        self.PARTIAL_DAYS = 'All Days'
        self.DURATION = 'Half Day - Morning'
        self.from_date = DT.datetime.now() - DT.timedelta(days=1)
        self.to_date = DT.datetime.now()
        self.CANCEL_XPATH = "//button[contains(normalize-space(), 'Cancel')]"

    def open_leave_page(self):
        self.explicit_wait(locator_tag=self.XPATH, locator="//span[text()='Leave']").click()

    def __choose_tab(self, link_text: str):
        self.explicit_wait(self.LINK_TEXT, link_text).click()

    def __choose_from_dropdown(self, option_text: str):
        self.driver.find_element(self.XPATH, "//div[contains(text(),'Select')]").click()
        self.explicit_wait(self.XPATH, f"//span[contains(text(),'{option_text}')]").click()

    def __choose_date(self, date_info: DT.datetime, index: int):
        self.explicit_wait(self.XPATH, "//input[contains(@placeholder,'yyyy')]", multiple=True)[index].click()
        self.explicit_wait(self.XPATH,
                           f"//div[@class='oxd-calendar-dates-grid']//div[text()='{date_info.day}']").click()

    # OPEN LEAVE APPLICATION TAB
    def choose_apply_tab(self):
        self.__choose_tab(self.APPLY_TAB)

    # SELECT LEAVE TYPE
    def choose_leave_type(self):
        self.__choose_from_dropdown(option_text=self.LEAVE_TYPE)

    # SELECT PARTIAL DAYS
    def choose_working_partial_days(self):
        self.__choose_from_dropdown(option_text=self.PARTIAL_DAYS)

    # SELECT DURATION
    def choose_partial_days_working_duration(self):
        self.__choose_from_dropdown(option_text=self.DURATION)

    # SELECT FROM DATE
    def choose_from_date(self):
        self.__choose_date(date_info=self.from_date, index=0)

    # SELECT TO DATE
    def choose_to_date(self):
        time.sleep(1)
        self.__choose_date(date_info=self.to_date, index=1)

    # COMMENT ON THE LEAVE
    def comment_for_leave(self, content: str):
        comment = f"{content} :- from {self.from_date.date()} to {self.to_date.date()}"
        self.explicit_wait(self.XPATH, " //textarea").send_keys(comment)

    # OPEN MY LEAVE TAB
    def choose_my_leave_tab(self):
        self.__choose_tab(self.MY_LEAVE_TAB)

    # VIEW LEAVE DETAILS
    def view_leave_details(self, msg: str):
        self.explicit_wait(self.XPATH,
                           f"//div[contains(text(),'{msg}')]/parent::div/following-sibling::div/div/li/button").click()

        self.explicit_wait(self.XPATH, "//p[text() = 'View Leave Details']").click()

    def cancel_all_leave_applications(self):
        cancel_btn_count = len(self.explicit_wait(self.XPATH, self.CANCEL_XPATH, multiple=True))
        for _ in range(cancel_btn_count):
            self.explicit_wait(self.XPATH, self.CANCEL_XPATH).click()
