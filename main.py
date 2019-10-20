class Contact:
    def __init__(self, name, surname, phone_number,
                 fav_contact=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.number = phone_number
        self.args = args
        self.kwargs = kwargs
        if fav_contact is False:
            self.fav_contact = 'нет'
        else:
            self.fav_contact = str(fav_contact)

    def get_add_details(self):
        if not self.args:
            return ''
        else:
            details = f'Детали: {", ".join(self.args)}\n'
            return details

    def get_add_info(self):
        if not self.kwargs:
            return '    нет'
        else:
            self.add_info = ''
            for item in self.kwargs.items():
                self.add_info += f'    {item[0]}: {item[1]}\n'
            return self.add_info

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Телефонный номер: {self.number}\n'
                f'В избранных: {self.fav_contact}\n'
                f'{self.get_add_details()}'
                f'Дополнительная информация:\n'
                f'{self.get_add_info()}'
                )


class PhoneBook:
    def __init__(self, book_name):
        self.book_name = book_name
        self.book = {}

    def enter_new_contact(self, name, surname, phone_number,
                          fav_contact=False, *args, **kwargs):
        self.book[f'{name} {surname}'] = Contact(name, surname,
                                                 phone_number,
                                                 fav_contact, *args,
                                                 **kwargs)

    def print_contacts(self):
        print('Телефонная книга', self.book_name, '\n')
        for contact in self.book:
            print(self.book[contact])
        print('\n')

    def remove_contact(self, number_request):
        self.number_request = number_request
        for contact in self.book.copy():
            if self.number_request == self.book[contact].number:
                self.book.pop(contact)

    def find_fav_contacts(self):
        for contact in self.book:
            if not self.book[contact].fav_contact or self.book[
                contact].fav_contact == 'нет':
                pass
            elif self.book[contact].fav_contact != 'нет':
                print(f'Избранные контакты {contact}: '
                      f'{self.book[contact].fav_contact}')

    def find_contact(self, name_request):
        self.name_request = name_request
        for contact in self.book:
            if self.name_request == contact:
                print(self.book[contact])

    def __str__(self):
        return str(self.print_contacts())


if __name__ == '__main__':
    print('Задача 1:\n')
    john = Contact('John', 'Smith', '+71234567809',
                   False,
                   'собака Жучка', 'смотрит сериалы',
                   telegram='@johnny', email='johnny@smith.com')
    print(john)

    print('Задача 2:\n')

    print('Выводим телефонную книгу на экран:\n')
    phone_book = PhoneBook('My Phone Book')
    phone_book.enter_new_contact('John', 'Smith', '+71234567809',
                                 False,
                                 'собака Жучка', 'смотрит сериалы',
                                 telegram='@johnny',
                                 email='johnny@smith.com')
    phone_book.enter_new_contact('Karl', 'Urban', '+79087654321')
    phone_book.print_contacts()

    print('Добавляем новый контакт, убираем старый:\n')
    phone_book.enter_new_contact('Charlie', 'Blanka', '+71234567809',
                                 fav_contact='+71234567809')
    phone_book.remove_contact('+79087654321')
    phone_book.print_contacts()

    print('Ищем контакт по имени:\n')
    phone_book.find_contact('John Smith')

    print('Ищем избранные номера по всей базе: \n')
    phone_book.find_fav_contacts()
