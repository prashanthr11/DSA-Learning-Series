for i in range(int(input())):
    n, m = map(int, input().split())
    sumi = 0
    l = list()
    for i in range(m):
        l += list(map(int, input().split()))
    for i in range(1, len(l)):
        sumi += abs(l[i - 1] - l[i])
    print(sumi + l[0])
