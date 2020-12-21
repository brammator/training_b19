# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group
import pytest


# @pytest.mark.skip
# @pytest.mark.parametrize("x", range(10))
def test_group_del_random(app, db, x, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.add(Group(name="Группа для удаления"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    id = old_groups[index].id
    app.group.del_byid(id)
    new_groups = db.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.list(), key=Group.id_or_max)


# @pytest.mark.skip
def test_group_del_all(app, db, x, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.add(Group())
    app.group.del_all()
    new_groups = db.get_group_list()
    assert len(new_groups) == 0
    if check_ui:
        assert len(app.group.list()) == 0
