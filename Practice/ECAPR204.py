from collections import Counter
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    d = Counter(l)
    for k, v in sorted(d.items()):
        print("{}:{}".format(k, v))
