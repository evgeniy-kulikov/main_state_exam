# ввод данных в лист, пока не будет введен 0 (ноль)
# res = list(iter(lambda: int(input()), 0))


# import sys
# min_n = sys.maxsize  # максимальное значение числа для интерпретатора


# from statistics import mean
# ls = []
# s = "таких цифер нет" + "\n" + "минимального значения нет"
#
# while True:
#     n = int(input())
#     if not n:
#         break
#     if n % 5 != 0 or n % 10 == 6:
#         ls += [n]
#
# if ls:
#     print(round(mean(ls), 1))
#     print(min(filter(lambda x: x % 5 == 1, ls), default="минимального значения нет"))
# else:
#     print(s)

# cnt = 0
# while True:
#     n = int(input())
#     if not n:
#         break
#     if len(str(n)) == 2 and n % 5 == 0:
#         cnt += 1
#
# print(cnt)

# wrong, vin = 1, 0
#
# for i in range(int(input())):
#     if i > vin:
#         vin = i
#     if i == 0:
#         wrong = 0
#
# print(vin)
# print(['NO', 'YES'][wrong])


# import os
#
# our_dir = r'I:\__ОГЭ\_Test\easy-exam\test209\DEMO-12'
# cnt = 0
#
# for folder, _, files in os.walk(our_dir):
#     for file in files:
#
#         # ограничения
#         # if 'Проза' in _: # Исключить данный каталог из поиска (при наличии файлов рядом с ним)
#         #     _.remove('Проза')
#
#         way = folder + os.sep + file  # os.sep == '\\'
#         size = os.path.getsize(way)
#         if size > 1024 ** 2:
#         # if size > 1024 ** 2 and file.lower()[-4:] == '.pdf' and 'DEMO-12\\Поэзия' in folder:  # ограничения
#             cnt += 1
#             print(folder, file, size)
#
# print(cnt)

#
# num = 589  # десятичное число
# base = 8  # база системы счисления
# res = ''
#
# while num:
#     res = str(num % base) + res
#     num //= base
# print(res)

# import os

# our_dir = r'I:\__ОГЭ\_Book\Ушаков Д.М. - ОГЭ. Информатика 2025\oge2025ast\z12\Серебро'
# cnt = 0
# for folder, _, files in os.walk(our_dir):
#     for f in files:
#         # way = our_dir + os.sep() + f
#         s = f.split('.')[-2]
#         if s[-1] == 'в':
#             cnt += 1
#             print(f)
# print(cnt)

# n = float(input())
# a, b = int(input()), int(input())
# if a == b:
#     print('Оба молодцы')
# elif a < b:
#     print('Петя молодец')
# else:
#     print('Дима молодец')

# a, b = int(input()), int(input())
# if a >= b:
#     print('Пора покупать мышку')
# else:
#     print('Пока без мышки')

# ls = [int(input()) for _ in range(4)]
# d, v = sum(ls[0:2]), sum(ls[2:])
# if d == v:
#     print('ничья')
# elif d > v:
#     print('"выигрывает Дима')
# else:
#     print('выигрывает Вася')


# d = [int(input()) for _ in range(3)]
# n = sorted(d)
# print(f"числа {'не ' * (d != n)}по возрастанию")

# print(['орел', 'решка'][int(input()) - 1])

# a, b = int(input()), int(input())
# if a == b:
#     print('ничья')
# else:
#     print(f"выигрывает {['Дима', 'Вася'][a > b]}")

# a, b, c = [int(input()) for _ in range(3)]
# if a < b < c:
#     print(a + b + c)
# else:
#     print(a * b * c)

# a, b = int(input()), int(input())
# for i in range(b, a, -2):
#     print(i)

# ****************************************************************************************
# ****************************************************************************************

# # 20-12
# import os
#
# main = r'I:\__ОГЭ\12\z1114\z12\Серебро'
# cnt = 0
#
# for full_dr, _, files in os.walk(main):
#     for file in files:
#         i = file.rindex('.') + 1
#         if file[i:] == 'txt':
#             cnt += 1
#             print(full_dr[20:] + os.sep + file)
# print(cnt)  # 7


# # 18-12
# import os
#
# main = r'I:\__ОГЭ\_Book\_Ушаков Д.М. - ОГЭ. Информатика 2025\oge2025ast\z12\Серебро'
# cnt = 0
#
# for full_dr, _, files in os.walk(main):
#     for file in files:
#         way = full_dr + os.sep + file
#         file_size = os.path.getsize(way)
#         if file_size <= 140 * 1024:
#             if 'о' in file:
#                 cnt += 1
#                 print(full_dr[-20:] + os.sep + file, file_size)
# print(cnt)  # 73 (ответ не совпадает. Условие задания неверное)

# ****************************************************************************************
# ****************************************************************************************

