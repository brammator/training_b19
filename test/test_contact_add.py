# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact


# @pytest.mark.parametrize("x", range(10))
def test_contact_add(app, x, json_contacts):
    person = json_contacts
    old_contacts = app.contact.list()
    app.contact.add(person)
    new_contacts = app.contact.list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(person)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
