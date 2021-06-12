from classes import *
import pathlib
import pickle
import re
import sys
​

address_book_file = 'data.bin'
pattern_birthday = r'\d\d-\d\d-\d\d\d\d'

​
 #Дальше основной код
    
def input_error(func):
    def inner(user_str):  
        try:
            result = func(user_str)
        except Exception as e:
            print("Error:", e)
        else:
            return result
    return inner

@input_error
def start(greeting):
    text = '''Hello! You can use next commands (without quotes) for dialog with me:
    'add'- adding name, phone or birthday,
    'change' - changing number pnone of specific user,
    'phone' - for looking number pnone of specific user,
    'find' - show all overlaps, 
    'birthday' - show days to birthday of specific user,
    'show all' - show all address-book,
    'good bye', 'close' or 'exit' - finish working.
    How can I help you?'''
    result = print(text')
    return result

@input_error
def adding_new_record():
    new_record = input('For adding a new record type `add record <name> <phone> <birthday>`')
    new_record_to_add = new_record.split()
    _, __, name, phone = new_record_to_add
    address_book = AddressBook()
    address_book.add_record(Record(name.strip(), phone, birthday))
    save_dumped_data(address_book.all_records())

@input_error
def change(user_str):
    user_list = user_str.split(' ')
    name = user_list[1]
    number_phone = user_list[2]
    if number_phone in address_book:
        answer = input('Just add or replace? A/R ')
        if answer == 'R':
            address_book[name].redact_phone(number_phone)
        else:
            address_book[name].add_phone(number_phone) 
        result = print('Ok, done')
        return result
        
@input_error
def show_number_phone(name):
    if name.isalpha() == False:
        raise Exception('Enter user name')
    else:
        name = name.capitalize()
        result = print(address_book.get(name))
        answer = input('Do you want delete it? Y/N ')
        if answer == 'Y':
            phones.remove(result)
        return result

#ф-ция возвращает запись, если есть совпадения в цифрах или буквах                   
                   
@input_error
def find_overlaps(data):
    result = addressbook.find_record(data)
    return result

#ф-ция определяет, ск. дней ост. до д.р.                   
                   
@input_error
def to_birthday(name):
    if name.isalpha() == False:
        raise Exception('Enter user name')
    else:
        name = name.capitalize()
        result = print(address_book.day_to_birthday(name))
        return result
        
@input_error
def show_all_book(user_str):
    if address_book == {}:
        raise Exception('Your phonebook is empty')
    else:
        result = address_book.__next__(data)
        return result

@input_error
def finish(user_str):
    result = print('Good bye!')
    return result

COMMANDS = {
    'hello': start,
    'add': adding_new_record,
    'change': change,
    'phone': show_number_phone,
    'birthday': to_birthday,
    'find': find_overlaps
    'show all': show_all_book,
    'good bye': finish,
    'close': finish,
    'exit': finish
    }

@input_error
def get_command_handler(user_str):
    for command in COMMANDS:
        if user_str.startswith(command):
            return COMMANDS[command](user_str)
    raise Exception('Give me a correct command please')
     


def read_dumped_data():
    with open(address_book_file, 'rb') as file:
        book = pickle.load(file)
        return book
​
def save_dumped_data(addresses):
    with open(address_book_file, 'wb') as file:
        pickle.dump(addresses, file)
​

if __name__ == '__main__':
    try:
        records_book = read_dumped_data()
        print('Records book existes.')
        while True:
        user_str = input('Enter command: ')
        user_str = user_str.lower()
        func = get_command_handler(user_str)
        if user_str.startswith('good bye') or user_str.startswith('close') or user_str.startswith('exit'):
                break
    except EOFError:
        print('No saved addresses book found')
        adding_new_record()
        