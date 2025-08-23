import random
import string


print('This is a password generator')
length = 0
all_characters = string.ascii_letters + string.digits + string.punctuation

def randomizer_string(user_option,characters, user_length):
    if user_option == 'b':
        user_length = 10
    elif user_option == 'm':
        user_length = 16
    elif user_option == 's':
        user_length = 24
    else:
        return None
    password = ''.join(random.choices(characters, k=user_length))
    return password

while True:
    user_input = input('Do you want a (b)asic, (m)edium, or (s)trong password? ').strip().lower()
    password = randomizer_string(user_input,all_characters,length)

    if password is not None:
        print("Your password is: ", password)
        again = input("Do you want another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
    else:
        print("Please enter a valid option: b / m / s") 
