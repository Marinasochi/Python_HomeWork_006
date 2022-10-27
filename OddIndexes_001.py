def input_set(mes):                          # Позволяет ввести список вещественных чисел, 
   try:                                      # произвольной длины, возвращая пользователя к вводу,
     nums = input(mes).split(' ')            # если введено не число.
     str = list(nums)
     mas = [float(x) for x in str]
     print(mas)
     return mas
   except ValueError:
     print('\033[1;31mЭто не число!\033[0m')
     return input_set(mes)

def summa_el(lst):                           # Возвращает сумму элементов списка, стоящих на
    sum = 0                                  # нечетных местах
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum     

print('\n'*3)
print('\t\tЗадача 1')
print('*'*60)
print('  Задайте список из нескольких чисел. Напишите программу, ко-\nторая найдёт сумму элементов списка, стоящих на нечётной по\nзиции.\n\t\t\033[1;35mI способ - обычная функция\033[0m')     
set = input_set('  Введите через пробел элементы списка – числа. Для оконча-\nния ввода нажмите "Enter"\n ')
sum_set = round(summa_el(set),2)
print(f'Сумма эл-ов списка на нечетных позициях: {sum_set}')   
print('\n\t\t\033[1;35mII способ - list comprehension, enummerate функция\033[0m')
res = sum([j for i, j in enumerate(set) if i&1])
print(f'Сумма эл-ов списка на нечетных позициях: {res}')
print('\n\t\t\033[1;35mIII способ - срезы\033[0m')
print(f'Сумма эл-ов списка на нечетных позициях: {sum(set[1::2])}')
print('*'*60)
print('\n'*3)