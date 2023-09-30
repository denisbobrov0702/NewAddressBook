from collections import UserDict
from datetime import date, datetime

class Field:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

class Name(Field):
    def __init__(self, value):
        if not value.isalpha():
            raise ValueError("It is not a name")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self._value = datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Wrong format of date, write YYYY-MM-DD")
        super().__init__(self._value) 

class Record:
    def __init__(self, name,birthday=None):
        self.name = Name(name)
        self.phones = []
        if birthday:
            
            self.birthday=Birthday(birthday).value
            
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError(f"Phone {phone} not found")

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone
        else:
            raise ValueError(f"Phone {old_phone} not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError(f"Phone {phone} not found")

    def days_to_birthday(self):
        if self.birthday:
            current_date = date.today()
            user_date = self.birthday.replace(year=current_date.year)
            delta_days = user_date - current_date
            if delta_days.days >= 0:
                return delta_days.days
            else:
                user_date = self.birthday.replace(year=current_date.year + 1)
                delta_days = user_date - current_date
                return delta_days.days
        raise ValueError(f"Birthsday not found")
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def iterator(self, N):
        self.N = N
        if self.N < len(self.data):
            list_N=list(self.data.values())[:self.N]
            self.N+=N
            return list_N
        raise StopIteration
