def solve(l):
    t = l.replace('|', ' ')
    t = list(t.split())
    t = [i for i in t if len(i) != 1]
    Alen = 0
    for i in t:
        Alen += len(i) - 1
    A = [0] * Alen

    for i in range(len(t)):
        val = t[i][-1]
        ind = t[i][:-1]
        ind = [int(i) for i in ind]
        for i in ind:
            A[int(i)] = int(val)
        
    return A

def solve2(l, ind):
    # print(ind)
    for i in ind:
        l[int(i)] += 10
    # print(l)
    return l
    
    
def solve3(l, ind):
    ret = [0] * len(l)
    ret[0] = ind
    ret[-1] = l[-1] - ind
    for i in range(len(l) - 2, 0, -1):
        ret[i] = l[i] - ret[i + 1]
    return ret
    
for i in range(int(input())):
    s = input().split('||')
    res = input()
    if len(set(res)) != 10 or len(s) == 1 or s[1] == '':
        print(-1)
    else:
        # print(s)
        # print(res)
        a = solve(s[0])
        if len(s[1]) == 1:
            c = int(s[1][0])
            ans2 = solve3(a, c)
        else:
            b = s[1][:-1]
            d = solve2(a, b)
            c = int(s[1][-1])
            ans2 = solve3(d, c)

        ans = ""
        # print(ans2)
        # print(ans)
        # print(ans2)
        for i in ans2:
            ans += res[i]
        print(ans)
