from collections import UserDict


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.name] = record

        
class Record:

    def __init__(self, name):
        self.name = name
        self.phones = []
        self.new_phone = ''

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def redact_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == phone:
                self.phones[i] = new_phone


class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name
    

class Phone(Field):

    def __init__(self, phone):
        self.phone = phone
