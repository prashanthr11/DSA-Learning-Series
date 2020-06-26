from collections import defaultdict
for i in range(int(input())):
    l = list()
    for j in range(int(input())):
        l.append(list(map(str, input().split())))
    d = defaultdict(int)
    l2 = list()
    for i in range(len(l)):
        if d[l[i][0]]:
            l2.append(l[i][0])
        else:
            d[l[i][0]] = 1
    
    for i in range(len(l)):
        if l[i][0] in l2:
            temp = l[i][0] + ' ' + l[i][1]
            print(temp)
        else:
            print(l[i][0])
        
