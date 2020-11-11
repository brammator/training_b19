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

    def ensure_logged(self, username=None, password=None):
        current_user = self.logged_username
        if username is None and current_user is not None:
            self.logout()
        elif username is not None and current_user is None:
            self.login(username, password)
        elif username is not None and username != current_user:
            self.logout()
            self.login(username, password)
        else:
            pass  # (user, current == None) || (user == current)

    @property
    def logged_username(self):
        wd = self.app.wd
        try:
            wd.implicitly_wait(1)
            form = wd.find_element_by_css_selector("form.header[name='logout']")
            form.find_element_by_css_selector("input[type='hidden'][name='logout']")
            username = form.find_element_by_tag_name("b").text[1:-1]
            wd.implicitly_wait(self.app.DEFAULT_WAIT_TIME)
            return username
        except:
            wd.implicitly_wait(self.app.DEFAULT_WAIT_TIME)
            return None
