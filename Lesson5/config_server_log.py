# Серверный лог
import sys
import os
import logging
import logging.handlers
sys.path.append(os.path.join(os.getcwd(), '..'))
from variables import LOGGING_LEVEL

# Создание формировщика
SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

# Имя файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# Создание потоков вывода логов

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='S')
LOG_FILE.setFormatter(SERVER_FORMATTER)

# Создание регистратора и настройка
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообшение')
