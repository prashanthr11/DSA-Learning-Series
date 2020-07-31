from collections import defaultdict

def getlen(x):
    s = list(map(str, x))
    return len(s)

for i in range(int(input())):
    n = int(input())
    a, b = 3, 2
    d = defaultdict(list)
    for i in range(n + 1):
        for j in range(i):
            x = a * b
            y = "0" * (5 - getlen(str(x)))
            d[i].append(y + str(x))
            a, b = a + 4, b + 2
    for i in range(1, len(d) + 1):
        print(" " * (n - i) * 3, end = "")
        for j in d[i]:
            print(j, end = " ")
        print()
