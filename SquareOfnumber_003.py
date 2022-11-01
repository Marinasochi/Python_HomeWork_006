def is_that_number(mes):               # Позволяет ввести с консоли целое число, возвращая
  print(mes, end=' ')                  # пользователя ко вводу каждый раз, если ввод не корректен
  val = input()
  try:
    if float(val) % 1 != 0:
        raise Exception("\033[1;31mЧисло должно быть целым!\033[0m")
    return int(val)
  except ValueError:
    print('\033[1;31mЭто не число!\033[0m')
    return is_that_number(mes)
  except Exception as e:
    print(e)
    return is_that_number(mes)
  
print('\n'*3)
print('\t\tЗадача 3')
print('*'*60)
print('  Напишите программу, которая принимает на вход два числа и \nпроверяет, является ли одно число квадратом другого.\n')
numb_1 = is_that_number('  Введите число_1 = ')
numb_2 = is_that_number('  Введите число_2 = ')
print('\n\t\t\033[1;35mI способ\033[0m')
if numb_1 * numb_1 == numb_2: print(f'число {numb_2} является квадратом числа {numb_1} ') 
else: print(f'число {numb_2} НЕ является квадратом числа {numb_1}')
print('\n\t\t\033[1;35mII способ\033[0m')
a = lambda i, j: f'число {j} является квадратом числа {i}' if i * i == j else f'число {j} НЕ является квадратом числа {i}'
print(a(numb_1, numb_2))
print('*'*60)
print('\n'*3)