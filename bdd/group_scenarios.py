# -*- coding: utf-8 -*-
from pytest_bdd import scenario
from .group_steps import *


@scenario(feature_name="groups.feature", scenario_name="Add new group")
def test_add_new_group():
    pass


@scenario(feature_name="groups.feature", scenario_name="Delete a group")
def test_del_group():
    pass

