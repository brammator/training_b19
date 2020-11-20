# -*- coding: utf-8 -*-
from model.group import Group


def test_group_edit(app):
    if app.group.count() == 0:
        app.group.add(Group(name="Группа для редактирования", header="Заголовок", footer="Подвал"))
    old_groups = app.group.list()
    group = Group(name="Отредактированная группа", header="Новый заголовок", footer="Новый подвал", id=old_groups[0].id)
    app.group.edit_first(group)
    new_groups = app.group.list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
