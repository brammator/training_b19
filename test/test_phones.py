# -*- coding: utf-8 -*-
import re
import pytest
from random import randrange

from model.contact import Contact


# @pytest.mark.skip
def test_info_on_home_page(app, x):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                                title="Cleanliness Director", company="Dixyorochka", address="SPb",
                                home="+78005553535", mobile="8-800-555-3535", work="8 (800) 555 3535",
                                fax="8 800 555 35 35", email="cdur@oldfiction.book",
                                homepage="localhost/addressbook", bday="1", bmonth="February", byear="1816",
                                aday="30", amonth="October", ayear="2020", address2="Msk", phone2="ditto",
                                notes="What are you, Oleg"))
    contactlist = app.contact.list()
    index = randrange(len(contactlist))
    contact_home = contactlist[index]
    contact_edit = app.contact.get_contact_info_from_edit_page(index)
    assert contact_home.firstname == contact_edit.firstname
    assert contact_home.lastname == contact_edit.lastname
    assert contact_home.address == contact_edit.address
    assert contact_home.phones == merge_phones_like_on_home_page(contact_edit)
    assert contact_home.emails == merge_emails_like_on_home_page(contact_edit)


# @pytest.mark.skip
def test_phones_on_contact_view_page(app, x):
    contact_view = app.contact.get_contact_info_from_view_page(0)
    contact_edit = app.contact.get_contact_info_from_edit_page(0)
    for field in Contact.PHONE_FIELDS:
        assert getattr(contact_view, field) == getattr(contact_edit, field)


def clear_phone(phone):
    # return re.sub("[^0-9+]", "", phone)
    return re.sub("[() -]", "", phone)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda p: p != "",
                            map(lambda p: clear_phone(p),
                                filter(lambda p: p is not None,
                                       map(lambda f: getattr(contact, f), Contact.PHONE_FIELDS)))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda p: p != "",
                            map(lambda p: clear_phone(p),
                                filter(lambda p: p is not None,
                                       map(lambda f: getattr(contact, f), Contact.EMAIL_FIELDS)))))

