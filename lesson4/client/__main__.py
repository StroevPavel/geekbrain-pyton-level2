# coding: utf-8

"""
Для всех функций из урока 3 написать тесты с использованием unittest. 
Они должны быть оформлены в отдельных скриптах с префиксом test_ в имени файла 
(например, test_client.py).
"""

import socket
import json
import sys
import argparse

def createParser(): # парсер для командной строки
	parser = argparse.ArgumentParser()
	parser.add_argument ('-a', default='localhost')
	parser.add_argument ('-p', default='7777')
	return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

sock = socket.socket()
sock.connect((namespace.a, int(namespace.p)))

print("Connected to Server on IP={} and port={}".format(namespace.a, namespace.p))

client_id = 'my_client_1'

action = input('Enter any request (type get_time): ')
data = input('Enter data (if requared): ')

request_string = json.dumps(
	{
	'action': action,
	'data': data,
	'client': client_id
	}
)

sock.send(request_string.encode())

while True:
	responce = sock.recv(1024)
	if responce:
		print(responce.decode('utf-8'))
		sock.close()
	break