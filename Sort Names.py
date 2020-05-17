n = int(input())

l = list()
for i in range(n):
    s = input()
    l.append(s)
    
for i in sorted(l):
    print(i, end=' ')
