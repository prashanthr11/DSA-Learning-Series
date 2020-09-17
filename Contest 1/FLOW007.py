# cook your dish here
n = int(input())

for i in range(n):
    l = list(map(str, input()))

    t = ''
    
    for i in reversed(l):
        t += str(i)
    
    print(int(t))
