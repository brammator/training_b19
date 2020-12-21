# -*- coding: utf-8 -*-
import pytest
from model.group import Group


# @pytest.mark.parametrize("x", range(10))
def test_group_add(app, db, json_groups_valid, x, check_ui):
    group = json_groups_valid
    old_groups = db.get_group_list()
    app.group.add(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.list(), key=Group.id_or_max)
