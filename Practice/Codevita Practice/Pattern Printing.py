for i in range(int(input())):
    print("Case #{}".format(i + 1))
    n = int(input())
    d = dict()
    t2 = n
    temp = 0
    for i in range(n):
        ans = "**" * (n - t2)
        for j in range(t2):
            ans += str(temp + 1) + "0"
            temp += 1
        t2 -= 1
        d[i] = ans
    temp += 1
    d[n - 1] += str(temp)
    
    for i in range(n - 2, -1, -1):
        ans = ""
        for j in range(1, n - i):
            temp += 1
            ans += str(temp) + "0"
        temp += 1
        ans += str(temp)
        d[i] += ans
        
    for k, v in d.items():
        print(v)