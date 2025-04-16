# 7.8 Вложенные циклы. Часть 1

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
for i in range(1, n + 1):
    if i <= int(n / 2 + 1):
        print('*' * i)
        continue
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
for a in range(1, 101):
    for b in range(1, 101):
        for c in range(1, 101):
            if 10 * a + 5 * b + 0.5 * c == 100 and a + b + c == 100:
                print(f'Быков = {a}, Коров = {b}, Телят = {c}')
# Быков = 1, Коров = 9, Телят = 90


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