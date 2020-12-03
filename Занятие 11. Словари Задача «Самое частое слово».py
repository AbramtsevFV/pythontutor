from collections import Counter
import operator
# Так как сайт ПИТОНТЬЮТОР не работает с "extend" пришлось сделать альтернативное решение

# Решение 1

def func1 ():
    c = int(input())

    res = []
    # ввод данных, extend : расширяет список, добавляя элементы из итеративного связывает их между собой.
    # при использование append в этой задаче получим список списков
    # для нахождения самого часто встречаемого слова используем Counter()
    # и его метод most_common(n) n - количество элементов с максимальными значениями
    for i in range(c):
        res.extend(input().split())
    dict = Counter(res).most_common(1)

    print(dict[0][0])

# Решение 2

def func2():
    dict = {}
    result = []
    for i in range(int(input())):
        text = input().split()
        for world in text:                                      # итерируемся по словам в строке, затем создаём словарь
            dict[world] = (dict.get(world, 0) + 1)              # метод "get()" возвращает значение по ключу если нет "0" прибавляем 1,
    res = list(dict.items())                                    # получаем список вида [(a, 1), (b, 2)]
    res.sort(key=lambda i: i[1], reverse=1)                     # сортируем по второму значению
    for i in range(len(res)):                                   # создаём список часто встречаемых слов
        x = res[0][1]
        if res[i][1] == x:
            result.append(res[i][0])

    print(min(result))                                          # выводим первое в алфавитном порядке

