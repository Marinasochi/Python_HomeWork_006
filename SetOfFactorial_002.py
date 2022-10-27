def is_that_number(mes):               # Позволяет ввести с консоли целое нат-ое  число, возвращая
  print(mes, end=' ')                  # пользователя ко вводу каждый раз, если ввод не корректен
  val = input()
  try:
    if int(val) < 1:
        raise Exception("\033[1;31mЧисло должно быть натуральным!\033[0m")
    return int(val)
  except ValueError:
    print('\033[1;31mЭто не число!\033[0m')
    return is_that_number(mes)
  except Exception as e:
    print(e)
    return is_that_number(mes)

def set_factor(number):                # Возвращает список чисел размером N, состоящий из фак-
  mass = range(1, number + 1)          # ториалов следующих друг за другом от 1 до N.
  new_mass = []
  m = 1
  for i in mass:
    m *= i
    i = m   
    new_mass.append(i)
  return new_mass  

def factorial_M(number):               # Возвращет факториал принимаемого нат-го числа.
  if number ==1: 
    return number
  else:
    return number*factorial_M(number-1)
    
print('\n'*3)
print('\t\tЗадача 2')
print('*'*60)
print('  Напишите программу, которая принимает на вход число N и вы-\nдает набор произведений чисел от 1 до N.\n')
N = is_that_number('  Введите число N = ')
print('\t\tI способ – обычная функция\n') 
print(set_factor(N))
print('\t\tII способ – рекурсия и функция map\n')
factorial_M(N)
print(list(map(factorial_M, range(1, N + 1))))
print('\t\tIII способ – рекурсия, функции map и lambda\n')
fact = lambda i: i * fact(i-1) if i > 1 else 1
print(list(map(fact, range(1, N + 1))))
print('*'*60)
print('\n'*3)