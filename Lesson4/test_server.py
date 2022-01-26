# Unit - тесты сервера

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from  Server import process_client_message

class TestServer(unittest.TestCase):
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    ok_dict = {RESPONSE: 200}
#корректный запрос
    def test_ok_check(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

#ошибка при бездействии
    def test_no_action(self):
        self.assertEqual(process_client_message({TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

#При неизвестном действии
    def test_wrong_action(self):
        self.assertEqual(process_client_message({ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

# Ошибка при отсутствии штампа времени в запросе
    def test_no_time(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)
#Ошибка при отсутствии пользователя
    def test_no_user(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guestl'}}), self.err_dict)

if __name__ == '__main__':
    unittest.main()