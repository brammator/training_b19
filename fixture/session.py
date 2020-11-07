# -*- coding: utf-8 -*-
from fixture.common import WebDriverHelper


class SessionHelper(WebDriverHelper):
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        self.fill_field("user", username)
        self.fill_field("pass", password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("pass")
