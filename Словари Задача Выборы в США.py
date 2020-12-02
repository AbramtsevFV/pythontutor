
dict = {}
cycle = int(input())

# создаём словарь
for i in range(cycle):
    k, v = input().split()
    v = int(v)
    if k not in dict:            # если ключ отсутствует в словаре
        dict[k] = v              # добовляем ключ со сзначением
    else:
        dict[k] += v             # иначе складываем текущее значение с новым

# вывод и сортировка

s = []
s.extend(dict.keys())           # все ключи добавляем в список
s.sort()                        # сортируем
for j in s:                     # интегрируемся по отсортированному списку
    print(j , dict[j])