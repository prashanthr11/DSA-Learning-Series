from collections import defaultdict
d = defaultdict(int)
cur = glo = 0
ans = ''
for i in range(int(input())):
    l = list(input().split())
    a = l[0]
    b = int(l[1])
    d[a] = d.get(a, 0) + b
    cur = max(cur, max(list(d.values())))
    if cur != glo:
        glo = cur
        ans = a
print(ans)
