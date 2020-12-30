# -*- coding: utf-8 -*-
import random
import pytest

from model.contact import Contact
from model.group import Group


def test_contact_group_add(app, db, x):
    with pytest.allure.step("Given random group"):
        if len(db.get_group_list()) == 0:
            app.group.add(Group(name="Группа для добавления контакта"))
        group = random.choice(db.get_group_list())
    with pytest.allure.step(f"Given random contact not in group {group}"):
        if len(db.get_contacts_not_in_group(group)) == 0:
            app.contact.add(Contact(firstname="Алевтина", lastname="Григорович"))
        contact = random.choice(db.get_contacts_not_in_group(group))
    with pytest.allure.step(f"Given list of contacts in group {group}"):
        old_contacts = db.get_contacts_in_group(group)
    with pytest.allure.step(f"When I add contact {contact} in group {group}"):
        app.contact.add_to_group(contact, group)
    with pytest.allure.step(f"Then the new list of contacts in group {group} is equal to the old list with contact {contact} added"):
        new_contacts = db.get_contacts_in_group(group)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact_group_del(app, db, x):
    with pytest.allure.step("Given random group"):
        if len(db.get_group_list()) == 0:
            app.group.add(Group(name="Группа для удаления контакта"))
        group = random.choice(db.get_group_list())
    with pytest.allure.step(f"Given random contact in group {group}"):
        if len(db.get_contacts_in_group(group)) == 0:
            if len(db.get_contact_list()) == 0:
                app.contact.add(Contact(firstname="Севостьян", lastname="Робертов"))
            contact = random.choice(db.get_contacts_not_in_group(group))
            app.contact.add_to_group(contact, group)
    with pytest.allure.step(f"Given list of contacts in group {group}"):
        old_contacts = db.get_contacts_in_group(group)
    contact = random.choice(old_contacts)
    with pytest.allure.step(f"When I remove contact {contact} from group {group}"):
        app.contact.del_from_group(contact, group)
    with pytest.allure.step(f"Then the new list of contacts in group {group} is equal to the old list minus contact {contact} added"):
        new_contacts = db.get_contacts_in_group(group)
        old_contacts.remove(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
