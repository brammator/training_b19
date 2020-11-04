# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(app=self)
        self.group = GroupHelper(app=self)

    def destroy(self):
        self.wd.quit()

    def create_contact(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        for field, value in contact.items():
            element = wd.find_element_by_name(field)
            if field in contact._selects:
                Select(element).select_by_visible_text(value)
            else:
                element.clear()
                element.send_keys(value)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_main_page()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def return_to_main_page(self):
        self.wd.find_element_by_link_text("home page").click()

