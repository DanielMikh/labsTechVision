from math import pi, e, floor

# Калькулятор

x, y = input('Введите первое и второе число через пробел:').split()
# y = input('Введите второе:')

if x == 'pi':
    x = pi
elif x == 'e':
    x = e

if y == 'pi':
    y = pi
elif y == 'e':
    y = e

a = float(x)
b = float(y)

c = input('+, -, /, *, mod, pow, div, floor: ')
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    try:
        print(a / b)
    except ZeroDivisionError:
        print('ТЫ ДЕЛИФ НА НОЛЬ')
    # if b == 0:
    #     print('Деление на 0!')
    # else:
    #     print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif c == 'pow':
    print(a**b)
elif c == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a//b)
elif c == 'floor':
    print('a:',floor(a))
    print('b:', floor(b))
else: print('Нет такой операции')
