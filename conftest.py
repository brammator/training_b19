# -*- coding: utf-8 -*-
import json

from fixture.application import Application
import pytest
import os.path

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as fp:
            target = json.load(fp)
    if fixture is None:
        fixture = Application(browser=browser, base_url=target['base_url'])
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=target['base_url'])
    fixture.session.ensure_logged(username=target["admin"], password=target["secret"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logged(None)
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


@pytest.fixture
def x():
    "пустая фикстура, чтобы закомментированная параметризация не ломала ран"
    return 0
