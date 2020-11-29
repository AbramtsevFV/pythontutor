import collections as c
# Инициализируем конструктор словаря defaultdict, при обращение к словарю с отсутствующим ключом.
# Вызывается функция в данном случаи "int" , которая возвращает  "0"
dict = c.defaultdict(int)
result = []

line = input().split()

for word in line:
    result.append(dict[word])           # согласно задания первое вхождение слова имеет 0, добовляем в список
    dict[word] += 1                     # находим по ключу и прибовляем 1

print(*result)                          

# проверка результата
x = [int(i) for i in input().split()]
if c.Counter(result) == c.Counter(x):
    print("Верно")
else:
    print("Не верно")