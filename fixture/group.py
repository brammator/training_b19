# -*- coding: utf-8 -*-
from fixture.common import WebDriverHelper


class GroupHelper(WebDriverHelper):
    def add(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # добавить новую группу
        wd.find_element_by_name("new").click()
        # заполнить форму добавления группы
        self.fill_all(group)
        # сохранить изменения
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_all(self, group):
        self.fill_field("group_name", group.name)
        self.fill_field("group_header", group.header)
        self.fill_field("group_footer", group.footer)

    def del_first(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def del_all(self):
        wd = self.app.wd
        self.open_groups_page()
        list(map(lambda x: x.click(), wd.find_elements_by_name("selected[]")))
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first()
        wd.find_element_by_name("edit").click()
        modified_group = wd.find_element_by_name("id").get_attribute("value")
        self.fill_all(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        return modified_group

    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()
