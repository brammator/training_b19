# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def destroy(self):
        self.wd.quit()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # добавить новую группу
        wd.find_element_by_name("new").click()
        # заполнить форму добавления группы
        wd.find_element_by_name("group_name").clear()   # FIXME вынести очистку и заполнение в отдельный метод
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # сохранить изменения
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

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

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def return_to_main_page(self):
        self.wd.find_element_by_link_text("home page").click()

    def return_to_groups_page(self):
        self.wd.find_element_by_link_text("group page").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        self.wd.find_element_by_link_text("Logout").click()
        self.wd.find_element_by_name("pass")
