# https://stepik.org/lesson/1084606/step/5?unit=1094968
def convert(num, base):
    res = ''
    while num:
        res = str(num % base) + res
        num //= base
    return res

a = 125 ** 200 + 74
for n in range(1000):
    num = a - 5 ** n
    if convert(num, 5).count('4') == 100:
        print(n)  # 502
        break


# https://stepik.org/lesson/1084606/step/6?unit=1094968
alfa = '0123456789ABCDE'
num = 11 * 15 ** 65 + 18 * 15 ** 38 - 14 * 15 ** 17 + 19 * 15 ** 11 + 18338
res = ''
while num:
    res = str(alfa[num % 15]) + res
    num //= 15
print(set(res))  # {'4', '8', '0', 'B', '5', '2', '7', 'E', '1', '6'}
print(len(set(res)))  # 10


# https://stepik.org/lesson/1084606/step/7?unit=1094968
alfa = '0' + '_' * 24
num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
res = ''
while num:
    res = str(alfa[num % 25]) + res
    num //= 25
print(res.count('0'))  # 9
print(res)  # _00000___0000________


# https://stepik.org/lesson/1084606/step/8?unit=1094968
alfa = '0123456789AB'
num = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
res = ''
while num:
    res = str(alfa[num % 12]) + res
    num //= 12
print(res.count('B'))  # 51


# https://stepik.org/lesson/1084606/step/9?unit=1094968
for n in range(1, 50):
    num = 36 ** 17 - 6 ** n + 71
    res = ''
    while num:
        res = str(num % 6) + res
        num //= 6
    if sum(map(int, res)) == 61:
        print(n)  # 24
        print(res)  # 5555555555000000000000000000000155
        break


# https://stepik.org/lesson/1084606/step/9?unit=1094968
num = 5 * 216 ** 1156 - 4 * 36 ** 1147 + 6 ** 1153 - 875
res = ''
while num:
    res = str(num % 6) + res
    num //= 6
print(res.count('5') - res.count('0'))  # 1182


# https://stepik.org/lesson/1107348/step/1?unit=1118586
for n in range(100):
    if int('33', n + 4) == 33 + int('33', 4):
        print(n)  # 11
        break


# https://stepik.org/lesson/1107348/step/3?unit=1118586
for n in range(10, 37):  # (n >= 2  and n <= 36)  and n >= 10
    if int('103', n) == int('97', n + 2):
        print(n)  # 11
        break


# https://stepik.org/lesson/1107348/step/3?unit=1118586
for n in range(5, 37):  # n >= 5  and (n >= 2  and n <= 36)
    if int('132', n) + int('13', 8) == int('124', n + 1):
        print(n)  # 6
        break


# https://stepik.org/lesson/1107348/step/4?unit=1118586
for n in range(100):
    if (2 * n + 1) * (n + 3) == 3 * n ** 2 + n + 3:
        print(n)  # 6
        break


# https://stepik.org/lesson/1107348/step/5?unit=1118586
for x in range(20, 31):
    res = ''
    n = x
    while n:
        res = str(n % 3) + res
        n //= 3
    if res[-2:] == '11':
        print(x)  # 22


# https://stepik.org/lesson/1107348/step/7?unit=1118586
for x in range(2, 10):
    res = ''
    n = 68
    while n:
        res = str(n % x) + res
        n //= x
    if len(res) == 4 and res[-1] == '2':
        print(x, f"'{res}'")  # 3 '2112'


# https://stepik.org/lesson/1107348/step/8?unit=1118586
def conv(num, base):
    res = ''
    while num:
        res = str(num % base) + res
        num //= base
    return res

for n in range(2, 100):
    if all([len(conv(n, 6)) == 2, len(conv(n, 5)) == 3, conv(n, 11)[-1] == '1']):
        print(n)  # 34
        break



# https://stepik.org/lesson/1107348/step/9?unit=1118586
def conv(num, base):
    res = ''
    while num:
        res = str(num % base) + res
        num //= base
    return res

cnt = 0
for n in range(2, 1000):  # range(28, 625)
    if all([len(conv(n, 5)) <= 4, len(bin(n)[2:]) >= 5, hex(n)[-1] == 'c']):
        cnt += 1
print(cnt)  # 38


# вариант
n_max = 0
for i in range(2, 10_000):
    res, num = '', i
    while num:
        res = str(num % 5) + res
        num //= 5
    if len(res) > 4:
        n_max = i
        break

cnt = 0
for n in range(int('10000', 2), n_max):  # range(28, 625)
    if hex(n)[-1] == 'c':
        cnt += 1
print(cnt)  # 38








