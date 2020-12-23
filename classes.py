import random

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property
    def email(self):
        return "{}.{}{}@companyR.com".format(self.first, self.last, random.randint(0, 999))

    def __repr__(self):
        return "{}, {}, {}".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
class Manager(Employee):
    def __init__(self, first, last, pay, officeId):
        super().__init__(first, last, pay)
        self.officeId = officeId

class Developer(Employee):
    def __init__(self, first, last, pay, progLang):
        super().__init__(first, last, pay)
        self.progLang = progLang

class Intern(Employee):
    def __init__(self, first, last, pay, school):
        super().__init__(first, last, pay)
        self.school = school
        
