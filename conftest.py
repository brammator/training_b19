# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app():
    fixture = Application()
    yield fixture
    fixture.session.ensure_logged(None)
    fixture.destroy()


@pytest.fixture(scope='function')
def auth(app):
    # app.session.login(username="admin", password="secret")
    app.session.ensure_logged(username="admin", password="secret")
    yield auth
    # app.session.logout()
    # app.session.ensure_logged(None)

