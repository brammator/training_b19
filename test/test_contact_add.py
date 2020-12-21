# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact


# @pytest.mark.parametrize("x", range(10))
def test_contact_add(app, db, x, json_contacts_valid, check_ui):
    person = json_contacts_valid
    old_contacts = db.get_contact_list()
    app.contact.add(person)
    new_contacts = db.get_contact_list()
    old_contacts.append(person)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.list(), key=Contact.id_or_max)
