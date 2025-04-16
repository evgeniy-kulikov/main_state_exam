"""
3 вариант
"""

# 05
for b in range(2, 100):
    if (4 + 3) * b + 3 + 3 + 3 == 51:
        print(b)  # 6


# 06
d = (12, -6), (13, -8), (11, -6), (13, -8), (-12, 7), (12, -6), (-12, -8), (13, -7), (11, -7)
cnt = 0
for s, t in d:
    cnt += s < 12 and t > -7
print(cnt)  # 2


# 10
n = min([0x29, 0o47, 0b100100])
print(n) # 36

# 12
import os
root = r'I:\__ОГЭ\_Book\_Ушаков Д.М. - ОГЭ. Информатика 2025\oge2025ast\z12\Серебро'
cnt = 0
for dirs, _, files in os.walk(root):
    for el in files:
        f = el.split('.')
        if f[0][0].lower() == 'в' and f[1][0].lower() == 'h':
            cnt += 1
            size = os.path.getsize(dirs + os.sep + el)
            print(cnt, el, size)
"""
1 Валерий Брюсов.htm 25800
2 Валерий Брюсов.html 46253
3 Владислав Ходасевич.html 60926
4 Владислав Ходасевич.htm 42532
5 Велимир Хлебников.htm 11805
6 Владимир Маяковский.htm 42691
"""

# 15.2
sm = 0
for _ in range(int(input())):
    n = int(input())
    # if abs(n) % 10 not in (3, 6):
    if str(n)[-1] not in '36':
        sm += n
print(sm)
"""
3
-27
325
-523
"""
# 298
