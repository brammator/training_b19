# -*- coding: utf-8 -*-
import pytest

from model.group import Group


def test_add_group(app, auth):
    app.group.create(Group(group_name="Family users", group_header="Простое лого", group_footer="Подвал группы"))


def test_add_empty_group(app, auth):
    app.group.create(Group(group_name="", group_header="", group_footer=""))


# @pytest.mark.skip
def test_delete_first_group(app, auth):
    app.group.create(Group(group_name="Для удаления 0"))
    app.group.delete_first()


# @pytest.mark.skip
def test_delete_all_groups(app, auth):
    app.group.create(Group(group_name="Для удаления 1"))  # мб это в фикстуру вынести?
    app.group.create(Group(group_name="Для удаления 2"))
    app.group.delete_all()


def test_modify_group(app, auth):
    app.group.create(Group(group_name="Для модификации", group_header="Заголовок", group_footer="Подвал"))
    modified_group = app.group.modify_first()
