# coding: utf-8

"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def show_menu():
	print('[1] перезаписать файл orders.json')
	print('[2] дополнить orders.json новыми заказами')
	print('[0] ничего не делать')


def write_order_to_json(item, quantity, price, buyer, date):
	order_data = {
		'item': item,
		'quantity': quantity,
		'price': price,
		'buyer': buyer,
		'date': date
	}
	array = []
	array.append(order_data)
	with open('json\orders.json', 'w') as json_file:
		json.dump(array, json_file, sort_keys=True, indent=4)

def add_order_to_json(item, quantity, price, buyer, date):
	order_data = {
		'item': item,
		'quantity': quantity,
		'price': price,
		'buyer': buyer,
		'date': date
	}
	with open('json\orders.json', 'ab') as json_file:
		json_file.seek(-1, 2)
		json_file.truncate()
	with open('json\orders.json', 'a+') as json_file:
		json_file.write(',\n')
		json.dump(order_data, json_file, sort_keys=True, indent=4)
		json_file.write('\n]')

def get_data_from_json(json_file):
	with open(json_file) as json_read_file:
		orders = json.load(json_read_file)
		return(orders)

def check_resulte():
	print('Проверим, что получилось в json файле:')
	print(get_data_from_json('json\orders.json'))


show_menu()
answer = input('Что сделать с файлом (1 или 2)? ')

if answer == '1':
	write_order_to_json('Milk', '5', '61.70', 'Stroev Pevel', '10.3.2019')
	# write_order_to_json('Груша', '3.2', '117.60', 'Stroev Pevel', '10.3.2019')
	check_resulte()

elif answer == '2':
	add_order_to_json('Груша', '3.2', '117.60', 'Stroev Pevel', '10.3.2019')
	add_order_to_json('Milk', '5', '61.70', 'Stroev Pevel', '10.3.2019')
	check_resulte()

print('Пока!')
