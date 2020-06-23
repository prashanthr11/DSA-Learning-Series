n = int(input())
l = list()
l.append("*" * n)

for i in range(n, (2 * n) - 1):
    s = ""
    s += "~" * i
    s += "*"
    l.append(s)

for i in range((2 * n) - 3, n - 1, -1):
    s = ""
    s += "~" * i
    s += "*"
    l.append(s)

l.append("*" * n)
for i in l:
    print(i)
