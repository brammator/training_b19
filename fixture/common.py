# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select


class WebDriverHelper:
    def __init__(self, app):
        self.app = app

    def fill_field(self, field, value, scope=None):
        if scope is None:
            scope = self.app.wd
        e = scope.find_element_by_name(field)
        if e.tag_name == "input" and e.get_attribute("type") in ("text", "password"):
            e.clear()
            e.send_keys(value)
        elif e.tag_name == "select":
            Select(e).select_by_visible_text(value)
        elif e.tag_name == "textarea":
            e.clear()
            e.send_keys(value)
        else:
            raise KeyError(f"Unsupported field: {e.tag_name} / {e.get_attribute('type')}")
