# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    old_groups = app.group.list()
    group = Group(name="Добавленная группа", header="Заголовок", footer="Подвал")
    app.group.add(group)
    new_groups = app.group.list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_group_add_empty(app):
    old_groups = app.group.list()
    group = Group(name="", header="", footer="")
    app.group.add(group)
    new_groups = app.group.list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
