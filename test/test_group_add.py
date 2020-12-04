# -*- coding: utf-8 -*-
import pytest

from fixture.common import random_string
from model.group import Group

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20)) for i
    in range(5)]


# @pytest.mark.parametrize("x", range(10))
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_group_add(app, x, group):
    old_groups = app.group.list()
    # group = Group(name=f"Добавленная группа {x}", header="Заголовок", footer="Подвал")
    app.group.add(group)
    new_groups = app.group.list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_group_add_empty(app):
#     old_groups = app.group.list()
#     group = Group(name="", header="", footer="")
#     app.group.add(group)
#     new_groups = app.group.list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
