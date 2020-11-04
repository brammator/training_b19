# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        for field, value in contact.items():
            element = wd.find_element_by_name(field)
            if field in contact._selects:  # FIXME: анализировать элемент страницы, а не данные
                Select(element).select_by_visible_text(value)
            else:
                element.clear()
                element.send_keys(value)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_main_page()

    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

