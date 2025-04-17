"""
https://stepik.org/course/58852/syllabus
Поколение Python": курс для начинающих
"""
"""
7.8 Вложенные циклы. Часть 1
https://stepik.org/lesson/298795/step/1?unit=280622
"""

# https://stepik.org/lesson/298795/step/5?unit=280622
n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
# 3 3 3
# 3 3 3
# 3 3 3

# https://stepik.org/lesson/298795/step/6?unit=280622
n = int(input())
for i in range(1, n + 1):
    print(f'{i} ' * 5)
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3


# https://stepik.org/lesson/298795/step/7?unit=280622
n = int(input())
for i in range(n):
    print()
    for k in range(1, 10):
        print(f'{i + 1} + {k} = {k + i + 1}')


# https://stepik.org/lesson/298795/step/8?unit=280622
n = int(input())
half = (n + 1) // 2

for i in range(1, half):
    print('*' * i)

for i in range(half, 0, -1):
    print('*' * i)

# Одним обходом
n = int(input())
for i in range(1, n + 1):
    if i <= n // 2 + 1:
        print('*' * i)
    else:
        print('*' * (n - i + 1))
# *
# **
# ***
# **
# *


# https://stepik.org/lesson/298795/step/9?unit=280622
n = int(input())
for i in range(1, n + 1):
    print(str(i) * i)
# 1
# 22
# 333

# https://stepik.org/lesson/298795/step/12?thread=solutions&unit=280622
for b in range(1, 101):
    for k in range(1, 101):
        for t in range(1, 101):
            if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
                print(f'Быков: {b}\nКоров: {k}\nТелят: {t}')
# Быков: 1
# Коров: 9
# Телят: 90


# https://stepik.org/lesson/298795/step/13?unit=280622
def f():
    for a in range(1, 151):
        for b in range(a, 151):
            for c in range(b, 151):
                for d in range(c, 151):
                    abcd = a ** 5 + b ** 5 + c ** 5 + d ** 5
                    e = int(abcd ** (1 / 5))
                    if e ** 5 == abcd:
                        return a + b + c + d + e
print(f())  # 498


"""
7.9 Вложенные циклы. Часть 2
https://stepik.org/lesson/298796/step/1?unit=280623
"""
# https://stepik.org/lesson/298796/step/1?unit=280623
n = int(input())
cnt = 0
for i in range(1, n + 1):
    for m in range(i):
        cnt += 1
        print(cnt, end=' ')
    print()
# 1
# 2 3
# 4 5 6


# https://stepik.org/lesson/298796/step/2?unit=280623
n = int(input())
for i in range(1, n + 1):
    for a in range(1, i):
        print(a, end='')
    for b in range(i, 0, -1):
        print(b, end='')
    print()
# 1
# 121
# 12321
# 1234321


# https://stepik.org/lesson/298796/step/3?unit=280623
a, b = int(input()), int(input())
n_max, sm_div = 0, 0

for i in range(a, b + 1):
    cnt_dv = 0
    for k in range(1, i + 1):
        if i % k == 0:
            cnt_dv += k
    if cnt_dv >= sm_div:
        sm_div = cnt_dv
        n_max = i
print(n_max, sm_div)


# https://stepik.org/lesson/298796/step/4?unit=280623
n = int(input())
for i in range(1, n + 1):
    print(i, end='')
    for k in range(1, i + 1):
        if i % k == 0:
            print('+', end='')
    print()
# 1+
# 2++
# 3++
# 4+++


# https://stepik.org/lesson/298796/step/5?unit=280623
n = int(input())
while n > 9:
    tmp = 0
    for i in str(n):
        tmp += int(i)
    n = tmp
print(n)

# короче
n = sum(map(int, input()))
while n > 10:
    n = sum(map(int, str(n)))
print(n)


# https://stepik.org/lesson/298796/step/7?unit=280623
a = int(input())
b = int(input())

for i in range(a, b + 1):
    flag = True
    for k in range(2, i):
        if i % k == 0:
            flag = False
            break
    if flag and i > 1:
        print(i)
