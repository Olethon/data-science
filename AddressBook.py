from collections import UserDict
import re
from datetime import datetime as dtdt
from datetime import timedelta as dttd


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'
    
    def setValue(self, value:str):
        self.value = value
 
class Name(Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Phone(Field):
    def __init__(self, value = None):
        super().__init__(value)   

    def normalize_phone (self, value):                                    # виведення введеного номеру у форматі (+38)+"10 цифр"
        number_template=r"[\d\+]+"
        phone_number=''.join(re.findall(number_template, value))
        if len(phone_number) == 10:
            phone = '+38' + phone_number
            return phone
        elif len(phone_number) == 11 and phone_number.startswith('8'):
            phone = '+3' + phone_number
            return phone
        elif len(phone_number) == 12 and phone_number.startswith('38'):
            phone = '+' + phone_number 
            return phone      
        elif len(phone_number) == 13 and phone_number.startswith('+38'):
            phone = phone_number
            return phone
        else:
            raise ValueError
        
class Birthday(Field):
    def __init__(self, value):        
        try:
            self.value = dtdt.strptime(value, '%d-%m-%Y').date()
        except ValueError:
            self.value = None
            raise ValueError("Invalid date format. Use DD-MM-YYYY")
        
class Record:
    def __init__(self, name):
        self.name = Name(name)       
        self.phones = []
        self.phone = Phone()
        self.birthday = None   

    def __repr__(self):
        if self.birthday:
            return f"Contact name: {self.name.value}, birthday: {self.birthday}, phones: {'; '.join(p for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

    def add_phone(self, number):
        number = self.phone.normalize_phone(number)
        if number in self.phones:    
            raise SyntaxError
        else:
            self.phones.append(self.phone.normalize_phone(number))         # додаєм номер в список використовуючи метод валідації з класу Phone               
    
    def remove_phone(self, phone:Phone):
        phone = self.phone.normalize_phone(phone)                          # валідуєм вхідний номер
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print ("phone not found")
            raise ValueError         
    
    def edit_phone(self, phone:str, change_phone:str):
        phone = self.phone.normalize_phone(phone)                         
        change_phone = self.phone.normalize_phone(change_phone)             
        if phone in self.phones:
            index_to_replace = self.phones.index(phone)                     # знаходимо індекс елемента списку
            self.phones[index_to_replace] = change_phone
            return 'the contact has been changed'                   # змінюємо номер у списку за індексом          
        else:
            return "phone not found"
          
    
    def find_phone(self, phone: Phone):
        phone = self.phone.normalize_phone(phone)
        return (phone if phone in self.phones else f" {phone} not found") 

    def add_birthday(self, birthday):
        if Birthday(birthday):
            self.birthday = birthday
            return (f'Для контакту {self.name} оновлено дату дня народження на {birthday}')
            


class AddressBook(UserDict):
    

    def add_record(self, record: Record):
           self.data[record.name.value] = record

    def find_records(self, user_name:str):
        for name, phone in self.data.items():
            if name == user_name:
                return phone
    
    def delete_record(self, name: str):
        if name in self.data:
            del self.data[name]
            return(f"The contact {name} has been deleted")
        else:
            return(f"Contact {name} not found in the address book.")       
        
    def calculate_birthdays(self):
        today = dtdt.today().date()
        self.birthdays = []
        for user in self.data.items():
            birthday = user[1].birthday
            birthday_parsing =dtdt.strptime(birthday, "%d-%m-%Y").date()
            now_birthday_parsing = birthday_parsing.replace(year=today.year)
            if now_birthday_parsing.toordinal() - today.toordinal() > 7 or now_birthday_parsing.toordinal() - today.toordinal() <= 0:
                pass
            else:
                if now_birthday_parsing.weekday() == 6:
                    sunday_day = birthday_parsing + dttd(days=1)  
                    self.birthdays.append({'name':user[1].name, "birthday":dtdt.strftime(sunday_day, "%d.%m.%Y")})                
                elif now_birthday_parsing.weekday() == 5:
                    saturday_day = birthday_parsing + dttd(days=2)  
                    self.birthdays.append({'name':user[1].name, "birthday":dtdt.strftime(saturday_day, "%d.%m.%Y")})  
                else: 
                    self.birthdays.append({'name':user[1].name, "birthday":birthday})    
        return self.birthdays

if __name__ == '__main__':
   pass