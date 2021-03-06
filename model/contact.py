# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:
    PHONE_FIELDS = ("home", "mobile", "work", "phone2")
    EMAIL_FIELDS = ("email", "email2", "email3")
    NAME_FIELDS = ("firstname", "middlename", "lastname", "nickname")
    TEXT_FIELDS = PHONE_FIELDS + EMAIL_FIELDS + NAME_FIELDS + \
                  ("fax", "address", "address2", "company", "title", "notes", "homepage")

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None,
                 phone2=None, notes=None, id=None, emails=None, phones=None):
        self.phones = phones
        self.emails = emails
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        # return f"Contact({self.id}: {self.firstname} {self.lastname})"
        text = str({k: v for k, v in filter(lambda e: e[1] is not None, {k: getattr(self, k) for k in self.TEXT_FIELDS}.items())})
        return f"Contact({self.id}: {text})"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.as_empties() == other.as_empties()

    def id_or_max(self):
        if self.id is None:
            return maxsize
        else:
            return int(self.id)

    def as_empties(self):
        return tuple("" if getattr(self, i) is None else getattr(self, i) for i in ("firstname", "lastname"))
