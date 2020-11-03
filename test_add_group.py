# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from selenium.webdriver.support.select import Select

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
        self.create_contact()
        self.return_to_main_page()
        self.logout()

    def return_to_main_page(self):
        self.wd.find_element_by_link_text("home page").click()

    def create_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("John")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Vasilyevitch")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Doe")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Gryazny")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Cleanliness Director")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Dixyorochka")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("SPb")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("+78005553535")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("8-800-555-3535")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("8 (800) 555 3535")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("8 800 555 35 35")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("cdur@oldfiction.book")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("localhost/addressbook")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("February")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1816")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("30")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("October")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2020")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Msk")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("ditto")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("What are you, Oleg")
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
