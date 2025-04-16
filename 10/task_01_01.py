# Информатика Подготовка к ЕГЭ 2025
# https://stepik.org/course/182932/
""""""

# https://stepik.org/lesson/255058/step/1?unit=235266
from itertools import product
cnt = 0
for p in product('ЕГЭ', repeat=5):
    if p[0] in 'ЕЭ':
        cnt += 1
print(cnt)  # 162

# https://stepik.org/lesson/255058/step/2?unit=235266
from itertools import product
cnt5 = 0
cnt6 = 0
for p in product('АТГЦ', repeat=5):
    cnt5 += 1
for p in product('АТГЦ', repeat=6):
    cnt6 += 1
print(cnt5 + cnt6)

# https://stepik.org/lesson/255058/step/3?unit=235266
from itertools import product
cnt = 0
for p in product('СЛОН', repeat=5):
    if p.count('С') == 1:
        cnt += 1
print(cnt)  # 405

# https://stepik.org/lesson/255058/step/4?unit=235266
from itertools import product
cnt = 0
for p in product('ABCX', repeat=5):
    if not p.count('X') or (p.count('X') == 1 and p[-1] == 'X'):
        cnt += 1
print(cnt)  # 324

# https://stepik.org/lesson/255058/step/5?unit=235266
from itertools import product
cnt = 0
for p in product('АБВГ', repeat=5):
    if p.count('А') == 1:
        cnt += 1
print(cnt)  # 405


# https://stepik.org/lesson/255058/step/6?unit=235266
from itertools import product
for n in range(10):
    cnt = 0
    for p in product('1234', repeat=n):
        cnt += 1
    if cnt >= 300:
        print(cnt)  # 1024
        print(n)  # 5
        break
"""
Для письменного решения задания воспользуемся формулой
4 ** n = x
где n — количество лампочек, а x — количество сигналов, которые можно закодировать таким количеством лампочек. 
4 — это количество состояний одной лампочки (красный, желтый, белый, черный).
Нам нужно наименьшее количество лампочек, то есть мы можем составить неравенство:
4 ** n >= 300, где наименьший n будет наименьшим количеством лампочек.
Наименьший n для этого неравенства — 5, так как 4 ** 4=256, а 4 ** 5=1024
"""
# Лучший подход
for n in range(20):
    if 4 ** n > 300:
        print(n, 4 ** n)  # 5 1024
        break




