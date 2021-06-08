from collections import UserDict
from datetime import datetime, timedelta
import json
import pickle
import re
​
address_book_file = 'data.bin'
pattern_birthday = r'\d\d-\d\d-\d\d\d\d'
​
class AddressBook(UserDict): 
    def add_record(self, record):
        self.data[record.name] = record
        print('A new record added for ', self.data[record.name].name)
​
    def all_records(self):
        return self.data
​
    def __iter__(self):
        self.number = 0
        return self
​
    def __next__(self):
        n = input(int('How much recordes do show? '))
        i = 0
        for key, value in self.data.items():
             if i == n:
                raise StopIteration
             else:
                return (key, value)
                i += 1
​
    def find_record(self, user_string):
        persons_list = []
        if self.name.find(user_string) != -1 or self.phone.find(user_string) != -1:
            persons_list.append(self.name)
        print(persons_list)
        return
​
    def pack(self, file_name):
        with open(file_name, "w") as fh:
            json.self.data(some_data, fh)
​
    def unpack(self, file_name):
        with open(file_name, "r") as fh:
            my_address_book = json.load(fh)
​
        
class Record:
    def __init__(self, name, phone='', birthday=None):
        self.name = name
        self.phones = []
        self.new_phone = phone
        self.birthday = birthday
​
    def add_birthday(self, birthday):
        self.birthday = birthday
​
    def add_phone(self, phone):
        self.phones.append(phone)
​
    def delete_phone(self, phone):
        self.phones.remove(phone)
​
    def redact_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == phone:
                self.phones[i] = new_phone
​
    def day_to_birthday(self, name):
        current_day = datetime.now()
        current_year = current_day.year
        for self.name in self.data:
            info_list = self.data.get(self.name)
            if self.birthday in info_list:
                date_birthday = datetime.strptime(self.birthday, "%d-%m-%y")
                if date_birthday > current_day:
                    print('Sorry, your friend is not born yet')
                current_birthday = date_birthday.replace(current_year)
                difference = abs(current_day - current_birthday)
                return difference
            else:
                raise Exception('Add user bithday')
​
​
class Field:
    def __init__(self):
        self.__value = None
​
    @property
    def value(self):
        return self.__value
​
    @value.setter
    def value(self, new_value):
        self.__value = new_value
​
​
class Name(Field):
    def __init__(self, name):
        self.name = name
​
​
class Birthday(Field):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday
​
    @property
    def value(self):
        return self._value
​
    @value.setter
    def value(self, new_value):
        if self.new_value != pattern_birthday:
            raise Exception('Only number, please, in format DD-MM-YYYY')
        else :
            self._value = new_value
    
​
class Phone(Field):
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone
​
    @property
    def value(self):
        return self._value
​
    @value.setter
    def value(self, new_value):
        if self.new_value.isdigit() == False:
            raise Exception('Only number, please')
        elif len(self.new_value) < 10:
            raise Exception('This number is too short')
        elif len(self.new_value) == 10:
            self._value = '+38' + new_value
        else:
            self._value = '+' + new_value
​

def read_dumped_data():
    with open(address_book_file, 'rb') as file:
        book = pickle.load(file)
        return book
​
def save_dumped_data(addresses):
    with open(address_book_file, 'wb') as file:
        pickle.dump(addresses, file)
​
def adding_new_record():
    new_record = input('For adding a new record type `add record <name> <phone> <birthday>`')
    new_record_to_add = new_record.split()
    _, __, name, phone = new_record_to_add
    address_book = AddressBook()
    address_book.add_record(Record(name.strip(), phone, birthday))
    save_dumped_data(address_book.all_records())
​

if __name__ == '__main__':
    try:
        records_book = read_dumped_data()
        print('Records book existes.)
        answer = input('Do show? Y/N ')
              if answer == 'Y':
                 __next__(self)
        adding_new_record()
    except EOFError:
        print('No saved addresses book found')
        adding_new_record()
        
