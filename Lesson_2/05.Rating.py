class Rating:
    list_ratings = []
    num = ''

    def __init__(self):
        self.list_ratings = []

    def add(self, num):
        if num != '' and num.isdigit():
            self.num = num
            self.list_ratings.append(num)
            return True
        else:
            return False

    def print_rating(self):
        if len(self.list_ratings) > 0:
            self.list_ratings.sort(reverse=True)
            print('Пользователь ввел число ' + self.num + '. Результат: ' +
                  ''.join([str(self.list_ratings[num])[0:10] + ', ' for num in range(len(self.list_ratings))])[0:-2]
                  + '.')


hashset = frozenset(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print('Структора Рейтинг')
rating = Rating()
while True:
    e = input('Введите любое значение: ')
    if e is not None and e in hashset:
        rating.add(e)
        rating.print_rating()
    else:
        if e == '':
            break
