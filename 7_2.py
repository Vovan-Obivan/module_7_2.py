def custom_write(file_name, string):
    n = 0
    elem = {}
    file = open(File_name, 'a', encoding='utf-8' #открытие файла до начала цикла
    for i in info:
        #file = open(file_name, 'a', encoding='utf-8')
        tell = (file.tell())
        n += 1
        file.write(f'{i}\n')
        #file.close()
        elem.update({(n, tell):i})
    file.close() # Закрытие файла после цикла
    return  elem

info = [
    'Text for tell',
    'Используйте кодировку utf-8',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)

