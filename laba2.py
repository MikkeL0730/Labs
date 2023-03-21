def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str
import re
file = open("test2.txt", "r")
k = int(input('Введите количество цифр'))
last_int_max = int(0)
print('Натуральные числа, у которых более', k, 'цифр:')
char = file.read()
file.close()
all = re.findall(r'\b\d+\b', char)
#print(all)
symbol = len(all)
symbolall = 0
for i in range(symbol):
    symbol2 = len(all[i])
    if (symbol2 > k):
        chislo = int(all[i])
        if (chislo > last_int_max):
            last_int_max = chislo
        symbolall += 1
        print(all[i])
print("Всего чисел, содержащих более",k,"цифр -", symbolall,"\n","\nМаксимальное число -", last_int_max)
#print(char)
#print('Всего чисел, содержащих более',k,'цифр -',kol_int,'\n','\nМаксимальное число -', last_int_max)
slovar = {"0": "ноль ", "1": "один ", "2": "два ", "3": "три ", "4": "четыре ", "5": "пять ", "6": "шесть ", "7": "семь ", "8": "восемь ", "9": "девять "}
print(multiple_replace(str(last_int_max), slovar))