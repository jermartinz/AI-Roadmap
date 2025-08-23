import random
import string


print('This is a password generator')
length = 0
user_input = input('Do you want a (b)asic, (m)edium, or (s)trong password? ').strip().lower()
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

password = randomizer_string(user_input,all_characters,length)

if password is None:
    print("Please enter a valid option: b / m / s")
else: print("Your password is: ", password)
# Ask to user if want a password (basic, medium strong)
#
#
# If basic password length(10) if medium password length 16,  
# if strong password length 24
# and return string of characters
