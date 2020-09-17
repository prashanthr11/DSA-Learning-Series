n = int(input())
l = list()
for i in range(n):
    a = int(input())
    l.append(a)

l= sorted(l)

for i in range(len(l)):
    l[i] *= n
    n -= 1

print(max(l))
