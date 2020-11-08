# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact
from model.group import Group

fixture = None


@pytest.fixture(scope="function")
def app():
    global fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application()
    yield fixture


@pytest.fixture(scope="session", autouse=True)
def destroy():
    global fixture
    yield
    fixture.session.ensure_logged(None)
    fixture.destroy()


@pytest.fixture(scope="function")
def auth(app):
    app.session.ensure_logged(username="admin", password="secret")
    yield auth


@pytest.fixture()
def prep_group(request, app, auth):
    # TODO: брать количество групп из request.param
    desired = 1
    present = app.group.count()
    for i in range(present + 1, desired + 1):
        app.group.create(Group(group_name=f"Группа №{i} создана в предусловиях",
                               group_header=f"Заголовок группы №{i}",
                               group_footer=f"Подвал группы №{i}"))
    yield


@pytest.fixture()
def prep_contact(request, app, auth):
    # TODO: брать количество контактов из request.param
    desired = 1
    present = app.contact.count()
    for i in range(present + 1, desired + 1):
        app.contact.create(Contact(**{c: f"{c.capitalize()}_{i}" for c in (
            'firstname', 'middlename', 'lastname', 'nickname', 'title', 'company', 'address', 'home', 'mobile', 'work',
            'fax', 'email', 'email2', 'email3', 'homepage', 'address2', 'phone2', 'notes',
            # , 'bday', 'bmonth', 'byear', 'aday', 'amonth', 'ayear'
        )}))
    yield
