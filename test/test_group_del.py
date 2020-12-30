# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group
import pytest


# @pytest.mark.skip
# @pytest.mark.parametrize("x", range(10))
def test_group_del_random(app, db, x, check_ui):
    with pytest.allure.step("Given a non-empty group list"):
        if len(db.get_group_list()) == 0:
          app.group.add(Group(name="Группа для удаления"))
        old_groups = db.get_group_list()
    with pytest.allure.step("Given a random group from the list"):
        index = randrange(len(old_groups))
        id = old_groups[index].id
    with pytest.allure.step(f"When I delete a group #{index} from the list"):
        app.group.del_byid(id)
    with pytest.allure.step("Then the new list is equal to the old list without the deleted group"):
        new_groups = db.get_group_list()
        old_groups[index:index+1] = []
        assert old_groups == new_groups
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.list(), key=Group.id_or_max)


# @pytest.mark.skip
def test_group_del_all(app, db, x, check_ui):
    with pytest.allure.step("Given a non-empty group list"):
        if len(db.get_group_list()) == 0:
            app.group.add(Group())
    with pytest.allure.step("When I delete all groups"):
        app.group.del_all()
    with pytest.allure.step("Then group list is empty"):
        new_groups = db.get_group_list()
        assert len(new_groups) == 0
        if check_ui:
            assert len(app.group.list()) == 0
