# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_edit(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="John", middlename="Vasilyevitch", lastname="Doe", nickname="Gryazny",
                                title="Cleanliness Director", company="Dixyorochka", address="SPb",
                                home="+78005553535", mobile="8-800-555-3535", work="8 (800) 555 3535",
                                fax="8 800 555 35 35", email="cdur@oldfiction.book",
                                homepage="localhost/addressbook", bday="1", bmonth="February", byear="1816",
                                aday="30", amonth="October", ayear="2020", address2="Msk", phone2="ditto",
                                notes="What are you, Oleg"))
    person = Contact(firstname="Иван", middlename="Васильевич", lastname="Первый", nickname="Синий",
                                title="Директор по чистоте", company="Диксёрочка", address="Питер",
                                home="88005553535", mobile="+7-800-555-3535", work="+7 (800) 555 3535",
                                fax="восемь 800 555 35 35", email="mlem@newchannel.meme",
                                homepage="http://localhost/addressbook", bday="21", bmonth="December", byear="1711",
                                aday="18", amonth="March", ayear="1531", address2="Мск", phone2="то же самое",
                                notes="Ох, Олег, что ты такое?")
    modified_contact = app.contact.edit_first(person)
