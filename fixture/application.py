# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(app=self)
        self.group = GroupHelper(app=self)
        self.contact = ContactHelper(app=self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

