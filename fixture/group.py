# -*- coding: utf-8 -*-


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # добавить новую группу
        wd.find_element_by_name("new").click()
        # заполнить форму добавления группы
        for field, value in group.items():
            element = wd.find_element_by_name(field)
            element.clear()
            element.send_keys(value)
        # сохранить изменения
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def delete_all(self):
        wd = self.app.wd
        self.open_groups_page()
        list(map(lambda x: x.click(), wd.find_elements_by_name("selected[]")))
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify_first(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        modified_group = wd.find_element_by_name("id").get_attribute("value")
        for i in wd.find_elements_by_css_selector("div#content>form>[name^='group_']"):
            text = i.get_attribute("value")
            if len(text) == 0:
                i.send_keys(f"Отредактированный элемент {i.get_attribute('name')}")
            elif text[::-1] == text:
                i.send_keys(" (отредактировано)")
            else:
                i.clear()
                i.send_keys(text[::-1])
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()
        return modified_group

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

