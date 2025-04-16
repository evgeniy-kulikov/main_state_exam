#  https://stepik.org/lesson/983014/step/2?thread=solutions&unit=990285
from itertools import permutations
g = {"А": "БВГ", "Б": "АВЕЖ", "В": "БАГ", "Г": "АВЕД", "Д": "ГЕ", "Е": "ЖБГД", "Ж": "БЕ"}
t = "0110100" + "1011001" + "1100100" + "0100001" + "1010011" + "0000101" + "0101110"
# print(len(g), len(t))
print(*range(1, 8))
for p in permutations(g):
    tn = ""
    for k in p:
        for v in p:
            if v in g[k]:
                tn += "1"
            else:
                tn += "0"
    if tn == t:
        print(*p)
"""
1 2 3 4 5 6 7
А Б В Ж Г Д Е  -
А Г В Д Б Ж Е  +
В Б А Ж Г Д Е  -
В Г А Д Б Ж Е  -

1 2 3 4 5 6 7
А Г В Д Б Ж Е
ВГЕ = 26 +  # 26
ИБЕ = 32 -
"""