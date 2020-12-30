# -*- coding: utf-8 -*-
from random import randrange

import pytest

from model.group import Group


# @pytest.mark.parametrize("x", range(10))
def test_group_edit(app, db, x, check_ui):
    with pytest.allure.step("Given a non-empty group list"):
        if len(db.get_group_list()) == 0:
            app.group.add(Group(name="Группа для редактирования", header="Заголовок", footer="Подвал"))
        old_groups = db.get_group_list()
    with pytest.allure.step("Given a random group from the list"):
        index = randrange(len(old_groups))
    with pytest.allure.step("Given a group"):
        group = Group(name=f"Отредактированная группа {index} ({x}/id={old_groups[index].id})",
                      header="Новый заголовок", footer="Новый подвал", id=old_groups[index].id)
    with pytest.allure.step("When I edit group with new properties"):
        app.group.edit_byid(group.id, group)
    with pytest.allure.step("Then the new list is equal to the old list with selected group modified"):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.list(), key=Group.id_or_max)
