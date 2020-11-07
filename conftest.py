# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

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
    # app.session.login(username="admin", password="secret")
    app.session.ensure_logged(username="admin", password="secret")
    yield auth
    # app.session.logout()
    # app.session.ensure_logged(None)

