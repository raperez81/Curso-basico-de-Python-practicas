import random


def generate_password():
    password = []
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'a', 'b', 'c', 'd', 'e',
                  'f', 'g', 'h', 'i', '1', '2', '3', '4', '5', '6', '7', '8', '9', '#', '$', '%', '&', '@']
    for i in range(15):
        password.append(random.choice(characters))
    password = ''.join(password)    
    return password


def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()
