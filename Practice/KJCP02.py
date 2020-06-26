from collections import Counter
for i in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    s, b = Counter(l[:n]), l[n:]
    for i in b:
        if s[i]:
            print("YES")
        else:
            s[i] = 1
            print("NO")
    
