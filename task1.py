# Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# все строки, начинающиеся на букву «А», расположенные между строками с
# номерами N1 и N2. Определить количество слов в первой строке файла F2.
count = 0

with open('F1.txt', 'w') as F1:
    while True:
        data = input("Введите строку (Нажмите ENTER при пустой строке для завершения ввода): ")
        if not data:
            break
        try:
            F1.write(data + '\n')
            count +=1
        except IOError: print('!ОШИБКА!\n Запись в файл не была выполнена')

while True:
    try:
        N1 = int(input("Введите номер строки N1: "))
        N2 = int(input("Введите номер строки N2: "))
    except ValueError:
        print('!ОШИБКА!\n Введено не целое число')
    else:
        if N2 <= 0 or N1 <= 0:
            print("!ОШИБКА!\n Введено неположительное значение")
        else:
            if N2 < N1:
                print("!ОШИБКА!\n Значение N2 должно быть больше значения N1")
            else: break
if N2 > count:
    N2 = count
    print(f'Введенное значение N2 превышает количество строк, вписанных в файл; значение было изменено на {count}')

with open(r'F1.txt', 'r') as F1, open(r'F2.txt', 'w') as F2:
    try:
        lines = F1.readlines()
        for i in range(N1 - 1, N2):
            line = lines[i]
            if line[0].lower().startswith('а'):
                F2.write(line)
    except IOError: print('!ОШИБКА!\n Запись в файл не была выполнена')

with open(r'F2.txt', 'r') as F2:
    try:
        firstLine = F2.readline()
        wordCount = len(firstLine.split())
        print(f"Количество слов в первой строке файла F2: {wordCount}")
    except IOError: print('!ОШИБКА!\n Запись в файл не была выполнена')
