# -*- coding: utf-8 -*-
from fixture.common import WebDriverHelper


class ContactHelper(WebDriverHelper):

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_all(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_main_page()

    def del_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def del_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_all(contact)
        wd.find_element_by_name("update").click()

    def fill_all(self, contact):
        self.fill_field("firstname", contact.firstname)
        self.fill_field("middlename", contact.middlename)
        self.fill_field("lastname", contact.lastname)
        self.fill_field("nickname", contact.nickname)
        self.fill_field("title", contact.title)
        self.fill_field("company", contact.company)
        self.fill_field("address", contact.address)
        self.fill_field("home", contact.home)
        self.fill_field("mobile", contact.mobile)
        self.fill_field("work", contact.work)
        self.fill_field("fax", contact.fax)
        self.fill_field("email", contact.email)
        self.fill_field("email2", contact.email2)
        self.fill_field("email3", contact.email3)
        self.fill_field("homepage", contact.homepage)
        self.fill_field("bday", contact.bday)
        self.fill_field("bmonth", contact.bmonth)
        self.fill_field("byear", contact.byear)
        self.fill_field("aday", contact.aday)
        self.fill_field("amonth", contact.amonth)
        self.fill_field("ayear", contact.ayear)
        self.fill_field("address2", contact.address2)
        self.fill_field("phone2", contact.phone2)
        self.fill_field("notes", contact.notes)

    def count(self):
        self.app.open_home_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    def return_to_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home page").click()
