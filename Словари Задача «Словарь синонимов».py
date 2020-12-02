
cycl = int(input())
dict = {}

# создаём стандартный словарь ключ значение

for i in range(cycl):
    key, val = input().split()
    dict[key] = val

sinonim = input()

# поиск по словарю реализован на основе цикла for
# и мотода items(), который возращает ключ, значение
# если найден печатаем синоним и выходим из цикла

for k, v in dict.items():
    if k == sinonim:
        print(v)
        break
    elif v == sinonim:
        print(k)
        break