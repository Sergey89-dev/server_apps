#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтового в строковый (предварительно определив кодировку выводимых сообщений).

import subprocess
 
 
pings = [['ping', 'yandex.ru'],['ping', 'youtube.com']]
 
for ping in pings:
 
    resource = subprocess.Popen(ping, stdout=subprocess.PIPE)
 
    i = 0
 
    for word in resource.stdout:
 
        if i<10:
            print(word)
            word = word.decode('cp866').encode('utf-8')
            print(word.decode('utf-8'))
            i += 1
        else:
            print('-' * 50)
            break