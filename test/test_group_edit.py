# -*- coding: utf-8 -*-
from model.group import Group


def test_group_edit(app):
    if app.group.count() == 0:
        app.group.add(Group(name="Группа для редактирования", header="Заголовок", footer="Подвал"))
    modified_group = app.group.edit_first(
        Group(name="Отредактированная группа", header="Новый заголовок", footer="Новый подвал"))
