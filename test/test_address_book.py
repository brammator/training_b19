# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import pytest

def test_add_group(app, auth):
    app.group.create(Group(group_name="Family users", group_header="Простое лого", group_footer="Подвал группы"))


def test_add_empty_group(app, auth):
    app.group.create(Group(group_name="", group_header="", group_footer=""))


def test_delete_first_group(app, auth):
    app.group.create(Group(group_name="Для удаления 0"))
    app.group.delete_first()


def test_delete_all_groups(app, auth):
    app.group.create(Group(group_name="Для удаления 1"))
    app.group.create(Group(group_name="Для удаления 2"))
    app.group.delete_all()


def test_modify_group(app, auth):
    app.group.create(Group(group_name="Для модификации", group_header="Заголовок", group_footer="Подвал"))
    modified_group = app.group.modify_first()


def test_add_contact(app, auth):
    app.contact.create(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                               title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
                               mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35",
                               email="cdur@oldfiction.book", homepage="localhost/addressbook", bday="1",
                               bmonth="February", byear="1816", aday="30", amonth="October", ayear="2020",
                               address2="Msk", phone2="ditto", notes="What are you, Oleg"))


def test_add_empty_contact(app, auth):
    app.contact.create(Contact())

