def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for i in range(int(input())):
    n = int(input())
    if n > 2:
        l = list()
        ans = list()
        l.append(5)
        for i in range(5,1000):
            if isprime(i):
                l.append(i)
        
        ans.append(5)
        
        sumi = 0
        for i in l:
            sumi += i
            if sumi > n:
                break
            if isprime(sumi):
                ans.append(sumi)
        # print(*l)
        # print(*ans)    
        print(len(ans) - 1)
    else:
        print(0)