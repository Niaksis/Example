'''Пользователь вводит номер буквы в алфавите.
 Определить, какая это буква.'''
print("Hello!. This program will help you"
      "\nto find numbers of english alphabet letters")

alp = ['', 'A', 'B', 'C', 'D',
       'E', 'F', 'G', 'H',
       'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W',
       'X', 'Y', 'Z']
number = int(input("Enter number: "))
if 0 < number < int(len(alp)):
    print(f"The letter on the {number} number is {alp[number]}!")
else:
    print("You enter out of range eng alphabet!")
