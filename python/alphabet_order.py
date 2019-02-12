'''Пользователь вводит две буквы.
Определить, на каких местах алфавита
 они стоят и сколько между ними находится букв.'''


alp = ['', 'A', 'B', 'C', 'D',
       'E', 'F', 'G', 'H',
       'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W',
       'X', 'Y', 'Z']


ask_a = input("Enter the first upper case letter: ")
ask_b = input("Enter the second upper case letter: ")

a = alp.index(ask_a)
b = alp.index(ask_b)
c = abs(a-b)

print("Your first letter: {} is on the {} alphabet order."
      "\nYour second letter: {} is on the {} alphabet order."
      "\n There are {} letters in english alphabet.".format(ask_a, a, ask_b, b, c))
