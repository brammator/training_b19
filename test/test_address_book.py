# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_group(app, auth):
    app.group.create(Group(name="Family users", header="Простое лого", footer="Подвал группы"))


def test_add_empty_group(app, auth):
    app.group.create(Group(name="", header="", footer=""))


def test_delete_first_group(app, auth):
    app.group.delete_first()


def test_add_contact(app, auth):
    app.contact.create(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                               title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
                               mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35",
                               email="cdur@oldfiction.book", homepage="localhost/addressbook", bday="1",
                               bmonth="February", byear="1816", aday="30", amonth="October", ayear="2020",
                               address2="Msk", phone2="ditto", notes="What are you, Oleg"))


def test_add_empty_contact(app, auth):
    app.contact.create(Contact())

