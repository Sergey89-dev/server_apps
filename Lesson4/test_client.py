# Unit - тесты клиента
import os
import unittest
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from Client import create_presence, process_ans
#Тесты
class TestClass(unittest.TestCase):

 #Тест корректности запроса
    def test_def_presence(self):
        test = create_presence()
        test[TIME] = 1.1

        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
 #Корректный разбор ответа 200
    def test_200_ans(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200: ОК')

 # Корректный разбор ответа 400
    def test_400_ans(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400: Bad Request')

#Тест исключения без поля RESPONSE
    def test_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})

if __name__ == '__main__':
    unittest.main()

