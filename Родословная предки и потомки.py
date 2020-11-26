import collections
dict_tree = {}
cycl = int(input())
rodoslovnost = []
# рекурсивная функция
def scht (child, parent):
    if child not in dict_tree:          # если нет в ключах словоря
        return False
    else:
        child = dict_tree[child]        # проверяем родителя
        if parent == child:             # ЕСЛИ ДА True
            return True
        return scht(child, parent)       # Если нет вызываем следеюших и проверяем

# по сути функция рекурсивно проходит по всем значениям потомок родитель, от самого молодого к
# к родоночальнику

# ввод данных и создание словаря, создаётся словарь потомок -- родитель
for i in range(cycl-1):
    k, v = input().split()
    dict_tree[k] = v


cycl_out = int(input())
for x in range(cycl_out):
    k, v = input().split()
    if scht(v,k):
        rodoslovnost.append(1)
    elif scht(k, v):
        rodoslovnost.append(2)
    else:
        rodoslovnost.append(0)
print(*rodoslovnost)

# проверка результатов
d = [ int(i) for i in input().split()]

# проверка элементов Counter возрщает словарь типа: Counter({0: 52, 1: 19, 2: 19})
if collections.Counter(rodoslovnost) == collections.Counter(d):
	print ("Списки одинаковые")
else:
	print ("Списки неодинаковые")