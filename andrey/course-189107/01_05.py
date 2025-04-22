"""
1.5 Вложенные циклы
"""
# https://stepik.org/lesson/1155438/step/2?unit=1167633
lst = ["мыть  или не  мыть вот   в чем вопрос", "наташа   ростова приключения во вьетнаме",
      "лучший курс   на степике", "утка   кря кря кря   папа хрю хрю хрю"]
for i, s in enumerate(lst):
    while '  ' in s:
        s = s.replace('  ', ' ')
    lst[i] = s.replace(' ', '-')
print(lst)


# https://stepik.org/lesson/1155438/step/3?unit=1167633
for i in range(1, int(input()) + 1):
    print(*range(1, i + 1))

# вариант
for i in range(1, int(input()) + 1):
    s = []
    for k in range(1, i + 1):
        s += [k]
    print(*s)


# https://stepik.org/lesson/1155438/step/4?unit=1167633
for i in map(int, input().split()):
    print('*' * i)


# https://stepik.org/lesson/1155438/step/5?unit=1167633
a, b = map(int, input().split())
print([['?' for _ in range(b)] for _ in range(a)])

# вариант
ls = []
for i in range(a):
    ls.append([])
    for _ in range(b):
        ls[-1].append('?')
print(ls)


# https://stepik.org/lesson/1155438/step/6?unit=1167633
n = int(input())
w = [2 ** i for i in range(6, -1, -1)]  # [64, 32, 16, 8, 4, 2, 1]
res = []
for el in w:
    # while n // el:
    while n >= el:
        n -= el
        res.append(el)
print(res)

# https://stepik.org/lesson/1155438/step/8?unit=1167633
import sys
lst = sys.stdin.readlines()
lst = [list(map(int, i.split())) for i in lst]
# lst = [[1, 2, 3, 4, 5],
#        [1, 2, 3, 4, 5],
#        [1, 2, 3, 4, 5],
#        [1, 2, 3, 4, 5],
#        [1, 2, 3, 4, 5]]
sm = 0
for row in range(len(lst)):
    for col in range(len(lst[0])):
        if col == row:
            sm += lst[row][col]
print(sm)

# вариант
print(sum(lst[i][i] for i in range(len(lst))))


# https://stepik.org/lesson/1155438/step/9?unit=1167633
foto = [
    [['B', 'W', 'Y'], ['C', 'Y', 'M'], ['M', 'B', 'W']],
    [['B', 'B', 'W'], ['W', 'W', 'B'], ['W', 'B', 'W']],
    [['C', 'B', 'W'], ['B', 'W', 'Y'], ['B', 'W', 'B']],
    [['W', 'B', 'W'], ['B', 'W', 'B'], ['B', 'W', 'B']],
    [['C', 'B', 'Y'], ['B', 'C', 'Y'], ['Y', 'W', 'B']]
]

for row in foto:
    flag = False
    for el in row:
        for i in el:
            if i in 'CYM':
                flag = True
    if flag:
        print('Цветная')
    else:
        print('Ч/Б')
    flag = False

# Короче
for row in foto:
    idx = any(i in 'CYM' for el in row for i in el)
    print(['Ч/Б', 'Цветная'][idx])

# Баловство
[print(['Ч/Б', 'Цветная'][any(i in 'CYM' for el in row for i in el)]) for row in foto]