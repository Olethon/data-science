from Bot_function import load_data, save_data, parse_input, add_contact, change_contact, show_phone, del_contact, add_birthday, show_birthday, birthdays 

def main():    
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            user_change = input("Save change? y/n: ")
            user_change = user_change.lower()
            if user_change == "y":
                print (save_data(book))
            print('goodbye:)')
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
           print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(book)        
        elif command == "delete":
            print(del_contact(args, book))
        elif command == "add_birthday":
             print(add_birthday(args, book))
        elif command == "show_birthday":
             print(show_birthday(args, book))
        elif command == "birthdays":
             print(birthdays(book))
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()
    

# add [ім'я] [телефон]:                                 Додати новий контакт з іменем та телефонним номером.
# change [ім'я] [існуючий телефон] [новий телефон]:     Змінити телефонний номер для вказаного контакту.
# phone [ім'я]:                                         Показати телефонний номер для вказаного контакту.
# all:                                                  Показати всі контакти в адресній книзі
# add_birthday [ім'я] [дата народження]:                Додати дату народження для вказаного контакту.
# show_birthday [ім'я]:                                 Показати дату народження для вказаного контакту.
# birthdays:                                            Показати дні народження, які відбудуться протягом наступного тижня.
# hello:                                                Отримати вітання від бота
# close або exit:                                       Закрити програму.
    
     # номери телефонів у виведенні представлені згідно методу валідації з класу Phone із AddressBook