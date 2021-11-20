from typing import Generator


import random

def generate_password():
    capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    char = ['*', '+', '-', '/', '@', '_', '?', '!', '[','{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    characters = capital_letter + lowercase + number + char
    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)
    
    password = ''.join(password)
    return password

        

def run():
    password = generate_password()
    print('You new password is: '+ password)


if __name__=='__main__':
    run()
