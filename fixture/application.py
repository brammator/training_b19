# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.DEFAULT_WAIT_TIME = 5
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(self.DEFAULT_WAIT_TIME)
        self.session = SessionHelper(app=self)
        self.group = GroupHelper(app=self)
        self.contact = ContactHelper(app=self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.get("http://localhost/addressbook/")

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


