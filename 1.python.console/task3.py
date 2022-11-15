salary = input('Введите заработную плату в месяц: ')
credit = input('Введите, какой процент(%) уходит на ипотеку: ')
bills = input('Введите, какой процент(%) уходит на жизнь: ')
if salary.isdigit() and credit.isdigit() and bills.isdigit():
    print('Вывод\n', 'На ипотеку было потрачено: ', int(salary) * 12 * int(credit) / 100, '\n', 'Было накоплено: ', int(salary) * 12 * (100 - int(credit) + int(bills)) / 100)
else:
    print('Надо ввести числовое значение')
    raise SystemExit(1)
