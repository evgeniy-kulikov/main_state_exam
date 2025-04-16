"""
Ушаков 40 вариантов ОГЭ 2025
Вариант 1
"""

# 5
"""
1 --> +4
2 --> *b  (b >= 2)

2 [2] 8 * 2 [1] 20 [1] 24 [1] 28 [1] 32

b = 8
"""

# 6
cnt = 0
d = (5, -11), (-4, -11), (-5, 10), (-6, 11), (-5, 12), (-5, 12), (-4, 10), (-4, 12), (5, 10)
for s, t in d:
    cnt += s >= -5 and t >= 11
print(cnt)  # 3

# 10
print(max(0x3b, 0o77, 0b1000011))  # 67

# 15.1
import os
start = r'I:\__ОГЭ\_Book\_Ушаков Д.М. - ОГЭ. Информатика 2025\oge2025ast\z12\Серебро'
cnt = 0

for dr, _, files in os.walk(start):
    for fl in files:
        if fl.split('.')[-2][-1] == 'в':
            cnt += 1
            # w = os.path.join(dr, fl)
            # print(w.split('Серебро')[1])
print(cnt)  # 23

# 15.2
cnt = 0
for _ in range(int(input())):
    n = input()
    if len(n) == 2 and n[-1] not in '37':
        cnt += 1
print(cnt)

