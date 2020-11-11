# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_add(app):
    person = Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                     title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
                     mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35",
                     email="cdur@oldfiction.book", homepage="localhost/addressbook", bday="1", bmonth="February",
                     byear="1816", aday="30", amonth="October", ayear="2020", address2="Msk", phone2="ditto",
                     notes="What are you, Oleg")
    app.contact.add(person)


def test_contact_add_empty(app):
    person = Contact()
    app.contact.add(person)
