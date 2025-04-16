""""""
"""
Task 12
Подготовка к ОГЭ по информатике
https://stepik.org/course/50659
"""


# https://stepik.org/lesson/667765/step/1?unit=665862
import os
root = r'I:\__ОГЭ\12\course-50659\DEMO-12'
cnt = 0
for el in os.walk(root):
    folder, _, file = el
    for f in file:
        if f.split('.')[-1] == 'rtf':
            way = os.path.join(folder, f)
            if os.path.getsize(way) > 2 * 2**20:
                cnt += 1
                # print(f, os.path.getsize(way))
print(cnt)  # 5


# https://stepik.org/lesson/667765/step/2?unit=665862
# Ручной поиск:  *."htm"
import os
root = r'I:\__ОГЭ\12\course-50659\DEMO-12'
cnt = 0
for el in os.walk(root):
    folder, _, file = el
    for f in file:
        if f.split('.')[-1] == 'htm':
            # way = os.path.join(folder, f)
            # if os.path.getsize(way) >= 2**20:
            size = os.path.getsize(folder + os.sep + f)
            if size >= 2**20:
                print(f, f'{size/2**20:.2f}')  # :.2f  - 2 разряда после запятой
                cnt += 1
print(cnt)  # 3


# https://stepik.org/lesson/667765/step/3?unit=665862
import os
root = r'I:\__ОГЭ\12\course-50659\Files'
cnt = 0
for el in os.walk(root):
    folder, _, file = el
    for f in file:
        if f.split('.')[-1] == 'py':
            cnt += 1
print(cnt)  # 4

# https://stepik.org/lesson/667765/step/4?unit=665862
# Ручной поиск:  *.pdf
import os
root = r'I:\__ОГЭ\12\course-50659\Task12'
cnt = 0
for el in os.walk(root):
    folder, _, file = el
    for f in file:
        if f.split('.')[-1] == 'pdf':
            cnt += 1
print(cnt)  # 7


# https://stepik.org/lesson/667765/step/5?unit=665862
# Ручной поиск:  *.doc OR *.docx
import os
root = r'I:\__ОГЭ\12\course-50659\Task12'
cnt = 0
for el in os.walk(root):
    folder, _, file = el
    for f in file:
        if f.split('.')[-1] in ('docx', 'doc'):
            cnt += 1
print(cnt)  # 5


# https://stepik.org/lesson/667765/step/6?unit=665862
# Ручной поиск:  *.doc OR *.docx
import os
root = r'I:\__ОГЭ\12\course-50659\DEMO-12(1)'
cnt = 0
for el in os.walk(root):
    folder, _, file = el
    for f in file:
        if f.split('.')[-1] in ('docx', 'doc'):
            cnt += 1
print(cnt)  # 4


# https://stepik.org/lesson/667765/step/7?unit=665862
# Ручной поиск:  *.txt
import os
root = r'I:\__ОГЭ\12\course-50659\DEMO-12(1)\Проза'
cnt = 0
for el in os.walk(root):
    folder, _, file = el
    for f in file:
        if f.split('.')[-1] == 'txt':
            cnt += 1
print(cnt)  # 16

