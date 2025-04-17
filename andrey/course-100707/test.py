# https://stepik.org/lesson/567042/step/10?unit=561316
n = int(input())
cash = [64, 32, 16, 8, 4, 2, 1]
for el in cash:
    while n // el != 0:
        n -= el
        print(el, end=' ')