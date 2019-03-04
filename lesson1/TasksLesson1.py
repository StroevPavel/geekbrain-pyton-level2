# coding: utf-8

import subprocess
import sys

def menu(point):
	print("")
	if (point == 1): 
		print ("1.	Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.")
	elif (point == 2):
		print ("2.	Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.")
	elif (point == 3):
		print("3.	Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.")
	elif (point == 4):
		print("4.	Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).")
	elif (point == 5):
		print("5.	Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.")
	elif (point == 6):
		print("6.	Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.")
	print("")
	answer = input("Нажмите Enter чтобы продолжить... ")
	print("Решение: ")
	print("")

menu(1)
i = 1
while i < 4:
	if i == 1: t1 = "разработка"
	elif i == 2: t1 = "сокет"
	elif i == 3: t1 = "декоратор"
	i += 1
	print (t1, " = ", type(t1))
	t1byte = t1.encode('utf-8')
	print (t1byte, " = ", type(t1byte))

menu(2)
i = 1
while i < 4:
	if i == 1: t1 = b'class'
	elif i == 2: t1 = b'function'
	elif i == 3: t1 = b'method'
	i += 1
	print (t1, " = ", type(t1), "length = ", str(len(t1)))

menu(3)
i = 1
while i < 5:
	if i == 1: t1 = 'attribute'
	elif i == 2: t1 = 'класс'
	elif i == 3: t1 = 'функция'
	elif i == 4: t1 = 'type'
	i += 1
	try:
		res = t1 + " -> byte -> OK"
		t1.encode('ascii')
	except UnicodeEncodeError: 
		res = t1 + " -> byte -> Erorr!"
	print(res)


menu(4)
i = 1
while i < 5:
	if i == 1: t1 = 'разработка'
	elif i == 2: t1 = 'администрирование'
	elif i == 3: t1 = 'protocol'
	elif i == 4: t1 = 'standard'
	i += 1
	print ("Original: ", t1)
	print ("Encoded: ", t1.encode())
	print ("Encoded&Decoded: ", t1.encode().decode())
	print("")

menu(5)
i = 1
while i < 3:
	if i == 1: args = ['ping', 'youtube.com']
	if i == 2: args = ['ping', 'yandex.ru']
	subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
	for line in subproc_ping.stdout:
		line = line.decode('cp866').encode('utf-8')
		print(line.decode('utf-8'))
	i += 1

menu(6)
print("Кодировка в OS по-умолчанию: ", sys.getdefaultencoding())
my_file = open('temp.txt', 'w', encoding='utf-8')
print ("Пишем в файл...")
my_file.write("сетевое программирование\n")
my_file.write("сокет\n")
my_file.write("декоратор\n")
my_file.close()

my_file = open('temp.txt', 'r', encoding='utf-8')
print ("Читаем из файла...")
print ("")
for rd in my_file:
	print(rd)
my_file.close()