# s = 'Россия матушка!'
# print(len(s) * 16)

# d = (1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)
# c = 0
# for s, t in d:
#     if not (s < 10 or t > 10):
#         c += 1
# print(c)

# print(int('22', 16))
# print(int('37', 8))
# print(int('11110', 2))

# n_min = 30_001
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if n < n_min:
#         n_min = n
# print(n_min)

# a, b = int(input()), int(input())
# c = 0
# for i in range(a, b + 1):
#     if i % 2 == 1:
#         c += 1
# print(c)


# n = (13, 2), (11, 12), (-12, 12), (2, -2), (-10, -10), (6, -5), (2, 8), (9, 10), (1, 13)
# for a in range(1, 30):
#     c = 0
#     for s, t in n:
#         if s > a or t > 12:
#             c += 1
#     if c == 3:
#         print(a)  # 9
#         break


# n = int(input())
# cnt = 0
#
# for _ in range(n):
#     i = int(input())
#     if i % 6 == 0:
#         cnt += 1
#
# print(cnt)


# n = int(input())
# n_max = 0
#
# for _ in range(n):
#     i = int(input())
#     if i % 10 == 4 and i > n_max:
#         n_max = i
#
# print(n_max)


# n = int(input())
# cnt = 0
#
# while n:
#     if n % 5 == 0 or n % 9 == 0:
#         cnt += 1
#     n = int(input())
#
# print(cnt)


# n = int(input())
# n_min = 30_001
#
# while n:
#     if n < n_min:
#         n_min = n
#         n = int(input())
#
# print(n_min)


# n = int(input())
# cnt = 0
# flag = False
#
# for _ in range(n):
#     i = int(input())
#     if i == 10:
#         flag = True
#     if i < 5:
#         cnt += 1
#
# print(cnt)
# print(['NO', 'YES'][flag])


# n = int(input())
# cnt = 0
#
# while n:
#     if n % 4 == 0 and n % 9 == 0:
#         cnt += 1
#     n = int(input())
#
# print(cnt)


# n = int(input())
# n_max = 0
#
# for _ in range(n):
#     i = int(input())
#     if i % 10 == 3 and i > n_max:
#         n_max = i
#
# print(n_max)

# import os
# root = r'I:\__ОГЭ\_Test\Stepik 104797\Test\01\oge12\Проза'
# sm = 0
# for dr, _, fl in os.walk(root):
#     for f in fl:
#         i = f.rfind('.') + 1
#         if f[i:] == 'htm':
#             sm += os.path.getsize(dr + os.sep + f)
# print(sm / 1024 / 1024)  # 8.2880220413208
#
# res = str(sm / 1024 / 1024)
# print(res[:res.find('.') + 3])  # 8.28


# address = '192.168.32.160'.split('.')
# one = 0
# for i in address:
#     one += bin(int(i)).count('1')
# print(one)  # 8 единиц в адресе
#
# cnt = 0
# for i in range(256 - 248):
#     if bin(i).count('1') % 2 != 0:
#         cnt += 1
# print(cnt)  # 4
#
#
# print(64 & 255, 128 & 255, 224 & 208, 194 & 0)

# https://stepik.org/lesson/1074876/step/14?unit=1095106
# Сеть задана IP-адресом 202.75.38.152 и маской сети 255.255.255.248
# Сколько в этой сети IP-адресов, у которых в двоичной записи IP-адреса имеется сочетание трех подряд идущих единиц ?
# from ipaddress import ip_network
#
# cnt = 0
# for adr in ip_network('202.75.38.152/255.255.255.248'):
#     if '111' in f'{adr:b}':
#         # if bin(int(adr))[2:].count('0') == 16:
#         cnt += 1
# print(cnt)  # 4


# https://stepik.org/lesson/1074877/step/4?thread=solutions&unit=1095107
# Для узла с IP-адресом 111.81.208.27 адрес сети равен 111.81.192.0
# Чему равно наименьшее возможное значение третьего слева байта маски ?
# from ipaddress import *
#
# for i in range(1, 33):  # перебор маски
#     try:
#         net = ip_network(f'111.81.192.0/{i}')
#         if ip_address('111.81.208.27') in net:
#             print(str(net.netmask))  # 192
#     except:
#         pass
# 255.255.192.0
# 255.255.224.0

""""""
""""""

#  https://stepik.org/lesson/1074878/step/7?unit=1095109
# Сеть задана IP-адресом одного из входящих в неё узлов 135.13.142.29 и сетевой маской 255.255.255.128.
# Найдите наибольший IP-адрес в данной сети, который может быть назначен компьютеру.
# from ipaddress import ip_network
# cnt = 0
# for i in ip_network('112.160.0.0/12'):
#     cnt += not f'{i:b}'.count('1') % 3 == 0
# print(cnt)  # 699050

