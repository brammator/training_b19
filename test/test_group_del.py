# -*- coding: utf-8 -*-
from model.group import Group
import pytest


# @pytest.mark.skip
def test_group_del_first(app):
    if app.group.count() == 0:
        app.group.add(Group(name="Группа для удаления"))
    old_groups = app.group.list()
    app.group.del_first()
    new_groups = app.group.list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


# @pytest.mark.skip
def test_group_del_all(app):
    if app.group.count() == 0:
        app.group.add(Group())
    app.group.del_all()
    new_groups = app.group.list()
    assert len(new_groups) == 0
