"""
Добрый, добрый Python с Сергеем Балакиревым
https://stepik.org/course/100707?search=6938055054
"""
"""
5.6 Вложенные циклы
https://stepik.org/lesson/567042?unit=561316
"""

# https://stepik.org/lesson/567042/step/3?unit=561316
n = int(input())
for _ in range(n):
    for __ in range(n - 1):
        print(1, end=' ')
    print(5)
# 1 1 5
# 1 1 5
# 1 1 5


# https://stepik.org/lesson/567042/step/4?unit=561316
import sys
# считывание списка из входного потока
ls_in = list(map(str.strip, sys.stdin.readlines()))

for el in ls_in:
    ls_out = "-".join(el.split())
    print(ls_out)

# https://stepik.org/lesson/567042/step/5?unit=561316
num = int(input())
for el in range(2, num):
    flag = True
    for i in range(2, int(el**0.5 + 1)):
        if el % i == 0:
            flag = False
            break
    if flag:
        print(el, end=' ')
        flag = True

# короче
num = int(input())
for i in range(2, num):
    for k in range(2, int(i**0.5 + 1)):
        if not i % k:
            break
    else:
        print(i, end=' ')


# https://stepik.org/lesson/567042/step/6?unit=561316
import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
ls = [list(map(int, x.strip().split())) for x in s]

res = 'ДА'
for i in range(4):
    for j in range(4):
        if sum([ls[i][j], ls[i][j + 1], ls[i + 1][j], ls[i + 1][j + 1]]) > 1:
            res = 'НЕТ'
            break
print(res)


# https://stepik.org/lesson/567042/step/7?unit=561316
import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
ls = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список ls)
res = 'ДА'
for row in range(5):
    for col in range(row + 1, 5):
        if ls[row][col] != ls[col][row]:
            res = 'НЕТ'
            break
print(res)

# https://stepik.org/lesson/567042/step/8?unit=561316
ls = list(map(int, input().split()))

for i in range(len(ls)):
    for k in range(i, len(ls)):
        if ls[i] > ls[k]:
            ls[i], ls[k] = ls[k], ls[i]
print(*ls)


# https://stepik.org/lesson/567042/step/9?unit=561316
ls = list(map(int, input().split()))
for i in range(len(ls) - 1):
    for k in range(len(ls) - 1 - i):  # "- i" сокращаем обходы в правой части
        if ls[k] > ls[k + 1]:
            ls[k], ls[k + 1] = ls[k + 1], ls[k]
print(*ls)



# https://stepik.org/lesson/567042/step/10?unit=561316
n = int(input())
cash = [64, 32, 16, 8, 4, 2, 1]
for el in cash:
    while n >= el:
    # while n // el != 0:
        n -= el
        print(el, end=' ')




