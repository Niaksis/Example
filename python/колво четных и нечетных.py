'''Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''



print("Эта программа посчитает из вашего числа количество четных и нечетных цифр")
even = 0
odd = 0
list_even = []
list_odd = []
list_num = []
number = int(input("Введите целое число: "))

while number > 10:
    x = number % 10
    number = number // 10
    list_num.append(x)

for l in list_num:
    if l % 2 == 0:
        list_even.append(l)
        even +=1
    else:
        list_odd.append(l)
        odd += 1
print(f'В вашем числе {odd} четных и {even} нечетных цифр.\nЧетные = {list_even}.\nНечетные = {list_odd}')