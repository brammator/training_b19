# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    app.group.add(Group(name="Добавленная группа", header="Заголовок", footer="Подвал"))


def test_group_add_empty(app):
    app.group.add(Group(name="", header="", footer=""))