import pickle 
from AddressBook import Record, AddressBook
# from file_manager import FileManager

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

def save_data(book, filename="addressbook.pkl"):  # Збереження контактів у файл у випадку зміни
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    return "data changed successfully"

def parse_input(user_input: str): # Парсинг введених даних
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):    # Декоратор для функцій
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "The data is not entered correctly" 
        except IndexError: 
            return "The data is not entered correctlyadd"
        except SyntaxError: 
            return "This number exists"               
    return inner

@input_error
def show_phone(args, contacts:AddressBook):
    name = args[0]
    return contacts[name] if name in contacts.keys() else "Not found"

@input_error                                           
def add_contact(args, contacts:AddressBook): # Функія додавання контактів
    name, phone = args
    name_found = contacts.find_records(name)      
    if name_found:
        name_found.add_phone(phone)
        return f'Контакт {name} оновлено'
    else:
        new_record = Record(name)
        new_record.add_phone(phone)
        contacts.add_record(new_record)
        return f'Контакт {name} додано'       
             
@input_error   
def change_contact(args: str, contacts:AddressBook): # Функія заміни контактів
    name, phone, new_phone  = args     
    rec_find = contacts.find_records(name)
    if rec_find:
        return rec_find.edit_phone(phone, new_phone)         
    else:
       return f'Контакт {name} не знайдено.'

@input_error    
def del_contact(args: str, contacts:AddressBook): # Функія видалення контактів
        name, = args
        return contacts.delete_record(name)
               
@input_error
def add_birthday(args:str, contacts:AddressBook):
    name, birthday = args    
    rec_find = contacts.find_records(name)
    if rec_find:
        rec_find.add_birthday(birthday)
        contacts.add_record(rec_find)
        return f'birthday {name} додано'
 
@input_error
def show_birthday(args:str, contacts:AddressBook):
    name = args[0]
    rec_find = contacts.find_records(name)
    if rec_find:
        return rec_find.birthday
    else: 
        return "Not found"

@input_error
def birthdays (contacts: AddressBook):
    now_birthdays = contacts.calculate_birthdays()
    return now_birthdays

if __name__ == '__main__':
    pass