"""
Города
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия
каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится
данный город.
"""
dct = {}
another_dct = {}

for _ in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        if city in dct:
            another_dct[city] = country
        else:
            dct[city] = country

for _ in range(int(input())):
    city = input()
    if city in another_dct:
        print(dct[city])
        print(another_dct[city])
    else:
        print(dct[city])
