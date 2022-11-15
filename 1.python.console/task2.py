a = input('Введите длину стороны квадрата: ')
if a.isdigit():
    print('Вывод\n', 'Периметр: ', int(a) * 4, '\n', 'Площадь: ', int(a) ** 2)
else:
    print('Надо ввести числовое значение')
    raise SystemExit(1)

b = input('Введите длину прямоугольника: ')
c = input('Введите ширину прямоугольника: ')
if b.isdigit() and c.isdigit:
    print('Вывод\n', 'Периметр: ', (int(b) + int(c)) * 2, '\n', 'Площадь: ', int(b) * int(c))
else:
    print('Надо ввести числовое значение')
    raise SystemExit(1)