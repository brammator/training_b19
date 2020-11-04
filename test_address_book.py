# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from group import Group
from application import Application

@pytest.fixture(scope="module")
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Family users", header="Простое лого", footer="Подвал группы"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
             title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
             mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35", email="cdur@oldfiction.book",
             homepage="localhost/addressbook", bday="1", bmonth="February", byear="1816", aday="30",
             amonth="October", ayear="2020", address2="Msk", phone2="ditto", notes="What are you, Oleg"))
    app.return_to_main_page()
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact())
    app.return_to_main_page()
    app.logout()

