class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    # Переопределить значение атрибута line_type класса Phone.
    line_type = 'беспроводной'

    # Переопределить метод ring() класса Phone.
    def ring(self):
        print('Дзынь-дзынь!')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный')

# Распечатать значение атрибута line_type для объекта класса Phone.
print(rotary_phone.line_type)
# Вызвать метод ring() для объекта класса Phone.
rotary_phone.ring()

# Распечатать значение атрибута line_type для объекта класса MobilePhone.
print(mobile_phone.line_type)
# Вызвать метод ring() для объекта класса MobilePhone.
mobile_phone.ring()

# Вывод:
# проводной
# Дзззззыыыыыыыынь!
# беспроводной
# Дзынь-дзынь!