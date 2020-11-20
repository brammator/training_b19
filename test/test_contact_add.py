# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_add(app):
    person = Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                     title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
                     mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35",
                     email="cdur@oldfiction.book", homepage="localhost/addressbook", bday="1", bmonth="February",
                     byear="1816", aday="30", amonth="October", ayear="2020", address2="Msk", phone2="ditto",
                     notes="What are you, Oleg")
    old_contacts = app.contact.list()
    app.contact.add(person)
    new_contacts = app.contact.list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(person)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact_add_empty(app):
    person = Contact()
    old_contacts = app.contact.list()
    app.contact.add(person)
    new_contacts = app.contact.list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(person)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
