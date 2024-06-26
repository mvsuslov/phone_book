def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Введите номер телефона: ')
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = input('Введите новые данные (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 5:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
            write_txt('phonebook.txt', phone_book)
        elif choice == 6:
            lastname = input('Введите фамилию для удаления: ')
            print(delete_by_lastname(phone_book, lastname))
            write_txt('phonebook.txt', phone_book)
        elif choice == 8:
            source_file = input('Введите имя исходного файла: ')
            target_file = input('Введите имя файла для копирования: ')
            line_number = int(input('Введите номер строки для копирования: '))
            line = read_line(source_file, line_number)
            if line:
                append_line(target_file, line)
                print(f"Строка {line_number} успешно скопирована из {source_file} в {target_file}")

        choice = show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные абонента\n"
          "6. Удалить абонента\n"
          "7. Закончить работу\n"
          "8. Копировать данные из одного файла в другой")
    choice = int(input("Введите номер действия: "))
    return choice


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')


def print_result(phone_book):
    for record in phone_book:
        print(', '.join(record.values()))


def find_by_lastname(phone_book, last_name):
    results = [record for record in phone_book if record['Фамилия'] == last_name]
    return results if results else "Абонент не найден."


def find_by_number(phone_book, number):
    results = [record for record in phone_book if record['Телефон'] == number]
    return results if results else "Абонент не найден."


def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return f"Номер для {last_name} изменен."
    return "Абонент не найден."


def delete_by_lastname(phone_book, last_name):
    for i, record in enumerate(phone_book):
        if record['Фамилия'] == last_name:
            del phone_book[i]
            return f"Абонент {last_name} удален."
    return "Абонент не найден."


def read_line(filename, line_number):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if 0 < line_number <= len(lines):
            return lines[line_number - 1]
        else:
            print(f"Line number {line_number} is out of range.")
            return None


def append_line(filename, line):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(line)


if __name__ == "__main__":
    work_with_phonebook()
