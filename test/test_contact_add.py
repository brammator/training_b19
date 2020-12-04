# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.common import random_string

testdata = [Contact()] + [Contact(**{k: random_string(f"{k}_{i} ", 20) for k in Contact.TEXT_FIELDS}) for i in range(5)]
# bad = dict(
           # home='home_0 # sH*$kFFa_',
           # mobile='mobile_0 G)~O?iA 0 # ',
           # work='work_0 -l',
           # phone2='phone2_0 4a@:/+u-d!',
           # email='email_0 0&ULR KFqm$duW56? ',
           # email2='email2_0 YoY',
           # email3='email3_0 ',
           # firstname='firstname_0 =8T  N&6[(.',  # здесь ошибка - два пробела
           # middlename='middlename_0 \\\\~',
           # lastname='lastname_0 EFB1N <j)A&',  # здесь ошибка "<"
           # nickname='nickname_0 D "i   : x',
           # fax='fax_0 y+ G`2&Wz9f=dLKc,p',
           # address='address_0 w7 KD"$ fB6$4 w',
           # address2='address2_0 8h',
           # company='company_0 Qu<2 z  =Zh_',
           # title='title_0 A ncOO',
           # notes='notes_0 397&o<Y@| 1I.',
           # homepage="homepage_0  'o EHPUs&#@",  # здесь ошибка - апостроф
           # )
# testdata = [Contact(**{k: v}) for k, v in bad.items()]

# @pytest.mark.parametrize("x", range(10))
@pytest.mark.parametrize("person", testdata, ids=[repr(x) for x in testdata])
def test_contact_add(app, x, person):
    # person = Contact(firstname=f"John {x}", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
    #                  title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
    #                  mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35",
    #                  email="cdur@oldfiction.book", homepage="localhost/addressbook", bday="1", bmonth="February",
    #                  byear="1816", aday="30", amonth="October", ayear="2020", address2="Msk", phone2="ditto",
    #                  notes="What are you, Oleg")
    old_contacts = app.contact.list()
    app.contact.add(person)
    new_contacts = app.contact.list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(person)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@pytest.mark.skip
def test_contact_add_empty(app):
    person = Contact()
    old_contacts = app.contact.list()
    app.contact.add(person)
    new_contacts = app.contact.list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(person)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
