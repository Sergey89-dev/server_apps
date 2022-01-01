#Преобразовать слова «разработка», «администрирование», «protocol», 
#«standard» из строкового представления в байтовое 
#и выполнить обратное преобразование (используя методы encode и decode).



def transform(args: list) -> None:
	for i in args:
		print('содержимое в виде байтов: ', i)
		print('преобразованное в строку: ',  i.decode('utf-8'))
	print('-' * 50)

word_1 = 'разработка'.encode('utf-8')
word_2 = 'администрирование'.encode('utf-8')
word_3 = 'protocol'.encode('utf-8')
word_4 = 'standard'.encode('utf-8')

word_list = [word_1, word_2, word_3, word_4]

transform(word_list)