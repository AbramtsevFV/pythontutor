from collections import defaultdict

#  шаблон словаря для подсчёта
# можно использовать метод dict.get(v,..)
# ключ слово значение количество
word_count = defaultdict(int)

# делаем подсчёт

for i in range(int(input())):
    text = input()
    for word in text.split():
        word_count[word] += 1

result = [(v, k) for k, v in word_count.items()]      # превращаем словарь в список кортежей
result.sort(key=lambda x: (-x[0], x[1]))           # сортируем по первом значению по убыванию
                                                    # если первые значения ровны, то по второму по убыванию
for i in range(len(result)): print(result[i][1])

