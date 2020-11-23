# -*- coding: utf-8 -*-
from fixture.common import WebDriverHelper
from model.contact import Contact


class ContactHelper(WebDriverHelper):

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_all(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_main_page()
        self.cache = None

    def del_first(self):
        self.del_nth(0)

    def del_nth(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_nth(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div#content > div.msgbox")
        self.app.open_home_page()
        self.cache = None

    def del_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div#content > div.msgbox")
        self.app.open_home_page()
        self.cache = None

    def edit_first(self, contact):
        self.edit_nth(0, contact)

    def edit_nth(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_all(contact)
        wd.find_element_by_name("update").click()
        self.cache = None

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

    def list(self):
        if self.cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.cache = list(map(lambda e: Contact(id=e[0], firstname=e[1], lastname=e[2]),
                                zip(
                                    map(lambda e: e.get_attribute("value"),
                                        wd.find_elements_by_css_selector("tr[name=entry] > td:nth-child(1) > input")),
                                    map(lambda e: getattr(e, "text"),
                                        wd.find_elements_by_css_selector("tr[name=entry] > td:nth-child(3)")),
                                    map(lambda e: getattr(e, "text"),
                                        wd.find_elements_by_css_selector("tr[name=entry] > td:nth-child(2)")),
                                )))
        return self.cache

    def return_to_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home page").click()
