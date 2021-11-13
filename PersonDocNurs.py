from enum import Enum

class Illnesses(Enum):#Illness enum
    Clear = "Clear",
    Illness1 = "Illness1",
    Illness2 = "Illness2",

class Person():
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    def __str__(self):
        return str.format("{fname} {lname}", fname = self.firstName, lname = self.lastName)
    def setAge(self, age):
        self.age = age

class Doctor(Person):
    def __init__(self, fName, lName, age):
        super().__init__(fName, lName, age)
        self.currentPatient = None
    def getPatient(self):
        return self.currentPatient
    def setPatient(self, newPatient):
        self.currentPatient = newPatient
    def __str__(self):
        return str.format("Doc: {fn} {ln}", fn = self.firstName, ln = self.lastName)

class Nurse(Person):
    def __init__(self, fName, lName, age):
        super().__init__(fName, lName, age)
    def __str__(self):
        return str.format("Nur: {fn} {ln}", fn = self.firstName, ln = self.lastName)

class Patient(Person):
    def __init__(self, fName, lName, age, illness):
        super().__init__(fName, lName, age)
        self.illness = illness
    def getIllness(self):
        return self.illness
    def setIllness(self, illness):
        self.illness = illness

doc = Doctor("jeff","brr", 50)
nurs = Nurse("name", "name2", 30)
pat = Patient("ded","dying", 30, Illnesses.Illness1)

print(doc)
print(doc.currentPatient)
doc.setPatient(pat)
print(doc.currentPatient)
print(pat.getIllness())
    
    