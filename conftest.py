# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()


@pytest.fixture(scope='function')
def auth(app):
    app.session.login(username="admin", password="secret")
    yield auth
    app.session.logout()

