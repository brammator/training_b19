# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select

from fixture.common import WebDriverHelper


class ContactHelper(WebDriverHelper):

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        for field, value in contact.items():
            self.fill_field(field, value)
        wd.find_element_by_name("submit").click()
        self.return_to_main_page()

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def delete_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        form = wd.find_element_by_css_selector("form[action='edit.php']")
        modified_contact = form.find_element_by_name("id").get_attribute("value")
        for i in form.find_elements_by_tag_name("input"):
            if i.get_attribute("type") != "text":
                continue
            text = i.get_attribute("value")
            if i.get_attribute("name").endswith("year") and len(text) == 0:
                text = "1831"
            if len(text) == 0:
                i.send_keys(f"Отредактированный элемент {i.get_attribute('name')}")
            elif text[::-1] == text:
                i.send_keys(" (отредактировано)")
            else:
                i.clear()
                i.send_keys(text[::-1])
        for i in form.find_elements_by_tag_name("textarea"):
            text = i.get_attribute("value")
            if len(text) == 0:
                i.send_keys(f"Отредактированный элемент {i.get_attribute('name')}")
            elif text[::-1] == text:
                i.send_keys(" (отредактировано)")
            else:
                i.clear()
                i.send_keys(text[::-1])
        for i in form.find_elements_by_tag_name("select"):
            options = i.find_elements_by_tag_name("option")
            for j, k in enumerate(options[1:], 1):
                if k.get_attribute("value") == options[0].get_attribute("value"):
                    # print(f"field {i.get_attribute('name')} has value #{j} {k.get_attribute('value')}, "
                    #       f"setting #{j-1} {options[j-1].get_attribute('value')}")
                    if j > 1:
                        options[j - 1].click()
                        break
                    else:
                        options[-1].click()
                        break
        form.find_element_by_name("update").click()
        return modified_contact

    def return_to_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

