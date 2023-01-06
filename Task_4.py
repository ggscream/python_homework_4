# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as r
k = int(input("Введите степень многочлена: "))
list_1 = [r(0, 101) for i in range(k + 1)]
string = ""
if len(list_1) <= 0:
    string = "x = 0"
else: 
    for i in range(len(list_1)): 
        if i != len(list_1) - 1 and list_1[i] != 0 and i != len(list_1) - 2: 
            string += f'{list_1[i]}x^{len(list_1)-i-1}'
            if list_1[i+1] != 0:
                string += ' + '
        elif i == len(list_1) - 2 and list_1[i] != 0: 
            string += f'{list_1[i]}x' 
            if list_1[i+1] != 0: 
                string += ' + '  
        elif i == len(list_1) - 1 and list_1[i] != 0: 
            string += f'{list_1[i]} = 0' 
        elif i == len(list_1) - 1 and list_1[i] == 0:
            string += ' = 0'
with open('file.txt', 'a') as data: 
    data.write(f'{string}\n')