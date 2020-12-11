# -*- coding: utf-8 -*-
import pytest
from model.group import Group


# @pytest.mark.parametrize("x", range(10))
def test_group_add(app, json_groups, x):
    group = json_groups
    old_groups = app.group.list()
    app.group.add(group)
    new_groups = app.group.list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

