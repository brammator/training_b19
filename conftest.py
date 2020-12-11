# -*- coding: utf-8 -*-
import importlib
import json
import os.path

import jsonpickle
import pytest

from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file, "r", encoding="utf-8") as fp:
            target = json.load(fp)
    if fixture is None:
        fixture = Application(browser=browser, base_url=target['base_url'])
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=target['base_url'])
    fixture.session.ensure_logged(username=target["username"], password=target["password"])
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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_form_module(module):
    return importlib.import_module(f"data.{module}").testdata


def load_from_json(filename):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{filename}.json"), "r",
              encoding="utf-8") as fp:
        return jsonpickle.decode(fp.read())


@pytest.fixture
def x():
    """пустая фикстура, чтобы закомментированная параметризация не ломала ран"""
    return 0
