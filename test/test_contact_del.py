# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact
import pytest


# @pytest.mark.skip
# @pytest.mark.parametrize("x", range(10))
def test_contact_del_nth(app, db, x, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                                title="Cleanliness Director", company="Dixyorochka", address="SPb",
                                home="+78005553535", mobile="8-800-555-3535", work="8 (800) 555 3535",
                                fax="8 800 555 35 35", email="cdur@oldfiction.book",
                                homepage="localhost/addressbook", bday="1", bmonth="February", byear="1816",
                                aday="30", amonth="October", ayear="2020", address2="Msk", phone2="ditto",
                                notes="What are you, Oleg"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    id = old_contacts[index].id
    app.contact.del_byid(id)
    new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.list(), key=Contact.id_or_max)


# @pytest.mark.skip
def test_contact_del_all(app, db, x, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                                title="Cleanliness Director", company="Dixyorochka", address="SPb",
                                home="+78005553535", mobile="8-800-555-3535", work="8 (800) 555 3535",
                                fax="8 800 555 35 35", email="cdur@oldfiction.book",
                                homepage="localhost/addressbook", bday="1", bmonth="February", byear="1816",
                                aday="30", amonth="October", ayear="2020", address2="Msk", phone2="ditto",
                                notes="What are you, Oleg"))
    # old_contacts = app.contact.list()
    app.contact.del_all()
    new_contacts = db.get_contact_list()
    assert 0 == len(new_contacts)
    if check_ui:
        assert 0 == len(app.contact.list())
