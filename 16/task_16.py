"""
Авторские задачи по программированию Волгина Павла Михайловича и других хороших людей
https://pvolgin-task.ru
"""
# https://pvolgin-task.ru/variant013oge/
nums = set()
n = int(input())

while n:
    if len(str(n)) == 5 and str(n)[-3:] == '238':
        nums.add(n)
    n = int(input())

if not len(nums):
    print('NO')
elif len(nums) == 1:
    print(0)
else:
    print(min(nums) * max(nums))

"""
238
17238
134
32238
238
123238
0

555718644
"""


