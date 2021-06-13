from collections import UserDict
from datetime import datetime, timedelta
import re


#Создаю классы

class AddressBook(UserDict): 
    def add_record(self, record):
        self.data[record.name.value] = record

        # итератор для пагинации

    def iterator(self, n):
        if len(self.data) < n:
            raise IndexError()
        else:
            data_list = list(self.data.items())
            while data_list:
                result = '\n'.join(
                    [f'\n\tContact <{el[0]}> has following data:\
                        \n\tbirthday info - {list(el[1].items())[0][1]}\
                        \n\tphon/s - {"; ".join(list(el[1].items())[1][1])}' for el in data_list[:n]])
                yield result
                data_list = data_list[n:]

    def find_record(self, user_string): 
        persons_list = [] 
        if self.name.find(user_string) != -1 or self.phone.find(user_string) != -1:
            persons_list.append(self.name)
        print(persons_list)
        return

        
class Record:
    def __init__(self, name, phone='', birthday=None):
        self.name = name
        self.phones = [phone]
        self.birthday = birthday

    def add_birthday(self, birthday):
        self.birthday = birthday

    def add_phone(self, phone):
        self.phones.append(phone)

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def redact_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == phone:
                self.phones[i] = new_phone

    def day_to_birthday(self):
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
                

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value
        
        
class Name(Field):
    def __init__(self, value):
        self.value = value


class Birthday(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        pattern_birthday = '\d{2}-\d{2}-\d{4}'
        if new_value != pattern_birthday:
            raise Exception('Only number, please, in format DD-MM-YYYY')
        else :
            self.__value = new_value 
    

class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value.isdigit() == False:
            raise Exception('Only number, please')
        elif len(new_value) < 10:
            raise Exception('This number is too short')
        elif len(new_value) == 10:
            self.__value = '+38' + new_value
        else:
            self.__value = '+' + new_value
