# -*- coding: utf-8 -*-
from random import randrange

import pytest

from model.group import Group


# @pytest.mark.parametrize("x", range(10))
def test_group_edit(app, x):
    if app.group.count() == 0:
        app.group.add(Group(name="Группа для редактирования", header="Заголовок", footer="Подвал"))
    old_groups = app.group.list()
    index = randrange(len(old_groups))
    group = Group(name=f"Отредактированная группа {index} ({x})",
                  header="Новый заголовок", footer="Новый подвал", id=old_groups[index].id)
    app.group.edit_nth(index, group)
    new_groups = app.group.list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
