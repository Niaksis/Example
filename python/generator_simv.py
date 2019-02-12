'''
Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ. Для каждого из трех
случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''
import random
import string

print("Hello, this is an russian generator!")
print("This program will help you"
      "\nto generate some number."
      "\nThey can be integer or float."
      "\nYou can generate some symbols from english alphabet too.")

print("***************************")
print("1 - to generate integer in you range 'a' to 'b'")
print("2 - to generate float in you range 'a' to 'b'")
print("3 - to generate symbol in you range 'A' to 'Z' or 'F'")
print("***************************")

ask = int(input("Enter your choice: "))

if ask == 1:
    ask_a = int(input("Enter number start range: "))
    ask_b = int(input("Enter number stop range: "))
    print("Your random number is {}!".format(random.randint(ask_a, ask_b)))

if ask == 2:
    ask_a = int(input("Enter number start range: "))
    ask_b = int(input("Enter number stop range: "))
    print("Your random number is {}!".format(random.uniform(ask_a, ask_b)))

if ask == 3:
    alp = list(string.ascii_uppercase)

    ask_a = input("Enter symbol start range: ")
    ask_b = input("Enter symbol stop range: ")

    a = alp.index(ask_a)
    b = alp.index(ask_b)
    alp_sliced = alp[a:b]
    print("Your random symbol is {}!".format(random.choice(alp_sliced)))
