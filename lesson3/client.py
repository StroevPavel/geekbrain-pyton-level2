# coding: utf-8

"""
Функции клиента: сформировать presence-сообщение; отправить сообщение серверу; 
получить ответ сервера; разобрать сообщение сервера; 
параметры командной строки скрипта client.py <addr> [<port>]: 
addr — ip-адрес сервера; port — tcp-порт на сервере, по умолчанию 7777
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

action = input('Enter any request (type get_time): ')

request_string = json.dumps(
	{
	'action': action
	}
)

sock.send(request_string.encode())

while True:
	responce = sock.recv(1024)
	if responce:
		print(responce.decode('utf-8'))
		sock.close()
		break