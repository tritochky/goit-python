from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.name] = record

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        i = 0
        for key, value in self.data.items():
             if i == 20:
                raise StopIteration
             else:
                return (key, value)
                i += 1

        
class Record:
    def __init__(self, name, phone=[], birthday=None):
        self.name = name
        self.phones = []
        self.new_phone = ''
        self.birthday = birthday

    def add_birthday(self, birthday):
        self.birthday.append(birthday)

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def redact_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == phone:
                self.phones[i] = new_phone

    def day_to_birthday(self, name):
        current_day = datetime.now()
        current_year = current_day.year
        if self.birthday == True: 
            current_day = self.birthday.replace(current_year)
            difference = abs(current_day - current_day)
            return difference
        else:
            raise Exception('Add user bithday')


class Field:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    def __init__(self, name):
        self.name = name


class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self.new_value.isdigit() == False:
            raise Exception('Only number, please')
        else:
            self._value = new_value
    

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self.new_value.isdigit() == False:
            raise Exception('Only number, please')
        else:
            self._value = new_value
