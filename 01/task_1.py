"""
Демонстрационный вариант ЕГЭ 2025
"""

# 01
from itertools import permutations
g = {"A": "BC", "B": "AD", "C": "EGA", "D": "FGB", "E": "FC", "F": "EGD", "G": "CFD"}
t = "0001101" + "0001010" + "0000111" + "1100000" + "1010010" + "0110100" + "1010000"
for p in permutations(g):  # ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    tn = ""
    for k in p:
        for v in p:
            if v in g[k]:
                tn += "1"
            else:
                tn += "0"
    if tn == t:
        print(*p)  # C B F A G D E
