import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Ask again (special 9)'
    else:
        return 'Invalid number'

print('Ask a yes or no question:')
input('>')

print(get_answer(random.randint(1, 9)))

def par_o_impar(n):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

print(par_o_impar(8))
print(par_o_impar(3))
