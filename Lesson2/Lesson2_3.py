#Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
#Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
#Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
#Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml


def yaml_file():
    rand_data = {
        1: ['a', 5, 0, 9],
        2: 135421,
        3: {1:'.\u00A5', 2:'\u00AE', 3:'\u00B5'}
    }

    with open('yaml_lesson.yaml', 'w', encoding='utf-8') as test_file:
        yaml.dump(rand_data, test_file, default_flow_style=False, allow_unicode=True)


def yaml_read():
    try:
        with open('yaml_lesson.yaml', 'r', encoding='utf-8') as file_read:
            testing = yaml.safe_load(file_read)
            return testing
    except FileNotFoundError:
        print('Ошибка')


yaml_file()
print(yaml_read())