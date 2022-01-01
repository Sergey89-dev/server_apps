# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого файла!). Затем открыть этот файл и вывести его содержимое на печать. 
#ВАЖНО: файл должен быть открыт без ошибок вне зависимости от того, в какой кодировке он был создан!

import locale
 
strings_words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as w_m:
    for i in strings_words:
        f_n.write(i + '\n')
    w_m.seek(0)

print(w_m)

transform_file = locale.getpreferredencoding()

with open('test_file.txt', 'r', encoding= transform_file) as w_m:
    for i in w_m:
        print(i)
 
    w_m.seek(0)