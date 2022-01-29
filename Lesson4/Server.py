#Программа сервер
import socket, time, sys
from variables import ACTION, USER, PRESENCE, DEFAULT_PORT, TIME, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS,  ERROR, RESPONSEDEFAULT_IP_ADDRESSSE
from utils import get_message
from utils import send_message
from variables import MAX_PACKAGE_LENGTH
import json

def process_client_message(message):
	if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
			and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
		return {RESPONSE: 200}
	return {
		RESPONSEDEFAULT_IP_ADDRESSSE: 400,
		ERROR: 'Bad Request'
	}

def main():
	try:
		if '-p' in sys.argv:
			listen_port = int(sys.argv[sys.argv.index('-p') + 1])
		else:
			listen_port = DEFAULT_PORT
		if listen_port < 1024 or listen_port > 65535:
			raise ValueError
	except IndexError:
		print('После параметра - \'p\' должен быть указан номер порта.')
		sys.exit(1)
	except ValueError:
		print(
			'В качестве порта можно указать число в диапазоне от 1024 до 65535'
			)
		sys.exit(1)

	# Адрес прослушивания

	try:
		if '-a' in sys.argv:
			listen_address = sys.argv[sys.argv.index('-a') + 1]
		else:
			listen_address = ''

	except IndexError:
		print(
			'После параметра \'-a\' необходимо указать адрес для прослушивания '
			)
		sys.exit(1)

	# Сокет

	transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	transport.bind((listen_address, listen_port))

	# Прослушивание порта

	transport.listen(MAX_CONNECTIONS)

	while True:
		client, client_address = transport.accept()
		try:
			message_from_client = get_message(client)
			print(message_from_client)
			response = process_client_message(message_from_client)
			send_message(client, response)
			client.close()
		except (ValueError, json.JSONDecodeError):
			print('Принято неккоректное сообщение от клиента.')
			client.close()

if __name__ == '__main__':
	main()