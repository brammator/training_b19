# -*- coding: utf-8 -*-
from model.group import Group


def test_group_del_first(app):
    if app.group.count() == 0:
        app.group.add(Group(name="Группа для удаления"))
    app.group.del_first()


def test_group_del_all(app):
    if app.group.count() == 0:
        app.group.add(Group())
    app.group.del_all()
