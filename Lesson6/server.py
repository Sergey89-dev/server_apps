# Сервер

import socket
import sys
import argparse
import json
import logging
import config_server_log
from  errors import  IncorrectDataRecivedError
from variables import  ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, DEFAULT_PORT, MAX_CONNECTIONS, ERROR
from  utils import  get_message, send_message
from decos import log
SERVER_LOGGER = logging.getLogger('server')
# создание обработчика сообщения от клиентов
@log
def process_client_message(message):
    SERVER_LOGGER.debug(f'Разбор сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and \
            USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
@log
def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')

def main():
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_adress = namespace.a
    listen_port = namespace.p

    # Проверка корректности номера порта
    if not 1023 < listen_port < 65536:
        SERVER_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта'
                               f'{listen_port}. Подходящие адреса с 1024 до 65535')
        sys.exit(1)
    SERVER_LOGGER.info(f'Запускаем сервер, порт для подключений: {listen_port}. '
                       f'Адрес с которого принимаются подключения: {listen_adress}.'
                       f'Если адрес не указан, принимаются соединения с любых адресов.')
    # Подготовка сокета

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_adress, listen_port))
    # Прослушивание порта

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_adress = transport.accept()
        SERVER_LOGGER.info(f'Установлено соединение с ПК {client_adress}')
        try:
            message_from_client = get_message(client)
            SERVER_LOGGER.debug(f'Получено сообщение {message_from_client}')
            response = process_client_message(message_from_client)
            SERVER_LOGGER.info(f'Сформирован ответ клиенту {response}')
            send_message(client, response)
            SERVER_LOGGER.debug(f'Соединение с клиентом {client_adress} закрывается')
            client.close()
        except json.JSONDecodeError:
            SERVER_LOGGER.error(f'Не удалось декодировать Json строку, полученную от'
                                f'клиента {client_adress}. Соединение закрывается.')
            client.close()
        except IncorrectDataRecivedError:
            SERVER_LOGGER.error(f'От клиента {client_adress} принятые неккоректные данные.'
                                f'Соединение закрывается.')
            client.close()
if __name__ == '__main__':
    main()


