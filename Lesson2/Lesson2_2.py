#Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
#Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). В это словаре параметров обязательно должны присутствовать юникод-символы, отсутствующие в кодировке ASCII.
#Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
#Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
#Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.

import json

def write_order_to_json(**kwargs):
	with open('orders.json') as jn_file:
		words = json.load(jn_file)
		words['orders'].append(kwargs)
		with open('orders.json', 'w') as end_file:
			json.dump(words, end_file, indent = 4 )

order = {'item': 'Pen', 'quantity': 2, 'price': 25, 'buyer': 'username', 'date': '23.06.2020'}

write_order_to_json(**order)

#проверим файл
with open('orders.json') as u_f:
	uf_reader = u_f.read()
	objs = json.loads(uf_reader)
	print(objs)