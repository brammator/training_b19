import pytest

from model.contact import Contact


def test_add_contact(app, auth):
    app.contact.create(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                               title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
                               mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35",
                               email="cdur@oldfiction.book", homepage="localhost/addressbook", bday="1",
                               bmonth="February", byear="1816", aday="30", amonth="October", ayear="2020",
                               address2="Msk", phone2="ditto", notes="What are you, Oleg"))


def test_add_empty_contact(app, auth):
    app.contact.create(Contact())


@pytest.mark.skip
def test_delete_first_contact(app, auth):
    app.contact.create(Contact(firstname="Жертва", lastname="Удаляемая"))
    app.contact.delete_first()


@pytest.mark.skip
def test_delete_all_contacts(app, auth):
    app.contact.create(Contact(firstname="Жертва 1", lastname="Удаляемая"))
    app.contact.create(Contact(firstname="Жертва 2", lastname="Удаляемая"))
    app.contact.delete_all()


@pytest.mark.skip
def test_modify_contact(app, auth):
    app.contact.create(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                               title="Cleanliness Director", company="Dixyorochka", address="SPb", home="+78005553535",
                               mobile="8-800-555-3535", work="8 (800) 555 3535", fax="8 800 555 35 35",
                               email="cdur@oldfiction.book", homepage="localhost/addressbook", bday="1",
                               bmonth="February", byear="1816", aday="30", amonth="October", ayear="2020",
                               address2="Msk", phone2="ditto", notes="What are you, Oleg"))
    modified_contact = app.contact.modify_first()
