# Аннотируем параметр функции: "значение name должно быть типа str!"
def we_crash_all(name: str):
    return 'Привет, ' + name + ', мы всё сломали!'


print(we_crash_all('piss'))