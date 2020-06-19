def isPrime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True


a, b = map(int, input().split())
s = set()
for i in range(a, b + 1):
  if isPrime(i):
    s.add(i)
s2 = set()
l = list(s)
l = [str(i) for i in l]
for i in range(len(l)):
  for j in range(len(l)):
    if i != j:
	    s2.add(int(l[i] + l[j]))
sts = set()
for i in s2:
    if isPrime(i):
        sts.add(i)
ls2 = list(sts)

maxi, mini = max(ls2), min(ls2)
it = len(ls2)
ls4 = list()
ls4.append(mini)
if it == 1:
    print(ls4[-1])
    exit()
    
ls4.append(maxi)
if it == 2:
    print(ls4[-1])
    exit()
    
if it > 2:
    for i in range(2, it):
      ls4.append(ls4[i - 1] + ls4[i - 2])

print(ls4[-1])
