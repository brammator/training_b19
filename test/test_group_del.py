# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group
import pytest


# @pytest.mark.skip
# @pytest.mark.parametrize("x", range(10))
def test_group_del_random(app, x):
    if app.group.count() == 0:
        app.group.add(Group(name="Группа для удаления"))
    old_groups = app.group.list()
    index = randrange(len(old_groups))
    app.group.del_nth(index)
    new_groups = app.group.list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups


# @pytest.mark.skip
def test_group_del_all(app):
    if app.group.count() == 0:
        app.group.add(Group())
    app.group.del_all()
    new_groups = app.group.list()
    assert len(new_groups) == 0
