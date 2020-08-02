def solve(x, y):
    ret = 0
    while True:
        if x == y:
            return ret + 1
        elif x > y:
            x -= y
        elif x < y:
            y -= x
        ret += 1



for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    l = set()
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            l.add((i, j))
    
    cnt = 0
    for i in l:
        cnt += solve(i[0], i[1])
    print(cnt)
