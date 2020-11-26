dict_sum = {}
dict_tree = {}
names = set()
cycl = int(input())

# рекурсивная функция
def scht (name, lv = 0):
    if dict_tree.get(name) != None:             # проверка на выход
        for s in dict_tree[name]:               # для каждого потомка проверка, проверяютсявсе родители
           return scht(s, lv + 1)               # менятся уровень
    return lv                                   # возврат уровня родословной

# ввод данных и создание словаря, создаётся словарь потомок -- родитель
#  с условием, что у одного потомка несколько родителей
# на строке 21 создаётся дополнительный словарь уровней
# все именя потомков и родителеё добовляются во опорное множество для исключения дубликатов (стр 23-24)

for i in range(cycl-1):
    k, v = input().split()
    if dict_tree.get(k) == None:
        dict_tree[k] = [v]
        dict_sum[k] = 0
        names.add(k)
        names.add(v)
    else:
        s = []
        s.extend(dict_tree[k])
        s.append(v)
        dict_tree[k] = s

for name in names:
    if name  in dict_tree:                  # если отсутствует в словаре детей значит это родоначальник
        dict_sum[name] += scht(name)
    else:
        dict_sum[name] = 0                  # и уровень 0

sum = list(dict_sum.keys())                 # все ключи переносим в список
sum.sort()                                  # сортируем
for k in sum:                               # и  выводим в отсортированном виде
    v= dict_sum[k]
    print(k, v)