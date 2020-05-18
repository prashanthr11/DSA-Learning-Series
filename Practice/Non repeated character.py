s = input()
s2 = input()

d = dict()
for i in range(len(s)):
    d[s[i]] = d.get(s[i], 0) + 1
    
for i in range(len(s2)):
    if s2[i] not in d:
        print(s2[i], end='')
