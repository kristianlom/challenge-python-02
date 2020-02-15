# Resolve the problem!!
import string
from random import randint, uniform, random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
MIN = 8
MAX = 15
CARACTER = list('aA0S')


def generate_password():
    # 97 - 122 az
    # 65 - 90 AZ
    # 48 - 57 09
    # 0-27 SYMBOLS
    total_caracteres = randint(MIN, MAX)
    password_ = ""
    for i in range(total_caracteres):
        eleccion = CARACTER[randint(0, 3)]
        if eleccion == 'a':
            password_ += string.ascii_lowercase[randint(0, 25)]
        elif eleccion == 'A':
            password_ += string.ascii_uppercase[randint(0, 25)]
        elif eleccion == '0':
            password_ += string.digits[randint(0, 9)]
        elif eleccion == 'S':
            password_ += SYMBOLS[randint(0, 24)]
    print(password_)
    return password_


def validate(password):
    if 8 <= len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    if validate(generate_password()):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
