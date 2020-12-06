# создаём словарь с расшифровками значений
access_rights = {"write": "W",
                 "execute": "X",
                 "read": "R"
}

dict_file = {}

res = []
# создаём словарь типа {'helloworld.exe': ['R', 'X']}
# ключ это имя файла, значение список операций над файлом

for i in range(int(input())):
    k = [i for i in input().split()]
    dict_file[k[0]] = k[1:]

for j in range(int(input())):
    k, v = input().split()
    access = access_rights[k]           # меняем имя операции в нужный нам формат с помощью словаря
    if access in dict_file[v]:          # проверяем есть ли среди разрешенных нужная нам операция
        res.append("OK")
    else:
        res.append("Access denied")

print('\n'.join(res))                   # результат выводим в столбик с помощью метода join
