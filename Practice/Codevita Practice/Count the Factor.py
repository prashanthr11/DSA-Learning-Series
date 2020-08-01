from math import factorial as ft

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

n = input()
if n.isdigit() and int(n) > 0:
    n = int(n)
    n = ft(n)
    l = list()
    for i in range(2, 10000):
        if isprime(i):
            l.append(i)
    te = 0  
    ans = ""
    cnt = 0
    while n != 1:
        if n % l[te] == 0:
            cnt += 1
            n = n // l[te]
        else:
            ans += str(cnt) + " "
            cnt = 0
            te += 1
    print(ans + str(cnt))            
        
else:
    print('Invalid Input')