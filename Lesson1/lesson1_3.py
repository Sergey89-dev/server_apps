#. Определить, какие из слов, поданных на вход программы, 
#невозможно записать в байтовом типе.
# Для проверки правильности работы кода используйте значения: «attribute», «класс», «функция», «type»

def value_out(args: list) -> None:
	for i in args:
		print(i)

word_1 = b'attribute'
word_2 = b'класс'
word_3 = b'функция'
word_4 = b'type'

word_list = [word_1, word_2, word_3, word_4]

value_out(word_list)

#итог bytes can only contain ASCII literal characters.(не поддерживает кириллицу)