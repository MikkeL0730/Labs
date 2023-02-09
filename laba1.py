file = open("test.txt", "r")
k = int(input('Введи количество цифр'))
kol_int = 0
yes_int = 1
last_int = ''
last_int_max = int(0)
#print('Натуральные числа, у которых более', k, 'цифр:')
while 1:
    char = file.read(1)
    if not char:
        break
    isInt = char.isdigit()
    if (isInt == True):
        yes_int = 1
        char = str(char)
        last_int = last_int + char
    else:
        if (yes_int == 1):
            kol = len(last_int)
            if (kol > k):
                kol_int += 1
                int_temp = int(last_int)
                if (int_temp > last_int_max):
                    last_int_max = int_temp
                #print(last_int)
        last_int = ''
        yes_int = 0
file.close()
print('Всего чисел, содержащих более',k,'цифр -',kol_int)
print('\nМаксимальное число -', last_int_max)
last_temp = str(last_int_max)
chisla = ['ноль ', 'один ', 'два ', 'три ', 'четыре ', 'пять', 'шесть ', 'семь ', 'восемь ', 'девять ']
forr = 0
for number in chisla:
    forr2 = str(forr)
    last_temp = last_temp.replace(forr2, number)
    forr += 1
print(last_temp)