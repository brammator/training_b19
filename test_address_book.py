# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from selenium.webdriver.support.select import Select

from contact import Contact
from group import Group


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name="Family users", header="Простое лого", footer="Подвал группы"))
        self.return_to_groups_page()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_groups_page()
        self.create_group(Group(name="", header="", footer=""))
        self.return_to_groups_page()
        self.logout()

    def test_add_contact(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                 title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
                 mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35", email="cdur@oldfiction.book",
                 homepage="localhost/addressbook", bday="1", bmonth="February", byear="1816", aday="30",
                 amonth="October", ayear="2020", address2="Msk", phone2="ditto", notes="What are you, Oleg"))
        self.return_to_main_page()
        self.logout()

    def test_add_empty_contact(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.create_contact(Contact())
        self.return_to_main_page()
        self.logout()

    def return_to_main_page(self):
        self.wd.find_element_by_link_text("home page").click()

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

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        self.wd.find_element_by_link_text("group page").click()

    def create_group(self, group):
        wd = self.wd
        # добавить новую группу
        wd.find_element_by_name("new").click()
        # заполнить форму добавления группы
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # сохранить изменения
        wd.find_element_by_name("submit").click()

    def open_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.wd.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
