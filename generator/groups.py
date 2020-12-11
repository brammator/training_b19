# -*- coding: utf-8 -*-
from fixture.common import random_string
from model.group import Group
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "f:n:")
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

filename = "data/groups.json"
number = 5

for o, a in opts:
    if o == "-f":
        filename = a
    elif o == "-n":
        number = int(a)

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20)) for i
    in range(number)]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", filename)
with open(data_file, "w", encoding="utf-8") as fp:
    jsonpickle.set_encoder_options("json", indent=2)
    fp.write(jsonpickle.encode(testdata))
