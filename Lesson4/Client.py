#Клиент
import socket 
import time
import json
import sys
from variables import ACTION, USER, PRESENCE, DEFAULT_PORT, RESPONSE, TIME, ACCOUNT_NAME, DEFAULT_IP_ADDRESS, ENCODING, ERROR
from utils import get_message, send_message
def create_presence(account_name = 'Guest'):
	out = {
		ACTION: PRESENCE,
		TIME: time.time(),
		USER: {
			ACCOUNT_NAME: account_name
		}
	}
	return out

def process_ans(message):
	if RESPONSE in message:
		if message[RESPONSE] == 200:
			return '200: ОК'
		return f'400: {message[ERROR]}'
	raise ValueError

def main():
	try:
		server_address = sys.argv[1]
		server_port = int(sys.argv[2])
		if server_port < 1024 or server_port > 65535:
			raise ValueError
	except IndexError:
		server_address = DEFAULT_IP_ADDRESS
		server_port = DEFAULT_PORT
	except ValueError:
		print('В качестве порта можно указать число в диапазоне от 1024 до 65535')
	# реализация обмена и сокета

	transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	transport.connect((server_address, server_port))
	message_to_server = create_presence()
	send_message(transport, message_to_server)
	try:
		answer = process_ans(get_message(transport))
		print(answer)
	except (ValueError, json.JSONDecodeError):
		print('Не удалось декодировать сообщение сервера.')

if __name__ == '__main__':
	main()

