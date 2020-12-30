# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact


# @pytest.mark.parametrize("x", range(10))
def test_contact_add(app, db, x, json_contacts, check_ui):
    person = json_contacts
    with pytest.allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with pytest.allure.step(f"When I add the contact {person} to the list"):
        app.contact.add(person)
    with pytest.allure.step("Then the new contact list is equal to the old list with the added contact"):
        new_contacts = db.get_contact_list()
        old_contacts.append(person)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.list(), key=Contact.id_or_max)
