def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str
file = open("test2.txt", "r")
k = int(input('Введите количество цифр'))
kol_int = 0
yes_int = 0
last_int = ''
last_int_max = int(0)
char = 'test'
print('Натуральные числа, у которых более', k, 'цифр:')
while (char != ""):
    char = file.read(1)
    if(char != " " and char != "" and char != "\n"):
        char = str(char)
        last_int = last_int + char
    else:
        if(last_int.isdigit()):
            kol = len(last_int)
            if (kol > k):
                kol_int += 1
                int_temp = int(last_int)
                if (int_temp > last_int_max):
                    last_int_max = int_temp
                print(last_int)
        last_int = ''
file.close()
print('Всего чисел, содержащих более',k,'цифр -',kol_int,'\n','\nМаксимальное число -', last_int_max)
slovar = {"0": "ноль ", "1": "один ", "2": "два ", "3": "три ", "4": "четыре ", "5": "пять ", "6": "шесть ", "7": "семь ", "8": "восемь ", "9": "девять "}
print(multiple_replace(str(last_int_max), slovar))