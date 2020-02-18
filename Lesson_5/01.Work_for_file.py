import os.path

try:
    if os.path.exists('test.txt') is False:
        open('test.txt', 'tw', encoding='utf-8').close()

    with open('test.txt', 'a') as f:
        while True:
            t = input('Введите данные:')
            if t != '':
                f.writelines(t + "\n")
            else:
                break
except IOError:
    print("Произошла ошибка ввода-вывода!")
