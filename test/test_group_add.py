# -*- coding: utf-8 -*-
import pytest
from model.group import Group


# @pytest.mark.parametrize("x", range(10))
def test_group_add(app, db, json_groups, x, check_ui):
    group = json_groups
    with pytest.allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with pytest.allure.step(f"When I add the group {group} to the list"):
        app.group.add(group)
    with pytest.allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.list(), key=Group.id_or_max)
