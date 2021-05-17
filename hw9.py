import pathlib
import sys


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
    result = print('How can I help you?')
    return result

@input_error
def add_or_change(user_str):
    user_list = user_str.split(' ')
    name = user_list[1]
    number_phone = user_list[2]
    if name.isalpha() == False: 
        raise Exception('Enter user name')
    elif number_phone.isdigit() == False:
        raise Exception('Enter user phone number')
    else:
        name = name.capitalize()
        phone_book.update({name: number_phone})
        result = print('Ok, done')
        return result

@input_error
def show_number_phone(user_str):
    user_list = user_str.split(' ')
    name = user_list[1]
    if name.isalpha() == False:
        raise Exception('Enter user name')
    else:
        name = name.capitalize()
        result = print(phone_book.get(name))
        return result

@input_error
def show_all_book(user_str):
    if phone_book == {}:
        raise Exception('Your phonebook is empty')
    else:
        for key, value in phone_book.items():
            print(key, value)
        return

@input_error
def finish(user_str):
    result = print('Good bye!')
    return result

COMMANDS = {
    'hello': start,
    'add': add_or_change,
    'change': add_or_change,
    'phone': show_number_phone,
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
     

def main():
    while True:
        user_str = input('Enter command: ')
        user_str = user_str.lower()
        func = get_command_handler(user_str)
        if user_str.startswith('good bye') or user_str.startswith('close') or user_str.startswith('exit'):
                break
    


if __name__ == "__main__":
    phone_book = {}
    main()
