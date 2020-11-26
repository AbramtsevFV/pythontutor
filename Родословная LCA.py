import collections
dict_tree = {}
parents = []
result = []
# формирует список родителей с конца
def poisk_parent(name):
    if name in dict_tree:           # проверяет наличие имени в словаре (ребёнка)
        name = dict_tree[name]      # name меняет значение на имя родителя
        parents.append(name)        # добовляет в список
        poisk_parent(name)          # рекурсия и так пока не закончится

# проверяет является ли значение из списка родителей родителем данного ребёнка
def proverka(name, parent):
    if name in dict_tree:
        name = dict_tree[name]
        if parent == name:                  # родитель или нет
            return True
        else:
           return proverka(name, parent)    # елси нет, рекурсия

cycl = int(input())

# заполняем словарь типа ребёнок -- родтитель
for i in range (cycl-1):
    k, v = input().split()
    dict_tree[k] = v

cycl2 = int(input())

for j in range(cycl2):
    child1, child2 = input().split()
    parents.append(child1)                  # добовляем для проверки в спискок родителей
    poisk_parent(child1)                    # вызываем функцию
    if child2 in parents:                   # если есть в списке родителей
        result.append(child2)               # добовляем в результат
        parents.clear()                     # очищаем список
    else:
        for k in parents:                   # проверка по списку
            if proverka(child2, k):
                result.append(k)
                parents.clear()
                break
print('\n'.join(result))

#функция проверки доп. опция
def proverka1():
    r = []
    for i in range(cycl2):
        s = input()
        r.append(s)
    if collections.Counter(result) == collections.Counter(r):
         print("Всё верно")
    else:
        print("Не верно")

# если совсем плохо, не работае без "proverka1"

def proverka():

    for k in range(len(result)):
        if result[k] != r[k]:
            print(f'то что у меня {result[k]}, верно{r[k]}, индекс{k}')