def isgame(x):
    sumi = 0
    while x > 0:
        sumi += (x % 10) * (x % 10)
        x = x // 10
        
    if sumi == 1:
        return True
    if sumi == 4:
        return False
    else:
        return isgame(sumi)
    
        
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

a = input()
b = input()
c = input()
if a.isdigit() and b.isdigit() and c.isdigit() and int(a) > 0 and int(b) > 0 and int(c) > 0:
    a = int(a)
    b = int(b)
    c = int(c)
    l = list()

    for i in range(a, b + 1):
        if isgame(i) and isprime(i):
            l.append(i)

    if len(l) < c:
        print("No number is present at this index")
    else:
        print(l[c - 1])
else:
    print("Invalid Input")  

