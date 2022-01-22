#2. Каждое из слов «class», «function», «method» записать в байтовом типе. 
#Сделать это необходимо в автоматическом, а не ручном режиме с помощью добавления литеры b к текстовому значению, 
#(т.е. ни в коем случае не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

def enc_dec(args:list) -> None:
	for i in args:
		print('тип переменной: ',type(i))
		print('содержимое: ', i)
		print('длина: ', len(i))
	print('-' * 50)

word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

word_list = [word_1, word_2, word_3]
enc_dec(word_list)