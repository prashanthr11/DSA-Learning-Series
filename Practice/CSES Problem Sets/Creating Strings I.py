from itertools import permutations
s = input()
l = list(set(permutations(s)))
l.sort()
print(len(l))
for i in l:
    s = ''
    for j in i:
        s += j
    print(s)
